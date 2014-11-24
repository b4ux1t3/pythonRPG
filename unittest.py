from units import *
from unitcreator import *

number = (2, 7)

level = (1, 10)

goblins = spawnGoblins(number[0], number[1], level[0], level[1])


print "There are %s goblins" % (len(goblins))

for i in goblins:
    print i.name
