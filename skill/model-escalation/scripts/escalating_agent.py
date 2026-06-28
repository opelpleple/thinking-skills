"""
Escalating Agent — tiered model fallback with cost-aware escalation.

Logic: a cheap model attempts the task. If it fails N times (default 2),
escalate to a more capable, more expensive model. Failure reasons from each
attempt are fed FORWARD so the next model knows exactly what to fix.

The hard part is NOT the escalation loop — it's the `validator`.
Escalation is only as good as your ability to detect a bad output.
See ../references/validators.md for how to build good ones.

Run me:  ANTHROPIC_API_KEY=... python escalating_agent.py
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Callable, Any
import anthropic


# --- 1. Define your tiers, cheapest first ---------------------------------
# Model IDs change over time — confirm the current strings before shipping.
# This enum is the single place to update them.
class Tier(str, Enum):
    CHEAP = "claude-haiku-4-5-20251001"
    MID = "claude-sonnet-4-6"
    EXPENSIVE = "claude-opus-4-8"


@dataclass
class Attempt:
    tier: str
    output: str | None
    ok: bool
    reason: str
    in_tokens: int
    out_tokens: int


@dataclass
class Result:
    success: bool
    output: Any
    attempts: list[Attempt] = field(default_factory=list)

    @property
    def total_tokens(self) -> tuple[int, int]:
        # Plug your own per-token rates in here to convert to real cost.
        return (
            sum(a.in_tokens for a in self.attempts),
            sum(a.out_tokens for a in self.attempts),
        )

    @property
    def winning_tier(self) -> str | None:
        for a in self.attempts:
            if a.ok:
                return a.tier
        return None


class EscalatingAgent:
    def __init__(
        self,
        validator: Callable[[str], tuple[bool, str]],
        tiers: list[Tier] | None = None,
        max_attempts_per_tier: int = 2,
    ):
        self.client = anthropic.Anthropic()
        self.validator = validator  # returns (is_valid, reason_if_not_valid)
        self.tiers = tiers or [Tier.CHEAP, Tier.MID, Tier.EXPENSIVE]
        self.max_attempts = max_attempts_per_tier

    def run(self, task: str, system: str = "") -> Result:
        result = Result(success=False, output=None)

        for tier in self.tiers:
            for _ in range(self.max_attempts):
                prompt = self._with_feedback(task, result.attempts)
                try:
                    out, ti, to = self._call(tier, system, prompt)
                    ok, reason = self.validator(out)
                except Exception as e:
                    out, ok, reason, ti, to = None, False, f"exception: {e}", 0, 0

                result.attempts.append(
                    Attempt(tier.value, out, ok, reason, ti, to)
                )

                if ok:
                    result.success = True
                    result.output = out
                    return result

            # this tier used up its attempts → escalate to next, pricier tier
            print(f"escalating: {tier.value} failed {self.max_attempts}x")

        return result  # every tier failed

    def _with_feedback(self, task: str, attempts: list[Attempt]) -> str:
        """Feed prior failure reasons forward — this is what makes escalation worth paying for."""
        fails = [a for a in attempts if not a.ok]
        if not fails:
            return task
        notes = "\n".join(f"- a previous attempt failed: {a.reason}" for a in fails)
        return f"{task}\n\nPrevious attempts failed. Do NOT repeat these mistakes:\n{notes}"

    def _call(self, tier: Tier, system: str, prompt: str) -> tuple[str, int, int]:
        msg = self.client.messages.create(
            model=tier.value,
            max_tokens=4000,
            system=system or "You are a precise task executor. Output only what is asked.",
            messages=[{"role": "user", "content": prompt}],
        )
        return msg.content[0].text, msg.usage.input_tokens, msg.usage.output_tokens


# --- 2. The REAL work: define what "failure" means -------------------------
# (See ../references/validators.md for the full treatment.)

# Example A: strict JSON schema (structural — fast, free, deterministic)
def json_validator(required_keys: set[str]):
    import json

    def check(output: str) -> tuple[bool, str]:
        text = output.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
        try:
            data = json.loads(text)
        except json.JSONDecodeError as e:
            return False, f"invalid JSON: {e}"
        if not isinstance(data, dict):
            return False, "expected a JSON object"
        missing = required_keys - data.keys()
        if missing:
            return False, f"missing required keys: {sorted(missing)}"
        return True, ""

    return check


# Example B: code must actually run (executable — ground truth)
# NOTE: only run model-generated code in a sandbox / trusted environment.
def python_runs_validator(output: str) -> tuple[bool, str]:
    import subprocess, tempfile, os

    code = output.strip().removeprefix("```python").removeprefix("```").removesuffix("```").strip()
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
        f.write(code)
        path = f.name
    try:
        r = subprocess.run(["python", path], capture_output=True, text=True, timeout=10)
        if r.returncode != 0:
            return False, f"runtime error: {r.stderr[-400:]}"
        return True, ""
    except subprocess.TimeoutExpired:
        return False, "timed out (possible infinite loop)"
    finally:
        os.unlink(path)


# --- 3. Use it -------------------------------------------------------------
if __name__ == "__main__":
    agent = EscalatingAgent(
        validator=json_validator({"broker_name", "trust_score", "license_status"}),
        max_attempts_per_tier=2,
    )

    res = agent.run(
        task=(
            "Extract broker info as a JSON object with exactly these keys: "
            "broker_name, trust_score, license_status.\n"
            "Source text: 'XM Group, regulated by CySEC, our trust rating is 8.4/10.'"
        )
    )

    ti, to = res.total_tokens
    print(f"\nsuccess={res.success}  winning_tier={res.winning_tier}")
    print(f"attempts={len(res.attempts)}  tokens={ti}in / {to}out")
    for a in res.attempts:
        print(f"  {a.tier:32} ok={a.ok}  {a.reason[:50]}")
    if res.success:
        print("\noutput:\n", res.output)
