import pytest

from minesweeper.dimension import Dimension


def test_should_raise_assertion_error_when_input_is_0_and_0():
    with pytest.raises(AssertionError):
        Dimension(0, 0)


def test_shouldnt_raise_assertion_error_when_input_is_1_and_1():
    Dimension(1, 1)


def test_shouldnt_raise_assertion_error_when_input_is_2_and_2():
    Dimension(2, 2)


def test_should_raise_assertion_error_when_input_is_1_and_0():
    with pytest.raises(AssertionError):
        Dimension(1, 0)


def test_should_raise_assertion_error_when_input_is_negative_1_and_1():
    with pytest.raises(AssertionError):
        Dimension(-1, 1)


def test_should_raise_assertion_error_when_input_is_1_and_negative_1():
    with pytest.raises(AssertionError):
        Dimension(1, -1)


def test_should_return_1_when_input_is_1_and_1():
    board = Dimension(1, 1)
    assert board.get_number_of_cells() == 1


def test_should_return_2_when_input_is_1_and_2():
    board = Dimension(1, 2)
    assert board.get_number_of_cells() == 2


def test_should_return_4_when_input_is_2_and_2():
    board = Dimension(2, 2)
    assert board.get_number_of_cells() == 4
