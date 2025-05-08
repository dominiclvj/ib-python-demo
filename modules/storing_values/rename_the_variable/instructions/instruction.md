# Rename the Variable

## Learning
Clear names are the difference between code that whispers its purpose and code that snarls in confusion. Python lets you bind any value to any identifier, but human readers will judge you by the clarity of those identifiers. In this exercise you will replace a vague variable name with one that broadcasts intent.

The starter script stores the string `"Computer Science"` inside a variable called `lesson`. Three print statements display that value in different formats. While nothing is technically wrong, the word *lesson* is too generic: does it refer to a time slot, a topic, or a moral? A single rename will remove the ambiguity.

Your task is to change **both** the variable declaration **and** every reference so the identifier becomes `subject`. After refactoring, the program should run unchanged, still printing the original three messages. Python will not hold a grudge if you remove the old name entirely, but the new one must exist and point at the same string.

This micro‑refactor reveals how naming choices influence readability. A good name turns raw data into self‑explanatory prose. As projects grow, precise naming prevents logic errors and accelerates team comprehension. Treat variables like well‑labelled containers: anyone should know their contents at a glance.
