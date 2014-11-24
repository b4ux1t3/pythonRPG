from units import *
from unitcreator import *
from time import sleep

number = (2, 7)

level = (1, 10)

goblins = spawnGoblins(number[0], number[1], level[0], level[1])


print "There are %s goblins" % (len(goblins))

print "Current goblins:"
for i in goblins:
    print i.name
    sleep(1)
    
gob1 = goblins[random.randrange(0, len(goblins))]

print "%s has joined the battle!" % (gob1.name)
sleep(1)
print "%s's equipment:" % (gob1.name)
for i in gob1.equipped:
    for j in gob1.equipped[i]:
        print j
        sleep(1)
sleep(1)

gob2 = goblins[random.randrange(0, len(goblins))]
    
while gob2 == gob1:
    
    gob2 = goblins[random.randrange(0, len(goblins))]
    
print "%s has joined the battle!" % (gob2.name)
sleep(1)
print "%s's equipment:" % (gob2.name)
for i in gob2.equipped:
    for j in gob2.equipped[i]:
        print j
        sleep(1)
sleep(1)
    
gob1.inventory['pocket'].append('a bone club')

gob2.pickpocket(gob1)
