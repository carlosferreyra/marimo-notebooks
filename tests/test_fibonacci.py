import pytest

from notebooks.fibonacci import app


def test_fibonacci_function():
    """Test the fibonacci sequence generation function"""
    # Get the fibonacci function from the app's namespace
    fibonacci = app.get_cell_value("fibonacci")

    # Test basic sequence generation
    assert fibonacci(1) == [0]
    assert fibonacci(2) == [0, 1]
    assert fibonacci(5) == [0, 1, 1, 2, 3]

    # Test edge cases
    with pytest.raises(TypeError):
        fibonacci("not a number")


def test_slider_bounds():
    """Test that the slider stays within defined bounds"""
    n = app.get_cell_value("n")

    assert n.component.min == 1
    assert n.component.max == 100
    assert isinstance(n.value, int)
    assert 1 <= n.value <= 100


def test_fibonacci_sequence_validity():
    """Test that generated sequence follows fibonacci property"""
    fibonacci = app.get_cell_value("fibonacci")
    sequence = fibonacci(10)

    # Test fibonacci property: each number is sum of previous two
    for i in range(2, len(sequence)):
        assert sequence[i] == sequence[i - 1] + sequence[i - 2]
