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

The player object and all its uniqueness (i.e. none) reside here.

This game is designed to have as little difference between how units behave as possible. As such, every unit in the game, from the player to the goblin king, has the same basic structure. The only difference in the player's case is that it is controllable. The player has no uniqe attacks or abilities, and can even be any of the races in the game.

For now, though, the player is limited to goblin.

TODO:
    - Implement player race selection
""" 

from units import *

class Player(Unit):
    def __init__(self, name, race, health, attack, defense, speed, gold, level, xp):
        
        super(Player, self).__init__(name, health, attack, defense, speed, gold, level, xp)
        
        if race == "goblin":
            self.inventory = {'pocket'}
            self.equipped['boots']='worn boots'
            
    
        
