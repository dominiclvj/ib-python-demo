import importlib.util, pathlib, types
from io import StringIO
import sys

SRC = pathlib.Path(__file__).resolve().parent.parent / "exercise" / "main.py"

def load_module(capture=False):
    if capture:
        old_stdout = sys.stdout
        sys.stdout = StringIO()
    spec = importlib.util.spec_from_file_location("student_main", SRC)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if capture:
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        return module, output
    return module

def test_print_name_number():
    module, out = load_module(capture=True)
    assert isinstance(module.pupil_name, str) and module.pupil_name.strip(), "pupil_name should be non-empty string"
    assert isinstance(module.coach_number, int), "coach_number should be int"
    assert module.pupil_name in out, "Output should include pupil_name"
    assert str(module.coach_number) in out, "Output should include coach_number"
