from random import Random


class MockRandomizer(Random):
    def __init__(self):
        super().__init__()
        self.seed_value = 0

    def randint(self):
        return 0

    def register_seed_value(self, seed_value):
        self.seed_value = seed_value
