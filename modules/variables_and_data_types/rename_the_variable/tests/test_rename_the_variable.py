
import importlib, inspect, sys, io
mod = importlib.import_module('modules.variables_and_data_types.rename_the_variable.exercise.main')
def test_rename_variable():
    source = inspect.getsource(mod)
    assert 'lesson' in source and 'bad_name' not in source
def test_update_prints(capsys):
    importlib.reload(mod)
    captured = capsys.readouterr()
    assert captured.out.strip().splitlines().__len__() == 3
