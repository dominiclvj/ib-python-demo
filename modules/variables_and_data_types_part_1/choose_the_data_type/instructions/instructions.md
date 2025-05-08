---
exercise_name: Choose the Data Type
concept: data-types
difficulty: 2
est_minutes: 8
tags:
- variables
- io
---

# Choose the Data Type
## Learning
A weather station logs several readings: temperature, station code, and whether its battery is low. If you store everything as text, numeric averages become impossible; store everything as numbers and you lose the difference between “ON” and `True`. Picking the right data type is like selecting the correct measuring jug—pour milk into a sieve and you regret it.

Python offers four primitives you have met today: `int`, `float`, `str`, and `bool`. The `type()` function confirms a variable’s nature, and implicit coercion sometimes swaps types behind your back. A savvy coder therefore decides explicitly which container to use before data ever flows.

```python
reading = "23.5"          # starts as text
celsius = float(reading)  # hint: also record if sensor is offline
```

Above we convert a string to a float so maths becomes legal, but we never capture the Boolean status. In the real exercise you will be given mixed inputs such as `"True"` and `31` and must assign each to a variable whose type matches its meaning. Checks will confirm both the value and the underlying class, so casting errors surface quickly.

Finish by printing all variables neatly; seeing values side by side reinforces the link between literal appearance and internal representation. Accurate classification here lays the groundwork for robust programs that do not choke on unexpected input.
