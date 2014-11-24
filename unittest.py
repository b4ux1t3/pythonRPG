from units import *
from unitcreator import *
from time import sleep

number = (2, 7)

level = (1, 10)

# Let's make some goblins!
goblins = spawnGoblins(number[0], number[1], level[0], level[1])

#This is just alist of the goblins in this particular field.
print "There are %s goblins" % (len(goblins))
print ""
print "Current goblins:"
for i in goblins:
    print i.name
    sleep(1)

print ""

# This is the first goblin!
gob1 = goblins[random.randrange(0, len(goblins))]

# This is the first goblin's particulars.
print "%s (Level %s) has joined the battle!" % (gob1.name, gob1.level)
sleep(1)
print "%s's equipment:" % (gob1.name)
for i in gob1.equipped:
    for j in gob1.equipped[i]:
        print j
        sleep(1)
        
print ""
sleep(1)

# This is the second goblin
gob2 = goblins[random.randrange(0, len(goblins))]

# Let's make sure that the goblins aren't the same!
while gob2 == gob1:
    
    gob2 = goblins[random.randrange(0, len(goblins))]
print ""

# And there we go! A second, unique goblin!
print "%s (Level %s) has joined the battle!" % (gob2.name, gob2.level)
sleep(1)
print "%s's equipment:" % (gob2.name)
for i in gob2.equipped:
    for j in gob2.equipped[i]:
        print j
        sleep(1)
        
print ""
sleep(1)

# Now let's just add some items to gob1's inventory.
gob1.inventory['pocket'].append('a bone club')
gob1.inventory['pocket'].append('a piece of lint')
gob1.inventory['pocket'].append('a book')

# Don't forget gob2! They need items too!
gob2.inventory['pocket'].append('a Raspberry Pi')
gob2.inventory['pocket'].append('a doll')
gob2.inventory['pocket'].append('a popsicle')

# And here they go! Pickpocketing each other!
gob2.pickpocket(gob1)

gob1.pickpocket(gob2)

print ""
sleep(1)
#Let's see what happened:
print "%s's inventory" % (gob1.name)
for i in gob1.inventory['pocket']:
    print i
sleep(1)
print ""    

print "%s's inventory" % (gob2.name)
for i in gob2.inventory['pocket']:
    print i
