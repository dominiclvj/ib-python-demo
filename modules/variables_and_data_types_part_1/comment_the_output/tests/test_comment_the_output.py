import importlib.util, pathlib, sys, builtins
from io import StringIO

SRC = pathlib.Path(__file__).resolve().parent.parent / "exercise" / "main.py"

def load_output():
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    spec = importlib.util.spec_from_file_location("student_main", SRC)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    return output

def test_silence_greeting():
    output = load_output()
    assert output.strip() == "", "Program should produce no output"

    # verify print statement still exists but is commented
    text = SRC.read_text().splitlines()
    commented = any(line.lstrip().startswith("#") and "print(" in line for line in text)
    assert commented, "print line must remain but be commented out"
