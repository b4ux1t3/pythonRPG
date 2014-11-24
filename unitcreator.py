from units import *
import random

""" 
Copyright (c) 2014 Chris Pilcher

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files 
(the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, 
publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY 
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module will spawn units. It's pretty self explanatory.

Each level will call these functions based on its own parameters.

For example:
    Certain levels will spawn multiple goblins and place them around the map.
    
    Others might create a certain ratio of goblins to wolves and set them battling each other.
    
All spawn functions will take at least four arguments, minNum, maxNum, minLevel, and maxLevel, which are integers representing 
the minimum and maximum two ranges.

For example:
    spawnGoblins((2, 5), (4, 5)) would make anywhere from 2-to-5 goblins with levels of either 4 or 5.

Current races:
    Goblins - incomplete
    Trolls - missing
    Orcs - incomplete
    Wolves - incomplete
    Fairies - missing

TODO:
    - Add more unit types.
    - Create name lists.
    - Actually finish making Unit creators

"""

def spawnGoblins(minNum, maxNum, minLevel, maxLevel):
    f = open("names.txt", "r")
    names = []
    for i in f:
        names.append(i[:-1])
    f.close()
    # DEBUG: Prints names
    for i in names:
        print i
    
    # Stores the goblins,is returned to level creator.
    goblins = []
    for i in range(minNum, maxNum):
        # Name will be randomized, for now just imported from names.txt
        name = random.choice(names)
        health = random.gauss(80, 120)
        attack = random.gauss(5, 15)
        defense = random.gauss(5, 15)
        speed = 3
        gold = random.gauss(20, 60)
        level = random.randrange(minLevel, maxLevel)
        xp = 123
        gob = Goblin(name, health, attack, defense, speed, gold, level, xp)
        goblins.append(gob)
    
    return goblins
    
