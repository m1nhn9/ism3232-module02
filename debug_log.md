# debug_log.md
# Author: Minh Nguyen (AI-assisted debugging session)

This log records commands and edits performed by the AI assistant at the student's
request. The explanations below are written walkthroughs, not a claim that the
student performed the out-loud duck exercise or fixed Bug 2 without AI.

## Bug 1

Error type: `KeyError: 'amount'`.

File + line: `week8_buggy.py`, original line 12 in `get_total()`, called from
original line 21. The failing statement is `total += rec['amount']`.

What the error means: Dictionary access with square brackets raises `KeyError`
when the requested key is absent. The first record has `amout`, not `amount`.

What I told the duck (written AI walkthrough):

1. `def get_total(records):` defines a function taking a collection of records.
2. `total = 0` initializes the accumulator to zero for this function call.
3. `for rec in records:` assigns each dictionary to `rec` in turn.
4. `total += rec['amount']` looks up the literal key `amount` and adds its value
   to `total`. On the first dictionary, that lookup raises an exception before
   anything is added because its key is spelled `amout`.
5. `return total` returns the accumulated number after the loop; execution never
   reaches it during this failing run.

What I tried: Ran the original script without modifying it and read the traceback
from the final error line back to the failing dictionary access. Recorded this
diagnosis before changing the script, then added
`print(f'DEBUG: rec = {rec}')` before the lookup and ran the script again. It
printed `DEBUG: rec = {'id': 1, 'name': 'Taylor', 'amout': 1200}` before failing,
confirming the misspelled key. The program stops on the first record, so later
records are not printed in this failing run.

How I fixed it: Renamed the first record's `amout` key to `amount` and removed
the temporary DEBUG print. The next run printed
`Total: $5150.00 across 3 records`, confirming `get_total()` completed, then
revealed Bug 2.

## Bug 2

Error type: `TypeError: '>' not supported between instances of 'int' and 'str'`.

File + line: `week8_buggy.py`, original line 16 in `is_over_limit()`, called from
original line 23. The failing statement is `return amount > '1000'`.

What the error means: Python cannot order an integer and a string with `>`.
Here `amount` is the integer `5150`, while `'1000'` is a string because it has
quotes. This diagnosis was recorded before changing that statement.

What I told the duck (written AI walkthrough): The left side of `>` is an `int`
containing 5150; the right side is a `str` containing four characters. The rule
needs a comparison of two numbers, so the threshold must be the integer `1000`.
Exactly 1000 must remain False because the operator is `>`, not `>=`.

How I fixed it: Replaced `'1000'` with `1000`, making both sides numeric. The
script then completed successfully with the expected output below. This is
AI-assisted work, so the instruction to fix this without AI first was not met.

Also placed the executable statements under `if __name__ == "__main__":` so
pytest can import the functions without printing the script's demonstration.
Removed the outdated "do not fix yet" header and formatted the finished script
with Ruff. The traceback line numbers above refer to the original, unformatted
script; formatting and the added guard change the final line numbers.

## After Fixing Both Bugs

Final output from `.venv/bin/python week8_buggy.py`:

```text
Total: $5150.00 across 3 records
True
```

Did pytest pass? Yes. All 26 repository tests passed, including the five new
tests in `tests/test_week8.py`. The larger total includes tests from earlier labs.
Ruff formatting and lint checks also passed.

The five new tests check summation, amounts above and below the limit, the exact
1000 boundary, and the complete formatted summary.

Instruction inconsistency: The supplied script's header says "three bugs", but
the lab identifies two bugs and asks for an "After Fixing Both Bugs" section.
Both observed runtime errors were fixed; the supplied `format_summary()` already
produces the required text, so no third functional bug was invented.

## AI Literacy Reflection

Did I use AI? Yes. This work was delegated to an AI coding assistant.

Exact prompt I used, supplied with the attached lab instructions:

> heres what for this lab, handle it, if theres soemthign wrong get back to me, if not keep going

Attachment supplied with that prompt:
`.context/attachments/OsDDtX/pasted_text_2026-10-14_18-46-38.txt`.

What AI explained: A missing dictionary key raises `KeyError`; the DEBUG print
revealed `amout` in the first record. Once that key was corrected, Python reached
the comparison of an integer with a string and raised `TypeError`. Replacing
`'1000'` with numeric `1000` fixes that comparison while keeping the strict `>`
boundary. The main guard separates running the script from importing its
functions for testing.

What I changed myself: No manual student code edits were recorded in this
session. The AI assistant reproduced the errors, edited the two faulty lines,
removed the temporary DEBUG print, added the main guard and five tests, and
prepared this log. The student requested the work; the edits must not be
represented as independently completed without AI.

Can I explain every fixed line? Not verified for the student in this session.
The written explanations are provided above for review. An out-loud duck exercise
and the student's own confirmation of understanding cannot be supplied by the
assistant.

## What I learned

AI-assisted learning summary for the student to review: Reading a traceback from
the bottom identifies the error type and the operation that failed, while a
temporary DEBUG print exposes the actual record reaching that operation.
Correcting one error can reveal another, so rerunning after each change is part
of debugging. Boundary tests confirm that an amount of exactly 1000 does not
exceed a strict approval limit.
