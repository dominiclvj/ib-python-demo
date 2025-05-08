## Learning
Meaningful names turn cryptic code into a readable story. While `x = 5` may work, `student_score = 5` tells the next reader exactly what is stored. Python lets you refactor freely: just change the identifier everywhere it appears.  

In the starter file you will find `bad_name`, a nondescript variable printed three times. Your task is to rename it to `lesson`—a clearer label—then ensure each print statement still works.  

```python
bad_name = "Variables Rock"
print(bad_name)
```

becomes  

```python
lesson = "Variables Rock"
print(lesson)
```

Take care to update every reference; a single leftover will raise a `NameError`. Run the program and watch the original message appear three times, proving the refactor kept behaviour intact.  

This challenge flexes two muscles: trace‑reading existing code and improving its clarity—an essential habit for collaborative projects.
