
import importlib, sys, io, inspect, builtins
mod = importlib.import_module('modules.variables_and_data_types.print_your_first_value.exercise.main')
def test_store_name():
    assert isinstance(mod.your_name, str) and mod.your_name
def test_print_name(monkeypatch, capsys):
    importlib.reload(mod)
    captured = capsys.readouterr()
    assert mod.your_name in captured.out
