import importlib, builtins, types, inspect

def test_calculate_age(monkeypatch, capsys):
    inputs = iter(["2000"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    import age_on_2050.exercise.main as m
    importlib.reload(m)
    assert m.age_2050 == 50
    captured = capsys.readouterr()
    assert "50" in captured.out

def test_extra_types():
    import age_on_2050.exercise.main as m
    found_float = any(isinstance(v, float) for v in vars(m).values())
    found_bool = any(isinstance(v, bool) for v in vars(m).values())
    assert found_float and found_bool
