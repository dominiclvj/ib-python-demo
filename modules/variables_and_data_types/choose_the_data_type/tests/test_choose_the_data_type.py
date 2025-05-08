
import importlib, inspect
mod = importlib.import_module('modules.variables_and_data_types.choose_the_data_type.exercise.main')
def test_declare_types():
    assert isinstance(mod.temp_int, int) and isinstance(mod.temp_float, float) and isinstance(mod.temp_bool, bool)
def test_explain_choice():
    source = inspect.getsource(mod)
    assert '#' in source
