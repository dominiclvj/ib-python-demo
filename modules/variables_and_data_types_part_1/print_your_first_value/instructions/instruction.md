---
exercise_name: Print Your First Value
concept: io
difficulty: 1
est_minutes: 5
tags:
- variables
- data-types
---

# Print Your First Value
## Learning
You have just been hired to create personalised wristbands for a school trip. Each band must show the pupil’s name and their assigned coach number so teachers can match students to buses. If your script prints only one detail, the boarding queue descends into chaos.

A variable is simply a labelled box in memory. When you write `name = "Mina"` you reserve storage tagged *name* and drop “Mina” inside. The `print()` function peeks inside a box and shows its contents in the terminal window. Because computers ignore vertical spacing, the order you place statements decides which line appears first. Choosing clear identifiers prevents future confusion when someone else reads your code.

```python
alias = "Echo"          # placeholder identifier
print(alias)
# hint: also show the matching seat number
```

The snippet gives an idea but stops short of completion—it never stores or displays a number. Your task is to declare a second variable for the coach number and print both pieces of information, either with two `print()` calls or an f‑string. Pick sensible names and remember that strings need quotes while integers do not. Beyond this micro‑task lies the habit of combining separate pieces of data so humans can act quickly; the same steps power boarding passes, shipping labels, and countless other everyday tools.

When both values appear on screen you will know the wristbands are legible and the buses can roll without confusion.
