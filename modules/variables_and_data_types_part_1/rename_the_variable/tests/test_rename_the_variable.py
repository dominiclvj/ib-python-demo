import importlib.util, pathlib, sys
from io import StringIO

SRC = pathlib.Path(__file__).resolve().parent.parent / "exercise" / "main.py"

def load(capture=False):
    if capture:
        old_stdout = sys.stdout
        sys.stdout = StringIO()
    spec = importlib.util.spec_from_file_location("student_main", SRC)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if capture:
        out = sys.stdout.getvalue()
        sys.stdout = old_stdout
        return module, out
    return module

def test_refactor_identifiers():
    module, out = load(capture=True)
    assert hasattr(module, "morning_lesson") and hasattr(module, "afternoon_lesson"), "Expected renamed variables"
    assert isinstance(module.morning_lesson, str) and isinstance(module.afternoon_lesson, str)
    assert "x" not in module.__dict__, "Placeholder variable x should be removed"
    assert "y" not in module.__dict__, "Placeholder variable y should be removed"
    assert module.morning_lesson in out and module.afternoon_lesson in out, "Both lessons should be printed"
