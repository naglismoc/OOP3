from game.non_player_character import NonPlayerCharacter


class Ork(NonPlayerCharacter):
    def __init__(self, name,a,b):
        self.name = name
        self.a = a
        self.b = b

    def make_a_sound(self):
        print("grraargh!")

    def weirdMath(self):
        return self.a + self.b