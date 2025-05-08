import importlib.util, pathlib, sys
from io import StringIO

SRC = pathlib.Path(__file__).resolve().parent.parent / "exercise" / "main.py"

def run_with_input(fake_input):
    def mock_input(prompt=""):
        return fake_input
    import builtins
    old_input = builtins.input
    builtins.input = mock_input
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        spec = importlib.util.spec_from_file_location("student_main", SRC)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        output = sys.stdout.getvalue()
    finally:
        builtins.input = old_input
        sys.stdout = old_stdout
    return module, output

def test_get_birth_year():
    module, _ = run_with_input("2000")
    assert isinstance(module.birth_year, int), "birth_year should be int"

def test_compute_future_age():
    module, _ = run_with_input("1990")
    expected = 2050 - 1990
    assert hasattr(module, "age_in_2050"), "age_in_2050 variable missing"
    assert module.age_in_2050 == expected, "age_in_2050 value incorrect"

def test_greet_user():
    module, out = run_with_input("1985")
    assert str(module.age_in_2050) in out, "Output should include computed age"
