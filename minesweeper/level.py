from dataclasses import dataclass
from random import Random

from minesweeper.board import Board
from minesweeper.cell import Position


@dataclass(frozen=True)
class Level:
    board: Board
    number_of_mines: int
    _randomizer: Random = Random()

    def __post_init__(self):
        assert self.number_of_mines <= self.board.get_number_of_cells()

    def generate_position_of_mines(self):
        position_array = []
        for _ in range(self.number_of_mines):
            x_position = self._randomizer.randint(
                0, self.board.number_of_columns - 1
            )
            y_position = self._randomizer.randint(
                0, self.board.number_of_rows - 1
            )
            position_array += [Position(x_position, y_position)]
        return position_array
