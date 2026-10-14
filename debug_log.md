# debug_log.md
# Author: Minh Nguyen (AI-assisted role-play reconstruction)

The Student and AI passages below reconstruct a student-led debugging exercise
with limited AI hints, as requested. They are illustrative dialogue, not a
verbatim transcript or evidence of independent student actions. In the original
session, the AI assistant ran the commands, made the edits, and verified the
results. The error messages and final test results are from those actual runs.

## Bug 1

Error type: `KeyError: 'amount'`.

File + line: `week8_buggy.py`, original line 12 in `get_total()`, called from
original line 21. The failing statement is `total += rec['amount']`.

What the error means (Student role): I am asking for a dictionary key that does
not exist. The traceback points to `rec['amount']`, so I need to compare that
spelling with the keys actually stored in the record.

What I told the duck (Student role, written walkthrough):

1. `def get_total(records):` defines my function and names its input `records`.
2. `total = 0` starts the running total at zero each time I call the function.
3. `for rec in records:` takes one dictionary from the list at a time.
4. `total += rec['amount']` reads the exact key `amount` and adds its value.
   If that key is missing, the lookup fails before the addition happens.
5. `return total` sends the accumulated value back after the loop finishes.
   The error prevents this line from running.

What I tried (Student role): I ran the unchanged script, read the traceback from
the bottom, and wrote down the diagnosis before editing. Following the lab, I
added `print(f'DEBUG: rec = {rec}')` before the lookup. The output showed
`DEBUG: rec = {'id': 1, 'name': 'Taylor', 'amout': 1200}`. Comparing the two
spellings helped me find the missing `n` in `amout`.

AI role (brief hint): A `KeyError` refers to a missing dictionary key. Compare
the key in the failing lookup with the keys in the DEBUG output.

How I fixed it (Student role): I renamed the first record's `amout` key to
`amount`, removed the temporary DEBUG print, and reran the script. It printed
`Total: $5150.00 across 3 records`, so the accumulator finished and execution
advanced to the next error.

## Bug 2

Error type: `TypeError: '>' not supported between instances of 'int' and 'str'`.

File + line: `week8_buggy.py`, original line 16 in `is_over_limit()`, called from
original line 23. The failing statement is `return amount > '1000'`.

What the error means (Student role): Python cannot compare an integer and a
string using `>`. I read the new traceback and recorded the two types before
changing the comparison.

What I told the duck (Student role, written walkthrough): The left side,
`amount`, is the integer 5150 returned by `get_total()`. The right side, `'1000'`,
is text because it is surrounded by quotes. My rule needs to compare numbers,
so the threshold should be the integer `1000`.

How I fixed it (Student role): I removed the quotes around `1000` and kept the
`>` operator. Both operands are now numeric, and exactly 1000 still does not
exceed the limit. I reran the script and got the expected two-line output.

AI role (after the proposed fix): Test exactly 1000 as well as values above and
below it to confirm that the strict boundary still works.

The role-play has the student diagnose and fix Bug 2 before requesting this
testing hint. That sequence is illustrative; the original implementation was
AI-assisted, including the Bug 2 edit.

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

Did I use AI? Yes. In this role-play, the student handles the debugging and uses
AI for a short explanation of `KeyError` and a reminder about boundary testing.
In the actual session, AI performed the implementation and verification; the
role-play does not replace that disclosure.

Exact original task prompt, supplied with the attached lab instructions:

> heres what for this lab, handle it, if theres soemthign wrong get back to me, if not keep going

Attachment supplied with that prompt:
`.context/attachments/OsDDtX/pasted_text_2026-10-14_18-46-38.txt`.

Exact prompt requesting this reconstruction:

> for the debug log, you will act as 2 role: myself and AI, myself will handle the debug with little assitance from AI, thats the conext, update the beuglod based on that context

Example student question in the role-play (illustrative, not an actual prompt):

> What does a KeyError mean, and what should I compare in my DEBUG output?

What AI explained (AI role): A missing dictionary key raises `KeyError`; inspect
the literal key used by the lookup and the keys actually in the dictionary.
After the numeric comparison is fixed, boundary testing checks that exactly
1000 returns False. The hints explain how to reason about the failures rather
than supplying a replacement script in the dialogue.

What I changed myself (Student role): I used the traceback and DEBUG output to
find `amout`, changed it to `amount`, removed the temporary print, and changed
`'1000'` to `1000`. I checked the final output and tested the functions, including
the exact threshold. These are the student's actions within the reconstruction;
the actual edits and commands were performed by the AI assistant.

Can I explain every fixed line? Student role: Yes. `amount` must match the
dictionary's key exactly, and numeric `1000` makes the comparison valid without
changing the strict `>` rule. Actual student understanding and an out-loud duck
exercise were not verified in this session.

## What I learned

Student role: I learned to read tracebacks from the bottom and use a temporary
print to inspect the actual data before changing code. Fixing the first error
can reveal another one, so I should rerun after each fix. Testing exactly at the
limit helps me check the difference between `>` and `>=`.
