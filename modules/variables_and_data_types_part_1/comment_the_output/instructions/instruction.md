# Comment the Output
## Learning
Imagine you are drafting safety messages for an airport departure board. One line mistakenly repeats an outdated announcement, causing passengers to wander needlessly. Rather than delete it (you might want to keep it for future use) you decide to silence the line temporarily.

In Python, the **hash** symbol (`#`) mutes every character that follows on the same line, keeping the code for reference but preventing it from executing. Comments also document intent and park experiments without risk. Unlike strings, they are never stored in memory or shipped to the processor; the Python interpreter skips them entirely.

```python
# old_gate_message = "Flight AB123 departs at 09:05"
display("Welcome travellers!")  # shows the greeting; the first line is ignored
```

Here a variable assignment is prefixed with `#`, turning it into plain text. In the exercise you need to locate an active `print()` statement and transform it into a comment while leaving the rest of the file untouched.

Mastering selective commenting equips you to manage noisy output gracefully and keeps potentially useful code close at hand.
