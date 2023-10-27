def add(block, nets, type_blocks):
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
                if type_blocks == "C":
                    output += ";"
                return output