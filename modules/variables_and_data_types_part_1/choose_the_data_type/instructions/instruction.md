# Choose the Data Type
## Learning
A weather station logs several readings: temperature, station code, and whether its battery is low. While it makes sense to store some of these as text (or a string), if everything is text then performing mathematical calculations becomes impossible. In some cases you might want the computer to quickly evaluate if something is "ON" or "OFF", which a computer could represent as `True` or `False`.

Python offers four data types to handle : `int`, `float`, `str`, and `bool`. These will be assigned automatically by the Python interpreter if you don't tell it which one to use. Or we can tell Python which data type it should use as in the example below.

```python
reading = "23.5"          # starts as text ('str')
celsius = float(reading)  # reassigned to a number ('float')
```

The `type()` function can be used to check a given variable's data type. If in this example you run `print(type(celsius))` then then Output would tell you that the variable was a `float`.

Above we convert a string to a float so maths becomes legal. In the real exercise you will be given mixed inputs such as `"True"` and `31` and must assign each to a variable whose type matches its meaning.

Finish by printing all variables side-by-side to the output. Accurate use of data types here lays the groundwork for robust programs that do not choke on unexpected input.
