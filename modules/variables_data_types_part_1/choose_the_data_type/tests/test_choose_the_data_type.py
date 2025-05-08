import importlib, inspect, builtins, io, sys, ast, os, pathlib

SOURCE_FILE = os.path.join(pathlib.Path(__file__).parent, "..", "exercise", "main.py")

def test_declare_types(monkeypatch, capsys):
    import choose_the_data_type.exercise.main as m
    importlib.reload(m)
    assert isinstance(m.year, int)
    assert isinstance(m.pi, float)
    assert isinstance(m.greeting, str)
    assert isinstance(m.is_sunny, bool)
    captured = capsys.readouterr()
    assert str(m.year) in captured.out
