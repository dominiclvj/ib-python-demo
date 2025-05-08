import os, pathlib
import importlib

def test_store_name(capsys):
    from print_your_first_value.exercise import main  # noqa
    importlib.reload(main)
    captured = capsys.readouterr()
    assert isinstance(main.student_name, str) and main.student_name
    assert main.student_name in captured.out

def test_favourite_number(capsys):
    from print_your_first_value.exercise import main  # noqa
    captured = capsys.readouterr()
    assert isinstance(main.favourite_number, int)
    assert str(main.favourite_number) in captured.out
