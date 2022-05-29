from dataclasses import dataclass
from random import Random

from minesweeper.cell import Position
from minesweeper.dimension import Dimension


@dataclass(frozen=True)
class Level:
    dimension: Dimension
    number_of_mines: int
    _randomizer: Random = Random()

    def __post_init__(self):
        assert self.number_of_mines <= self.dimension.get_number_of_cells() / 2

    def generate_empty_level(self):
        empty_level = set()
        for x_pos in range(self.dimension.number_of_columns):
            for y_pos in range(self.dimension.number_of_rows):
                empty_level.add(Position(x_pos, y_pos))
        return empty_level

    def generate_position_of_mines(self, position_array=None):
        position_array = position_array or set([])
        if len(position_array) == self.number_of_mines:
            return position_array
        random_number = self._randomizer.randint(0, 100)
        x_offset = random_number % self.dimension.number_of_columns
        y_offset = random_number % self.dimension.number_of_rows
        position_array.add(Position(x_offset, y_offset))
        return self.generate_position_of_mines(position_array)
