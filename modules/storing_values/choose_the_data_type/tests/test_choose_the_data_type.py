import importlib

def test_correct_types():
    import choose_the_data_type.exercise.main as m  # noqa: F401
    assert isinstance(m.an_integer, int), "an_integer must be int"
    assert isinstance(m.a_float, float), "a_float must be float"
    assert isinstance(m.a_string, str), "a_string must be str"
    assert isinstance(m.a_boolean, bool), "a_boolean must be bool"
