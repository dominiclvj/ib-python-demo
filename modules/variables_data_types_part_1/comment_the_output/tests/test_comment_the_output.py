import os, pathlib, importlib

def test_comment_line(capsys):
    from comment_the_output.exercise import main  # noqa
    importlib.reload(main)
    captured = capsys.readouterr()
    assert captured.out.strip() == ""
    with open(os.path.join(pathlib.Path(__file__).parent, "..", "exercise", "main.py"), "r") as file:
        content = file.read()
        assert "print(" in content
