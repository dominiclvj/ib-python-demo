
import importlib, builtins, sys, io
def reload_module(monkeypatch):
    monkeypatch.setattr(builtins, 'input', lambda _: '2000')
    return importlib.import_module('modules.variables_and_data_types.future_age_calculator.exercise.main')
def test_read_year(monkeypatch):
    mod = reload_module(monkeypatch)
    assert isinstance(mod.birth_year, int)
def test_calculate_age(monkeypatch):
    mod = reload_module(monkeypatch)
    assert mod.age_2050 == 50
def test_display_message(monkeypatch, capsys):
    mod = reload_module(monkeypatch)
    captured = capsys.readouterr()
    assert '50' in captured.out
