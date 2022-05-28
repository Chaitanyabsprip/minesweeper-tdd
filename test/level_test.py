from test.mocks import MockRandomizer

import pytest

from minesweeper.board import Board
from minesweeper.cell import Position
from minesweeper.level import Level


def test_should_raise_assertion_error_when_number_of_mines_is_3_in_1x1_board():
    with pytest.raises(AssertionError):
        board = Board(1, 1)
        Level(board, number_of_mines=3)


def test_shouldnt_raise_assertion_error_when_number_of_mines_is_1_in_1x1_board():
    board = Board(1, 1)
    Level(board, number_of_mines=1)


def test_shouldnt_raise_assertion_error_when_number_of_mines_is_3_in_3x3_board():
    board = Board(3, 3)
    Level(board, number_of_mines=3)


def test_shouldnt_raise_assertion_error_when_number_of_mines_is_3_in_2x3_board():
    board = Board(2, 3)
    Level(board, number_of_mines=3)


def test_shouldnt_raise_assertion_error_when_number_of_mines_is_3_in_3x2_board():
    board = Board(3, 2)
    Level(board, number_of_mines=3)


def test_shouldnt_raise_assertion_error_when_number_of_mines_is_6_in_3x2_board():
    board = Board(3, 2)
    Level(board, number_of_mines=6)


def test_should_return_empty_array_when_input_is_0_in_1x1_board():
    board = Board(1, 1)
    sut = Level(board, number_of_mines=0)

    result = sut.generate_position_of_mines()

    expected = []
    assert result == expected


def test_should_return_1_position_array_when_input_is_1_in_1x1_board():
    expected = [Position(0, 0)]
    board = Board(1, 1)

    sut = Level(board, number_of_mines=1)
    result = sut.generate_position_of_mines()

    assert result == expected


def test_should_return_array_of_length_3_when_input_is_3_in_2x3_board():
    expected = 3
    board = Board(2, 3)

    sut = Level(board, number_of_mines=3)
    result = len(sut.generate_position_of_mines())

    assert result == expected


@pytest.mark.skip(reason="no way of currently testing this")
def test_should_return_2_positions_when_input_is_1_in_2x1_board():
    board = Board(2, 1)
    randomizer = MockRandomizer()

    sut = Level(board, number_of_mines=2, _randomizer=randomizer)
    result = sut.generate_position_of_mines()

    assert result[0][0] < board.number_of_columns
    assert result[0][1] < board.number_of_rows
