

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
            for net in nets:
                if net[1] == block[0]:
                    output += net[0] + "_ant = " + block[1] + "(" + str(block[2]) + ", time, " + str(block[3]) + ")"
                    return output
                

# SUM: this conditional creates the sum function
        elif block[1] == "sum":
            #search first input
            for net in nets:
                if type(net[2]) == list:
                    for n in net[2]:
                        if n == block[0]+"[0]":
                            output += "sum(" + net[0] + ", "
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
                            output += net[0] + ") "
                            stop2 = 1
                            break
                        
                else:
                    if net[2] == block[0]+"[1]":
                        output += net[0] + ") "
                        break


            #search output
            for net in nets:
                if net[1] == block[0]+"[2]":
                    output = net[0] + "_ant = " + output 
                    return output


# TFS: this conditional creates the tfs function
        elif block[1] == "tfs":
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
    
        return output