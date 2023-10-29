from Blocks.Blocks_functions.step import *
from Blocks.Blocks_functions.add import *
from Blocks.Blocks_functions.convolution import *
from Blocks.Blocks_functions.gain import *


class Blocks():
    def __init__(self, type_blocks = "Python"):
        self.cont = 0
        self.type_blocks = type_blocks


    def readBlocks(self):
        pass



    def writeBlocks(self, block, nets, constants):
        output = ""

# STEP: this conditional creates the step function
        if block[1] == "step":
            output += step(block, nets, self.type_blocks)

# ADD: this conditional creates the sum function
        elif block[1] == "add":
            #search first input
            output += add(block, nets, self.type_blocks)

# TFS: this conditional creates the tfs function
        elif block[1] == "tfs":
            output += conv(block, nets, self.cont, constants, self.type_blocks)
            self.cont += 1

# GAIN: this conditional creates the gain function
        elif block[1] == "gain":
            output += gain(block, nets, self.type_blocks)
    
        return output
    
    

    
      