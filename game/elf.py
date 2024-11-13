from game.non_player_character import NonPlayerCharacter


class Elf(NonPlayerCharacter):
    classField = "Elf klases laukas"
    def __init__(self, name):
        self.name = name
        pass

    def make_a_sound(self):
        print("hssss!")