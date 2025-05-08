---
exercise_name: Rename the Variable
concept: variables
difficulty: 2
est_minutes: 6
tags:
- comments-style
- io
---

# Rename the Variable
## Learning
Picture a librarian labelling boxes simply “Thing 1” and “Thing 2”. Colleagues waste minutes opening lids before they find mystery novels or science magazines. Programmers face the same frustration when variables have vague names, yet a renaming takes seconds and yields lasting clarity.

In Python you can reassign a variable or create a new one, but the smartest move is to give it a meaningful label from the outset. Changing every reference is painless, yet forgetting a single spot produces a `NameError` and halts the script.

```python
temp = "Giacometti"
print(temp)        # hint: rename 'temp' to reveal the artist's role
```

The snippet prints a surname stored in the catch‑all identifier `temp`. Paste it into your project and your peers will still ask “What is temp?” Your mission is to refactor the skeletal code by replacing placeholder names with expressive ones—no extra logic required. Then display each reassigned value in sequence to trace how state changes through the day.

Along the way you will glimpse Python’s dynamic typing: changing an identifier’s name changes nothing about the underlying data, yet the boost to readability is enormous. Consistent naming also primes you for later topics like scope, where a stray identifier can shadow another and introduce subtle bugs. Practise now; future teammates—and your examiners—will thank you.
