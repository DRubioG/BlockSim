
def step(block, nets, type_blocks):
        output = ""
        for net in nets:
            if net[1] == block[0]:
                if type_blocks == "Python":
                    output += net[0] + "_ant = " + block[1] + "(" + str(block[2]) + ", time, " + str(block[3]) + ")"
                elif type_blocks == "C":
                    output += net[0] + "_ant = " + block[1] + "(" + str(block[2]) + ", time, " + str(block[3]) + ");"
                return output