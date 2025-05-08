import importlib, inspect

def test_comment_silences_output(capsys):
    import comment_the_output.exercise.main as m  # noqa: F401
    captured = capsys.readouterr()
    assert captured.out.strip() == "", "Output should be empty"
    source = inspect.getsource(m)
    assert "# print(" in source or source.strip().startswith("#"), "Print line must be commented, not deleted"
