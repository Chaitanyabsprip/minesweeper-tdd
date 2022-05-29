# pylint: disable=no-self-use
import pytest

from minesweeper.cell import MINE, Cell, Position


class TestPosition:
    def test_should_raise_assertion_error_when_input_is_negative1_and_0(self):
        with pytest.raises(AssertionError):
            Position(-1, 0)

    def test_should_raise_assertion_error_when_input_is_0_and_negative1(self):
        with pytest.raises(AssertionError):
            Position(0, -1)

    def test_should_raise_assertion_error_when_input_is_0_and_negative2(self):
        with pytest.raises(AssertionError):
            Position(0, -2)

    def test_should_raise_assertion_error_when_input_is_negative2_and_0(self):
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


class TestCellIsAdjacentTo:
    def test_should_return_true_when_cell_is_1_tile_on_right(self):
        sut = Cell(MINE, Position(0, 0))
        adjacent_cell = Cell(MINE, Position(1, 0))

        assert sut.is_adjacent_to(adjacent_cell)

    def test_should_return_false_when_cell_is_2_tile_on_right(self):
        sut = Cell(MINE, Position(0, 0))
        adjacent_cell = Cell(MINE, Position(2, 0))

        assert not sut.is_adjacent_to(adjacent_cell)

    def test_should_return_true_when_cell_is_1_tile_on_left(self):
        sut = Cell(MINE, Position(1, 0))
        adjacent_cell = Cell(MINE, Position(0, 0))

        assert sut.is_adjacent_to(adjacent_cell)

    def test_should_return_false_when_cell_is_2_tile_on_left(self):
        sut = Cell(MINE, Position(2, 0))
        adjacent_cell = Cell(MINE, Position(0, 0))

        assert not sut.is_adjacent_to(adjacent_cell)

    def test_should_return_true_when_cell_is_1_tile_above(self):
        sut = Cell(MINE, Position(2, 0))
        adjacent_cell = Cell(MINE, Position(2, 1))

        assert sut.is_adjacent_to(adjacent_cell)

    def test_should_return_false_when_cell_is_2_tile_above_and_1_tile_on_left(
        self,
    ):
        sut = Cell(MINE, Position(3, 3))
        adjacent_cell = Cell(MINE, Position(2, 5))

        assert not sut.is_adjacent_to(adjacent_cell)

    def test_should_return_false_when_cell_is_1_tile_below_and_1_tile_on_left(
        self,
    ):
        sut = Cell(MINE, Position(3, 3))
        adjacent_cell = Cell(MINE, Position(2, 2))

        assert sut.is_adjacent_to(adjacent_cell)


def test_should_return_same_cell_with_is_explored_true():
    expected = Cell(0, Position(0, 0), True)
    sut = Cell(0, Position(0, 0))

    assert sut.mark_as_explored() == expected
