class Start:
    def __init__(self):
        self.display = 'X'

    def step(self, game):
        pass


class End:
    def __init__(self):
        self.display = 'Y'

    def step(self, game):
        pass


class Air:
    def __init__(self):
        self.display = ' '

    def step(self, game):
        pass


class Wall:
    def __init__(self):
        self.display = '*'

    def step(self, game):
        pass


class Fire:
    def __init__(self):
        self.display = 'F'

    def step(self, game):
        pass


class Water:
    def __init__(self):
        self.display = 'W'

    def step(self, game):
        pass


class Teleport:
    def __init__(self):
        self.display = 0  # You'll need to change this!

    def step(self, game):
        pass
