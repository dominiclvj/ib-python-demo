# Future Age Calculator
## Learning
Your city’s transit authority is designing a smart pass that will adjust fares based on a rider’s age on **1 January 2050**. To prototype the back‑end, you need a script that asks for someone’s birth year, computes how old they will be on that date, and prints a friendly message. Get the formula right and commuters glide through gates; get it wrong and discounts misfire at midnight.

Three ingredients are vital: **input**, **conversion**, and **arithmetic**. The `input()` function fetches raw text from the keyboard. Use what you've learned about data types to convert text input to a numeric format that we can perform calcutions on. Then use an f‑string to stitch numbers and words into a clear output. The following code snippet shows how we can both capture text from the user and present it back to them.

```python
year_str = input("Please input your year of birth ")
print(f"Your year of birth is {year_str}")
```

Your full task has three stages: first, capture the birth year as an `int`; second, store the result in the variable `age_in_2050`; third, print a sentence such as “You will be 42 years old on 01/01/2050.”

Mastering the trio of reading, processing, and presenting data unlocks almost every real‑world utility script you will write, from calorie trackers to tax calculators. Let’s future‑proof those tickets!
