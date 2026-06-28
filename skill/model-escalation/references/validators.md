# Validators — how to detect failure

Escalation is only as good as your ability to tell that an output is bad. This is where almost all the real engineering goes. There are three classes of validator. Reach for them in this order — cheaper and more deterministic first.

## Table of contents
1. Structural validators (fast, free, deterministic)
2. Executable validators (ground truth)
3. LLM-as-judge (flexible, but costs and noise)
4. Composing validators
5. Common mistakes

---

## 1. Structural validators

The output must satisfy a hard, checkable shape: parses as JSON, matches a schema, contains required fields, matches a regex, is within a length bound, picks from an allowed enum.

**Use when** the task has any enforceable format. This should be your default whenever possible — it is instant, free, and never wrong.

```python
import json
from pydantic import BaseModel, ValidationError

class BrokerRecord(BaseModel):
    broker_name: str
    trust_score: float
    license_status: str

def validate(output: str) -> tuple[bool, str]:
    text = output.strip().removeprefix("```json").removesuffix("```").strip()
    try:
        BrokerRecord.model_validate_json(text)
        return True, ""
    except ValidationError as e:
        return False, str(e)  # Pydantic's message is specific — great feedback to feed forward
```

Pydantic is ideal here because its error messages name exactly which field was wrong and why — exactly the feedback you want to append to the next attempt.

**Tip:** push as much correctness into structure as you can. "Score must be 0–10" as a validator field is better than hoping the model stays in range. The more you can encode as schema, the less you need the slower validators below.

---

## 2. Executable validators

The output is run against reality: code must compile/run, unit tests must pass, generated SQL must execute (and ideally return a sane row count), a generated regex must match known positive cases and reject negatives, a config must load.

**Use when** the output is something a machine can execute or check against ground truth. This is the strongest signal you can get — there is no arguing with a failing test.

```python
import subprocess, tempfile, os

def code_passes_tests(output: str, test_file: str) -> tuple[bool, str]:
    code = output.strip().removeprefix("```python").removesuffix("```").strip()
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False, dir=".") as f:
        f.write(code)
        path = f.name
    try:
        r = subprocess.run(["pytest", test_file, "-q"], capture_output=True, text=True, timeout=30)
        return (r.returncode == 0, r.stdout[-600:] if r.returncode else "")
    finally:
        os.unlink(path)
```

**Safety:** model-generated code is untrusted. Run it in a sandbox / container / restricted environment, never with credentials or write access to anything that matters.

---

## 3. LLM-as-judge

A model scores the output against a rubric; below a threshold counts as failure. Use this only when correctness genuinely can't be reduced to a structural or executable check — e.g. "is this summary faithful and on-brand," "did the reply actually answer the question."

```python
def llm_judge(output: str, rubric: str, client, judge_model: str) -> tuple[bool, str]:
    prompt = (
        f"Score this output from 1-10 against the rubric. "
        f"Reply with ONLY JSON: {{\"score\": int, \"reason\": str}}.\n\n"
        f"Rubric:\n{rubric}\n\nOutput:\n{output}"
    )
    msg = client.messages.create(
        model=judge_model, max_tokens=300,
        messages=[{"role": "user", "content": prompt}],
    )
    import json
    verdict = json.loads(msg.content[0].text)
    passed = verdict["score"] >= 7
    return passed, "" if passed else f"judge scored {verdict['score']}/10: {verdict['reason']}"
```

**Critical:** do **not** judge with the same model that just failed — it tends to bless its own bad output. Judge with a *mid* tier (the one you'd escalate to), or a separate model. Note that a judge is itself an LLM call, so it adds cost and a little noise; budget for it.

---

## 4. Composing validators

Real tasks usually want a cheap gate first, then a stronger one only if the cheap gate passes:

```python
def composite(output: str) -> tuple[bool, str]:
    ok, reason = structural_check(output)   # instant, free
    if not ok:
        return False, reason
    return executable_check(output)         # only runs if structure is valid
```

Order matters: never spend an executable or judge call on output that already failed a free structural check.

---

## 5. Common mistakes

- **No validator at all** — "retry on exception" only catches crashes, not wrong answers. A model returning confident nonsense in valid JSON passes silently. This is the most common and most expensive mistake.
- **Vague failure reasons** — "output was bad" teaches the next attempt nothing. Return *specific* reasons ("missing key `license_status`", "score 14 exceeds max 10"); they get fed forward and are the difference between a fix and a repeat.
- **Judging with the failing model** — see above.
- **Validator stricter than the task** — if your check rejects outputs a human would accept, you will escalate forever and burn money. Calibrate the validator against a handful of known-good outputs before trusting it.
