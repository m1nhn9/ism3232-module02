# debug_log.md
# Author: Minh Nguyen (AI-assisted debugging session)

I do the explanations and AI hints below describe the debugging
reasoning. The AI assistant executed the commands and code edits in this session;
the notes are not a transcript of separate student and AI actions. Error messages
and test results are from the actual runs.

## Bug 1

Error type: `KeyError: 'amount'`.

File + line: `week8_buggy.py`, original line 12 in `get_total()`, called from
original line 21. The failing statement is `total += rec['amount']`.

What the error means (Student explanation): I am asking for a dictionary key that does
not exist. The traceback points to `rec['amount']`, so I need to compare that
spelling with the keys actually stored in the record.

What I told the duck (Student explanation, written walkthrough):

1. `def get_total(records):` defines my function and names its input `records`.
2. `total = 0` starts the running total at zero each time I call the function.
3. `for rec in records:` takes one dictionary from the list at a time.
4. `total += rec['amount']` reads the exact key `amount` and adds its value.
   If that key is missing, the lookup fails before the addition happens.
5. `return total` sends the accumulated value back after the loop finishes.
   The error prevents this line from running.

What I tried: The unchanged script was run and the traceback was read from the
bottom. The diagnosis was recorded before adding
`print(f'DEBUG: rec = {rec}')` before the lookup. The output showed
`DEBUG: rec = {'id': 1, 'name': 'Taylor', 'amout': 1200}`.

Student explanation: The lookup uses `amount`, but the record stores `amout`.
Comparing those spellings reveals the missing `n`.

AI hint: A `KeyError` refers to a missing dictionary key. Compare
the key in the failing lookup with the keys in the DEBUG output.

How I fixed it: The first record's `amout` key was renamed to `amount`, the
temporary DEBUG print was removed, and the script was rerun. It printed
`Total: $5150.00 across 3 records`, so the accumulator finished and execution
advanced to the next error.

## Bug 2

Error type: `TypeError: '>' not supported between instances of 'int' and 'str'`.

File + line: `week8_buggy.py`, original line 16 in `is_over_limit()`, called from
original line 23. The failing statement is `return amount > '1000'`.

What the error means (Student explanation): Python cannot compare an integer and
a string using `>`. The traceback identifies the two incompatible types.

What I told the duck (Student explanation, written walkthrough): The left side,
`amount`, is the integer 5150 returned by `get_total()`. The right side, `'1000'`,
is text because it is surrounded by quotes. My rule needs to compare numbers,
so the threshold should be the integer `1000`.

How I fixed it: The quotes around `1000` were removed while keeping the `>`
operator. Both operands are now numeric, and exactly 1000 still does not exceed
the limit. Rerunning the script produced the expected two-line output.

AI hint: Test exactly 1000 as well as values above and
below it to confirm that the strict boundary still works.

Verified implementation detail: The executable statements are under
`if __name__ == "__main__":` so importing the functions does not print the
demonstration. Ruff formatted the finished script. The traceback line numbers
above refer to the original script, before formatting and the main guard.

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

Did I use AI? Yes. AI assisted with explaining the errors and performed the
implementation, testing, and documentation in this session.

What AI explained: A missing dictionary key raises `KeyError`; inspect
the literal key used by the lookup and the keys actually in the dictionary.
After the numeric comparison is fixed, boundary testing checks that exactly
1000 returns False.

What I changed myself: I requested assistance and a revision of the explanation.
The assistant made the code edits: `amout` became `amount`, `'1000'` became
`1000`, and the temporary DEBUG print was removed. The assistant also added the
main guard and tests. No independent student code edits were recorded here.

Can I explain every fixed line? Student understanding has not been verified in
this session. The explanation to review is that `amount` must match the
dictionary's key exactly, and numeric `1000` makes the comparison valid without
changing the strict `>` rule.

## What I learned

Reading tracebacks from the bottom and temporarily printing the actual data
helps locate a failure before changing code. Fixing the first error can reveal
another one, so rerunning after each fix is important. Testing exactly at the
limit checks the difference between `>` and `>=`.
