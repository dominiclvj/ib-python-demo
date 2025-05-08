# Comment the Output

## Learning
Programmers often leave notes to future readers, including themselves, directly inside their code. In Python a note begins with the hash symbol `#`. Everything that follows on the same line is ignored when the program runs. Comments explain intent, record decisions, or temporarily silence lines while you experiment.

Today you will practise that last use‑case. The starter script contains a print statement that shouts a test message whenever it runs. Loud messages are helpful while you debug but distracting once the code works. Rather than deleting the line—and losing its history—you will turn it off with a comment.

Scan the file until you find `print("Debug me!")`. Place `#` before the word `print` so the interpreter treats the whole line as harmless text. The code should still show the now‑silent line to any human reader, proving your respect for traceability, but it must produce **no visible output** when executed.

Commenting is a tiny action with big consequences. It teaches precision: one character changes program behaviour without rewriting logic. It also models professional habits where readable comments and intentional silence keep projects maintainable. Master this micro‑skill now; your future debugging sessions will thank you.
