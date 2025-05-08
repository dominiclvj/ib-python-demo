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

def test_declare_correct_types():
    module = load()
    assert isinstance(module.temperature_c, float), "temperature_c should be float"
    assert isinstance(module.station_code, str), "station_code should be string"
    assert isinstance(module.battery_low, bool), "battery_low should be bool"

def test_display_readings():
    module, out = load(capture=True)
    assert str(module.temperature_c) in out and module.station_code in out and str(module.battery_low) in out, "All variables must be printed"
