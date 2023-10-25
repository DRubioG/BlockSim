

class Blocks():
    def __init__(self, type_blocks = "Python"):
        self.cont = 0
        self.type_blocks = type_blocks


    def readBlocks(self):
        pass



    def writeBlocks(self, block, nets):
        output = ""

# STEP: this conditional creates the step function
        if block[1] == "step":
            output += self.step(block, nets)

# ADD: this conditional creates the sum function
        elif block[1] == "add":
            #search first input
            output += self.add(block, nets)

# TFS: this conditional creates the tfs function
        elif block[1] == "tfs":
            output += self.conv(block, nets)
    
        return output
    

    def step(self, block, nets):
        output = ""
        for net in nets:
            if net[1] == block[0]:
                if self.type_blocks == "Python":
                    output += net[0] + "_ant = " + block[1] + "(" + str(block[2]) + ", time, " + str(block[3]) + ")"
                elif self.type_blocks == "C":
                    output += net[0] + "_ant = " + block[1] + "(" + str(block[2]) + ", time, " + str(block[3]) + ");"
                return output
    

    def add(self, block, nets):
        output = ""
        for net in nets:
            if type(net[2]) == list:
                for n in net[2]:
                    if n == block[0]+"[0]":
                        output += "add(" + net[0] + ", "
                        break
            else:
                if net[2] == block[0]+"[0]":
                    output += "add(" + net[0] + ", "
                    break


        #search second input
        stop2 = 0
        for net in nets:
            if stop2 == 1: break
            if type(net[2]) == list:
                for n in net[2]:
                    if n == block[0]+"[1]":
                        output += net[0] + ")"
                        stop2 = 1
                        break
                    
            else:
                if net[2] == block[0]+"[1]":
                    output += net[0] + ")"
                    break


        #search output
        for net in nets:
            if net[1] == block[0]+"[2]":
                output = net[0] + "_ant = " + output 
                if self.type_blocks == "C":
                    output += ";"
                return output
            
    def conv(self, block, nets):
        output = ""
        if self.type_blocks == "Python":
            for net in nets:
                if net[1] == block[0]:
                    output += net[0] + "_ant, input" + str(self.cont) + " = conv(" 
                    break
                    
            
            for net in nets:
                if type(net[2]) == list:
                    for n in net[2]:
                        if n == block[0]:
                            output += net[0] + ", block" + str(self.cont) + ", input" + str(self.cont) + ")"
                            self.cont += 1
                            return output
                else:
                    if net[2] == block[0]:
                        output += net[0] + ", block" + str(self.cont) + ", input" + str(self.cont) + ")"
                        self.cont += 1
                        return output
                    
        elif self.type_blocks == "C":
            for net in nets:
                if net[1] == block[0]:
                    output += net[0] + "_ant = convolution(" 
                    break
            
            for net in nets:
                if type(net[2]) == list:
                    for n in net[2]:
                        if n == block[0]:
                            output += net[0] + ", block" + str(self.cont) + ", input" + str(self.cont) + ");"
                            self.cont += 1
                            return output
                else:
                    if net[2] == block[0]:
                        output += net[0] + ", block" + str(self.cont) + ", input" + str(self.cont) + ");"
                        self.cont += 1
                        return output