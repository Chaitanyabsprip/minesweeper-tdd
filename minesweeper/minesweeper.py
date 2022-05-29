from minesweeper.cell import MINE, Cell
from minesweeper.level import Level


class Board:
    def __init__(self):
        self.board = set()

    def generate_board_with_level(self, level: Level):
        mine_positions = level.generate_position_of_mines()
        positions = level.generate_empty_level()
        for pos in positions:
            value = 0
            if pos in mine_positions:
                value = MINE
            else:
                value = [
                    Cell(0, pos).is_adjacent_to(Cell(MINE, x))
                    for x in mine_positions
                ].count(True)
            self.board.add(Cell(value, pos))
