import pytest

from minesweeper.cell import Cell, Position


def test_should_raise_assertion_error_when_input_is_negative1_and_0():
    with pytest.raises(AssertionError):
        Position(-1, 0)


def test_should_raise_assertion_error_when_input_is_0_and_negative1():
    with pytest.raises(AssertionError):
        Position(0, -1)


def test_should_raise_assertion_error_when_input_is_0_and_negative2():
    with pytest.raises(AssertionError):
        Position(0, -2)


def test_should_raise_assertion_error_when_input_is_negative2_and_0():
    with pytest.raises(AssertionError):
        Position(-2, 0)


class TestCell:
    origin = Position(0, 0)

    def test_should_raise_assertion_error_when_input_is_negative_2(self):
        with pytest.raises(AssertionError):
            Cell(-2, self.origin)

    def test_should_raise_assertion_error_when_input_is_10(self):
        with pytest.raises(AssertionError):
            Cell(10, self.origin)

    def test_shouldnt_raise_assertion_error_when_input_is_3(self):
        Cell(3, self.origin)

    def test_shouldnt_raise_assertion_error_when_input_is_4(self):
        Cell(4, self.origin)

    def test_should_raise_assertion_error_when_input_is_negative_14(self):
        with pytest.raises(AssertionError):
            Cell(-14, self.origin)

    def test_should_raise_assertion_error_when_input_is_14(self):
        with pytest.raises(AssertionError):
            Cell(14, self.origin)
