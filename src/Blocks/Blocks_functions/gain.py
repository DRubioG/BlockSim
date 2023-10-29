
def gain(block, nets, type_blocks):
    output = ""

    if type_blocks == "C":
        end = ";"
    else:
        end = ""

    for net in nets:
        if net[1] == block[0]:
            output += net[0] + "_ant = gain(" 
            break
    
    for net in nets:
        if type(net[2]) == list:
            for n in net[2]:
                if n == block[0]:
                    output += n + ", " + block[2] + ")"
                    return output + end
        else:
            if net[2] == block[0]:
                output += net[0] + ", " + block[2] + ")"
                return output + end
    return output