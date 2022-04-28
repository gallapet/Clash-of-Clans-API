class Hero:

    def __init__(self, name, level, maxLevel, village):
        self.name = name
        self.level = level
        self.maxLevel = maxLevel
        self.village = village

    def is_max(self):
        return self.level == self.maxLevel

    def print_max_message(self):
        if self.is_max():
            return ". Hero maxed!"
        else:
            return ""
