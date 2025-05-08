## Learning
Programmers talk to both the machine and future humans. Comments are the whispers we leave for people while the interpreter politely looks away. Anything after `#` on a line is ignored by Python, letting you explain intent, disable code temporarily, or sketch ideas in plain language.  

Consider a loud script:  

```python
# Developer greeting
print("Noise!")
```

Remove the hash and it prints; reinstate it and silence returns. This simple switch is your new debugging ally.  

In this exercise a rogue print statement shouts every time the file is run. Your mission is to quiet it without deleting the line. Add `#` at the very start so the interpreter skips the call, then run the script. If nothing appears in the output pane you have succeeded. Leave the rest of the code untouched—future you (or a teammate) might want to restore the line later by removing the hash.  

By mastering comments you improve code readability and gain a reversible mute button for experiments.
