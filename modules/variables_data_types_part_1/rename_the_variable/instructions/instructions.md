# Rename the Variable

## Learning

Imagine opening someone else’s code and finding variables named `x` or `y`. Without context those letters hide meaning and slow every reader. Clear identifiers act as signposts; poor ones are roadblocks. In this refactoring challenge you will upgrade two mystery labels to expressive alternatives.

Inside the script two variables—`x` storing a lesson title and `y` storing a topic—feed a short f‑string. Your job is to rename `x` to `lesson` and `y` to `topic` everywhere they appear. That includes their declarations and any later references. After renaming, run the program to ensure the output still matches the original.

```python
# before
x = "Variables"
y = "Data Types"
print(f"This lesson covers {x}: {y}")

# after
lesson = "Variables"
topic = "Data Types"
print(f"This lesson covers {lesson}: {topic}")
```

Why bother? When names reveal intent readers spend less time mentally tracing values and more time reasoning about the algorithm. Renaming is therefore a key part of *code hygiene*, the practice of keeping projects comprehensible as they evolve.

The first checkpoint tests that no identifier `x` remains and that `lesson` exists. The second does the same for `y` and `topic`. Be careful: deleting without replacing will cause a `NameError`. A successful run demonstrates you can maintain program behaviour while improving readability—an essential skill for collaborative software development.

Take this moment to appreciate how tiny edits now prevent hours of confusion later. Clarity is kindness; clear variables share that kindness with every future maintainer, including your future self.
