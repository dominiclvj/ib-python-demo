---
exercise_name: Comment the Output
concept: comments-style
difficulty: 1
est_minutes: 5
tags:
- io
- variables
---

# Comment the Output
## Learning
Imagine you are drafting safety messages for an airport departure board. One line mistakenly repeats an outdated announcement, causing passengers to wander needlessly. Rather than delete it—future regulations might revive that notice—you decide to silence the line temporarily.

In Python, the **hash** symbol (`#`) mutes every character that follows on the same line, keeping the code for reference but preventing accidental execution. Comments also document intent and park experiments without risk. Unlike strings, they are never stored in memory or shipped to the processor; the interpreter skips them entirely.

```python
# old_gate_message = "Flight AB123 departs at 09:05"
display("Welcome travellers!")  # shows the greeting; the first line is ignored
```

Here a variable assignment is prefixed with `#`, turning it into plain text. If you pasted this snippet straight into your programme it would still print something, defeating your purpose. The real task is to locate an active `print()` statement and transform it into a comment while leaving the rest of the file untouched. The precise silence you achieve today will let you toggle any feature on and off in seconds—vital when debugging under pressure or showcasing alternatives during lessons.

Mastering selective commenting equips you to manage noisy output gracefully and keeps potentially useful code close at hand.
