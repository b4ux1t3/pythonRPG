from unitcreator import *
from units import *
from player import *
#name, health, attack, defense, speed, gold, level, xp
bob = Goblin('Bob', 100, 10, 2, 1, 100, 1, 0)
bill = Goblin('Bill', 100, 10, 2, 1, 100, 1, 0)

bill.inventory['pocket'].append('hankerchief')
bill.inventory['pocket'].append('idol')
bill.inventory['pocket'].append('lint')

for i in bill.inventory:
    for j in bill.inventory[i]:
        print j

bob.pickpocket(bill)

print bill.inventory

