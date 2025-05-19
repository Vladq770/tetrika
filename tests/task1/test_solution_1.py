import pytest

from task1.solution import foo, foo_v2, sum_two


@pytest.mark.parametrize(
    "a, b, expected_result, function",
    [
        (1, 2, 3, sum_two),
        (1, 2, None, foo),
        (1.0, 2, None, foo),
        (1, "2", None, foo),
        (1.0, "2", None, foo),
        (1, 2, 3, sum_two),
        (1, 2, 3, sum_two),
        (1, 2, None, foo_v2),
        (1.0, 2, None, foo_v2),
        (1, "2", None, foo_v2),
        (1.0, "2", None, foo_v2),
        ("1", 1, None, foo_v2),
        ("1.", "2", None, foo_v2),
    ],
)
def test_strict(a, b, expected_result, function):
    assert function(a, b) == expected_result


@pytest.mark.parametrize(
    "a, b, function",
    [
        (1, 2.0, sum_two),
        ("1", 2, sum_two),
        ("1.", "2", foo),
    ],
)
def test_strict_with_type_error(a, b, function):
    with pytest.raises(TypeError, match="Argument "):
        function(a, b)
