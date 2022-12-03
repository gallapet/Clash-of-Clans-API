class Hero:

    def __init__(self, name, level, max_level):
        self.name = name
        self.level = level
        self.max_level = max_level

    def is_max(self):
        return self.level == self.max_level

    def print_max_message(self):
        if self.is_max():
            return ". Hero maxed!"
        return ""
