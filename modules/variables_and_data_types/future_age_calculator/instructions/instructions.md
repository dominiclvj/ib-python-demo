## Learning
Fast‑forwarding through time is simple arithmetic once a birth year sits safely in memory. By combining input, type conversion and subtraction you can ask Python to predict someone’s age on any future date.  

The script should:  
1. Read a birth year from the keyboard with `input()`  
2. Convert that string to an `int` called `birth_year`  
3. Compute `age_2050` as `2050 - birth_year`  
4. Print a friendly sentence announcing the result  

Remember that `input()` always returns a string, so you must wrap it in `int()` before maths will work. Use an f‑string for a polished message:  

```python
print(f"In 2050 you will be {age_2050} years old.")
```  

Complete each step and run the program, trying a few different birth years to see the output change. This challenge ties together variables, data types, arithmetic and I/O—the core toolkit for real‑world scripts.
