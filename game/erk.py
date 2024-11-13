from game.elf import Elf
from game.non_player_character import NonPlayerCharacter
from game.ork import Ork


class Erk(Elf, Ork):
    def __init__(self, name, a, b, c,clf):
        self.name = name
        self.a = a
        self.b = b
        self.c = c
        self.classField = clf

    # def make_a_sound(self):
    #     print("we.. dont really want to hear that")
    def make_a_sound(self):
        return NonPlayerCharacter.make_a_sound(self)
    # def weirdMath(self):
    #     return Ork.weirdMath(self) - self.c
    def weirdMath(self):
        return self.a - self.b - self.c