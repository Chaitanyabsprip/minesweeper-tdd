# pylint: disable=no-self-use

from test.mocks import MockLevel

from minesweeper.cell import MINE, Cell, Position
from minesweeper.dimension import Dimension
from minesweeper.level import Level
from minesweeper.minesweeper import Board


class TestGenerateGameBoard:
    def test_should_return_1_cell_array_when_input_is_0_with_1x1_board(self):
        expected = {Cell(0, Position(0, 0))}
        board = Dimension(1, 1)
        level = Level(board, number_of_mines=0)

        sut = Board()
        sut.generate_board_with_level(level)

        assert sut.board == expected

    def test_should_return_1_cell_array_when_input_is_1_with_1x1_board(self):
        pos = Position(0, 0)
        expected = {Cell(MINE, pos)}
        board = Dimension(1, 1)
        level = Level(board, number_of_mines=1)

        sut = Board()
        sut.generate_board_with_level(level)

        assert sut.board == expected

    def test_should_return_2_cell_array_when_input_is_2_with_2x1_board(self):
        expected = {Cell(MINE, Position(0, 0)), Cell(MINE, Position(1, 0))}
        board = Dimension(2, 1)
        level = Level(board, number_of_mines=2)

        sut = Board()
        sut.generate_board_with_level(level)

        assert sut.board == expected

    def test_should_return_2_cell_array_when_input_is_1_with_1x2_board(self):
        expected = {Cell(MINE, Position(0, 0)), Cell(1, Position(0, 1))}
        dimension = Dimension(1, 2)
        level = MockLevel(dimension, number_of_mines=1)
        level.register_stub([Position(0, 0)])

        sut = Board()
        sut.generate_board_with_level(level)

        assert sut.board == expected

    def test_should_return_6_cell_array_when_input_is_1_with_3x2_board(self):
        expected = {
            Cell(1, Position(0, 0)),
            Cell(MINE, Position(1, 0)),
            Cell(1, Position(2, 0)),
            Cell(1, Position(0, 1)),
            Cell(1, Position(1, 1)),
            Cell(1, Position(2, 1)),
        }
        dimension = Dimension(3, 2)
        level = MockLevel(dimension, number_of_mines=1)
        level.register_stub([Position(1, 0)])

        sut = Board()
        sut.generate_board_with_level(level)

        assert sut.board == expected
