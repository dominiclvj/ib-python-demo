import os, pathlib, ast

SOURCE_FILE = os.path.join(pathlib.Path(__file__).parent, "..", "exercise", "main.py")

with open(SOURCE_FILE, "r") as f:
    tree = ast.parse(f.read())

names_in_code = {n.id for n in ast.walk(tree) if isinstance(n, ast.Name)}

def test_rename_lesson():
    assert "lesson" in names_in_code and "x" not in names_in_code

def test_rename_topic():
    assert "topic" in names_in_code and "y" not in names_in_code
