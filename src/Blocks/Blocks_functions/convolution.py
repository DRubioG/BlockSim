    
def conv(block, nets, cont, constants, type_blocks):
    output = ""
    if type_blocks == "Python":
        for net in nets:
            if net[1] == block[0]:
                output += net[0] + "_ant, input" + str(cont) + " = conv(" 
                break
                
        
        for net in nets:
            if type(net[2]) == list:
                for n in net[2]:
                    if n == block[0]:
                        output += net[0] + ", block" + str(cont) + ", input" + str(cont) + ")"
                        cont += 1
                        return output
            else:
                if net[2] == block[0]:
                    output += net[0] + ", block" + str(cont) + ", input" + str(cont) + ")"
                    cont += 1
                    return output
                
    elif type_blocks == "C":
        for net in nets:
            if net[1] == block[0]:
                output += net[0] + "_ant = convolution(" 
                break
        
        for net in nets:
            if type(net[2]) == list:
                for n in net[2]:
                    if n == block[0]:
                        output += net[0] + ", block" + str(cont) + ", input" + str(cont) + ", " + str(len(constants[cont])) + ");"
                        cont += 1
                        return output
            else:
                if net[2] == block[0]:
                    output += net[0] + ", block" + str(cont) + ", input" + str(cont) + ", " + str(len(constants[cont])) + ");"
                    cont += 1
                    return output