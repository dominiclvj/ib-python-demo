import importlib, builtins

def _run(monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda _: "2000")
    mod = importlib.import_module("age_calculator_2050.exercise.main")
    importlib.reload(mod)
    return mod

def test_birth_year_int(monkeypatch):
    mod = _run(monkeypatch)
    assert isinstance(mod.birth_year, int), "birth_year must be int"

def test_age_calculation(monkeypatch):
    mod = _run(monkeypatch)
    assert mod.age_2050 == 50, "age_2050 calculation incorrect"

def test_bool_and_float(monkeypatch):
    mod = _run(monkeypatch)
    bool_found = any(isinstance(v, bool) for v in vars(mod).values())
    float_found = any(isinstance(v, float) for v in vars(mod).values())
    assert bool_found, "Add at least one bool variable"
    assert float_found, "Add at least one float variable"
