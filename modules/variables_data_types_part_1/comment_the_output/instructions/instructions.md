# Comment the Output

## Learning

Sometimes code speaks too loudly. A runaway print statement can flood the console or reveal information you did not intend to share. Programmers silence such lines with a comment: text that the interpreter skips entirely. In Python the comment symbol is a single hash `#`. Anything after it on the same line is ignored when the script runs.

```python
print("Visible line")
# print("This line is muted")
```

Above, only the first call reaches the console. Comments are not just for muting code, they double as notes to remind future readers why a decision was made. Good comments explain intent rather than restating the obvious.

In this exercise a rogue `print()` already lives in *main.py*. Your mission is simple: disable that line by placing a `#` at its start, without deleting the function call itself. When you run the program the output pane should remain empty, demonstrating that the statement has been bypassed.

Although the task is tiny it teaches a valuable debugging habit. Commenting out code lets you experiment safely, step through problems, and compare results without losing earlier versions. Make sure to keep the spacing neat—many teams expect one space after the hash to aid readability.

Achieving a blank console here is your checkpoint. Once you are certain nothing prints, run the tests to confirm success and reflect on how a single character can control the flow of a program. You will rely on this trick constantly as scripts grow larger, so master it now while the stakes are small.
