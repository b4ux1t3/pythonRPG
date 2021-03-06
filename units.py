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

This module defines all the basic non-player units in the game. These are referred to as races. If it isn't here, it isn't implemented.

The Player is also a Unit object, but is separated for readability's sake. This means that every unit in the game, from the player to the Goblin King, has the same basic structure. Every unit in the game has it's own inventory, its own XP level, its own everything.

Current races:
    Goblins - incomplete
    Trolls - missing
    Orcs - incomplete
    Wolves - Possibly removed. Monster units may be different.
    Fairies - missing
        
Races who have unique abilities will have them implemented in their class definitions instead of in the Attacks or Abilities modules.

There is a second module for more complex units, essentially different "classes" using the same basic races.
"""
import random
from time import sleep

#TODO: Implement missing/incomplete races

# Defines a basic unit.
class Unit(object):
    
    # Initialize all attributes
    def __init__(self, name, health, attack, defense, speed, gold, level, xp):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.inventory = {'backpack': [], 
                          'pocket'  : [], 
                          'boot'    : []}
        self.equipped = {'head':[],
                         'neck':[],
                         'shoulders':[],
                         'chest':[],
                         'wrist':[],
                         'legs':['pants'],
                         'boots':[],
                         'ring0':[],
                         'ring1':[],
                         'ring2':[],
                         'ring3':[],
                         'ring4':[],
                         'ring5':[],
                         'ring6':[],
                         'ring7':[],
                         'ring8':[],
                         'ring9':[]}
        self.gold = gold
        self.level = level
        self.xp = xp
        # Contains ability objects
        self.abilities = []
    
    # Important to every RPG   
    def levelUp(self):
        print "You leveled up!"
        self.level += 1
        h = self.health
        a = self.attack
        d = self.defense
        self.health += random.randrange(1, 4)
        self.attack += random.randrange(1, 4)
        self.defense += random.randrange(1, 4)
        print "You are now level %s!" % (self.level)
        print "Health increased by " + str(self.health - h) + " %s -> %s" % (h, self.health)
        print "Attack increased by " + str(self.attack - a) + " %s -> %s" % (a, self.attack)
        

    # Attacks a target, calls target's "defend" method
    def attack(self, target):
        pass
        
    # Defends against an attack, passed attacking unit as a parameter
    def defend(self, attacker):
        pass
    
    # Moves across map using speed stat
    def move(self):
        pass
        
    # Adds an item to the unit's inventory
    def pickup(self, item):
        self.inventory['pocket'].append(item)
        
    # Removes an item from inventory
    def remove(self, storage, item):
        del self.inventory[storage][item]

# Goblins are quick, stupid, and greedy. Low attack, high speed, extra gold, increased chance of spawning with items.
# Goblins start with only pockets, will be able to pick up other methods of carrying items.
# TODO: Implement storage. 
class Goblin(Unit):
    
    def __init__(self, name, health, attack, defense, speed, gold, level, xp):
        super(Goblin, self).__init__(name, health, attack, defense, speed, gold, level, xp)
        self.inventory = {'pocket': []}
        
    # This is a goblin-specific ability. It can steal items ONLY from a target's pocket.
    def pickpocket(self, target):
        print "%s tries to pick %s's pocket!" % (self.name, target.name)
        sleep(1)
        targetPocket = target.inventory['pocket']
        ppTarget = random.randrange(0, len(targetPocket))
        self.pickup(targetPocket[ppTarget])
        print "%s stole %s from %s!" % (self.name, targetPocket[ppTarget], target.name)
        sleep(1)
        target.remove('pocket', ppTarget)
        
        self.xp += 1
        
class Orc(Unit):
    pass
    
class Faerie(Unit):
    pass
    
class Troll(Unit):
    pass
