class NonPlayerCharacter():
    classField = "npc klases laukas"
    def __init__(self, name):
        self.name = name

    def make_a_sound(self):
        print(f"beep pop poop! {self.name}")