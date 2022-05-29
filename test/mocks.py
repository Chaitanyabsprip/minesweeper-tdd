from random import Random
from typing import Any

from minesweeper.level import Level


class MockLevel(Level):
    def __init__(self, dimension, number_of_mines):
        super().__init__(dimension, number_of_mines)
        self.stub: Any

    def generate_position_of_mines(self, _=None):
        return self.stub

    def register_stub(self, stub):
        self.stub = stub


class MockRandomizer(Random):
    def __init__(self):
        super().__init__()
        self.seed_value = 0

    def randint(self, _, __):
        return 0

    def register_seed_value(self, seed_value):
        self.seed_value = seed_value
