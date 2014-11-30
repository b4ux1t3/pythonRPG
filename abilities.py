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

"""
import random
#from datetime import *

# This class holds all the "universal" abilities.
# Each ability has a unique identifer (ID)
# Todo:
    # Add error handling and logging
    
class Ability(object):
    def __init__(self, ID):
        self.ID = ID
        self.cost = 0
        
    
    
    # Sneak a peak in an opponent's inventory.
    # peek's ID is 1
    def peek(self, target):
        # Makes sure the ability using this method is "peek".
        if self.ID == 1:
            peek = []
            slot = random.randrange(0, len(target.inventory))
            peek.append(slot)
            print peek
        else:
            print "Error: Illegal ability call."
            return "Error"

