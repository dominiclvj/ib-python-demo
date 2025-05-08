import importlib, inspect, builtins

def test_print_values_output(capsys):
    import print_your_first_value.exercise.main  # noqa: F401
    captured = capsys.readouterr().out.strip().split()
    assert any(item.isdigit() for item in captured), "No integer printed"
    assert any(not item.isdigit() for item in captured), "No string printed"
