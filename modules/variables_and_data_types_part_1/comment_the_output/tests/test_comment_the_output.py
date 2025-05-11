import os
import pathlib

def test_silence_greeting(capsys):
    """
    Program should produce no output but still contain print statement
    """
    from exercise import main
    captured = capsys.readouterr()
    assert captured.out == ""

    with open(os.path.join(pathlib.Path(__file__).parent, "..","exercise", "main.py"), "r") as file:
        content = file.read()
        assert "print(" in content
