# pylint: disable=no-self-use,C0301
from test.mocks import MockRandomizer

import pytest

from minesweeper.cell import Position
from minesweeper.dimension import Dimension
from minesweeper.level import Level


class TestGeneratePositionOfMines:
    def test_should_raise_assertion_error_when_number_of_mines_is_3_in_1x1_board(
        self,
    ):
        with pytest.raises(AssertionError):
            dimension = Dimension(1, 1)
            Level(dimension, number_of_mines=3)

    def test_shouldnt_raise_assertion_error_when_number_of_mines_is_1_in_1x1_board(
        self,
    ):
        dimension = Dimension(1, 1)
        Level(dimension, number_of_mines=1)

    def test_shouldnt_raise_assertion_error_when_number_of_mines_is_3_in_3x3_board(
        self,
    ):
        dimension = Dimension(3, 3)
        Level(dimension, number_of_mines=3)

    def test_shouldnt_raise_assertion_error_when_number_of_mines_is_3_in_2x3_board(
        self,
    ):
        dimension = Dimension(2, 3)
        Level(dimension, number_of_mines=3)

    def test_shouldnt_raise_assertion_error_when_number_of_mines_is_3_in_3x2_board(
        self,
    ):
        dimension = Dimension(3, 2)
        Level(dimension, number_of_mines=3)

    def test_shouldnt_raise_assertion_error_when_number_of_mines_is_6_in_3x2_board(
        self,
    ):
        dimension = Dimension(3, 2)
        Level(dimension, number_of_mines=6)

    def test_should_return_empty_array_when_input_is_0_in_1x1_board(self):
        dimension = Dimension(1, 1)
        sut = Level(dimension, number_of_mines=0)

        result = sut.generate_position_of_mines()

        assert result == set()

    def test_should_return_1_position_array_when_input_is_1_in_1x1_board(self):
        expected = {Position(0, 0)}
        dimension = Dimension(1, 1)

        sut = Level(dimension, number_of_mines=1)
        result = sut.generate_position_of_mines()

        assert result == expected

    def test_should_return_array_of_length_3_when_input_is_3_in_2x3_board(self):
        expected = 3
        dimension = Dimension(2, 3)

        sut = Level(dimension, number_of_mines=3)
        result = len(sut.generate_position_of_mines())

        assert result == expected

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_should_return_2_positions_when_input_is_1_in_2x1_board(self):
        dimension = Dimension(2, 1)
        randomizer = MockRandomizer()

        sut = Level(dimension, number_of_mines=2, _randomizer=randomizer)
        result = list(sut.generate_position_of_mines())

        assert result[0][0] < dimension.number_of_columns
        assert result[0][1] < dimension.number_of_rows


class TestGenerateEmptyLevel:
    def test_should_return_single_element_set_when_dimension_is_1x1(self):
        expected = {Position(0, 0)}

        sut = Level(Dimension(1, 1), 1)
        result = sut.generate_empty_level()

        assert result == expected

    def test_should_return_2_element_set_when_dimension_is_2x1(self):
        expected = {Position(0, 0), Position(1, 0)}

        sut = Level(Dimension(2, 1), 1)
        result = sut.generate_empty_level()

        assert result == expected

    def test_should_return_3_element_set_when_dimension_is_3x1(self):
        expected = {Position(0, 0), Position(1, 0), Position(2, 0)}

        sut = Level(Dimension(3, 1), 1)
        result = sut.generate_empty_level()

        assert result == expected

    def test_should_return_4_element_set_when_dimension_is_2x2(self):
        expected = {
            Position(0, 0),
            Position(1, 0),
            Position(0, 1),
            Position(1, 1),
        }

        sut = Level(Dimension(2, 2), 1)
        result = sut.generate_empty_level()

        assert result == expected

    def test_should_return_6_element_set_when_dimension_is_3x2(self):
        expected = {
            Position(0, 0),
            Position(1, 0),
            Position(2, 0),
            Position(0, 1),
            Position(1, 1),
            Position(2, 1),
        }

        sut = Level(Dimension(3, 2), 1)
        result = sut.generate_empty_level()

        assert result == expected
