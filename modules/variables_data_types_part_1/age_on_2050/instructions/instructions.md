# Age on 2050

## Learning

Programs excel at boring arithmetic, freeing humans for creative thinking. In this extended exercise you will write a script that projects a person’s age on 1 January 2050. The task combines variables, input, and simple maths—capstones for today’s lesson.

First prompt the user for their birth year with `input()`. Convert the response to an `int` immediately, because raw input arrives as a `str` and cannot be subtracted from another integer.

```python
birth_year = int(input("Enter your birth year: "))
age_2050 = 2050 - birth_year
print(f"You will be {age_2050} years old on 01/01/2050.")
```

Add two more variables of different primitive types: choose one `float` (perhaps an approximate life expectancy) and one `bool` (maybe `is_leap_year`). These extra declarations prove you can juggle multiple types within a single script.

The first checkpoint verifies that `age_2050` is correct given the supplied year. The second scans the file to confirm at least one `float` and one `bool` literal are present. Avoid hard‑coding age values; your script must work for anyone born in any year.

Although the arithmetic is trivial, the exercise mirrors real software that must read external data, cast it safely, compute results, and communicate them clearly. When you see the personalised message appear you will have stitched together many threads: console I/O, type conversion, variables, and subtraction. Take pride—this is a complete, user‑facing program, not just a code snippet. The skills you apply here will resurface in loops, conditionals, and full projects to come.
