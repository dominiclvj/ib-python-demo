
import importlib, inspect
mod = importlib.import_module('modules.variables_and_data_types.comment_the_output.exercise.main')
source = inspect.getsource(mod)
def test_comment_line():
    assert source.lstrip().startswith('#')
def test_keep_code():
    assert 'print(' in source
