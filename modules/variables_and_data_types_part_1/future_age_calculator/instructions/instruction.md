# Future Age Calculator
## Learning
Your city’s transit authority is designing a smart pass that will adjust fares based on a rider’s age on **1 January 2050**. To prototype the back‑end, you need a script that asks for someone’s birth year, computes how old they will be on that date, and prints a friendly message. Get the formula right and commuters glide through gates; get it wrong and discounts misfire at midnight.

Three ingredients are vital: **input**, **conversion**, and **arithmetic**. The `input()` function fetches raw text from the keyboard. Wrapping that call in `int()` transforms the string into a number you can subtract from the target year. Finally an f‑string stitches numbers and words into clear output.

```python
year_str = input("When were you born? ")
# hint: calculate the future age and greet the user
```

Run this fragment and the programme stalls at the maths step. Your full task has three stages: first, capture the birth year as an `int`; second, store the result in **exactly** the variable `age_in_2050`; third, print a sentence such as “You will be 42 years old on 01/01/2050.” Reuse literals from the description if you wish, but trust that inputs make sense—no need to guard against travellers from the future.

Mastering the trio of reading, processing, and presenting data unlocks almost every real‑world utility script you will write, from calorie trackers to tax calculators. Let’s future‑proof those tickets!
