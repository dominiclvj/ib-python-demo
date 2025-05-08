import importlib

def test_variable_renamed():
    import rename_the_variable.exercise.main as m  # noqa: F401
    assert hasattr(m, "subject"), "Variable 'subject' not found"
    assert not hasattr(m, "lesson"), "Variable 'lesson' should be renamed or removed"
