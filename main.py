from buhalterija import Buhalterija
from game.elf import Elf
from game.erk import Erk
from game.non_player_character import NonPlayerCharacter
from game.ork import Ork

npc = NonPlayerCharacter("tevinis salbonas")
elf = Elf("Le less legless lego legolass")
ork = Ork("nepamenu", 5, 10)
erk = Erk("zbigniavas",5,10, 8,"tai jau nera tie classfieldai kur matem, tai yra erko propertis")

# npc.make_a_sound()
#
# elf.make_a_sound()

#--------------------
# ork.make_a_sound()    # daro ta pati
# Ork.make_a_sound(ork) #
#--------------------

erk.make_a_sound()

buhalterija = Buhalterija()

# NonPlayerCharacter.make_a_sound(buhalterija) meta errora, nes buhalterija neturi vardo

print(npc.classField)
print(erk.classField)

print(ork.weirdMath())
print(erk.weirdMath())
