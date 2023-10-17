from Blocks import *

class ExportC():
    def __init__(self, file):
        self.file = file


    def generate_file(self, nets, blocks, constants, Ts):
        self.generate_file_constants(constants)
        self.generate_main(Ts)
        self.block_exe_file(nets, blocks, constants)

    
    def generate_file_constants(self, constants_list):
        if constants_list:
            file_constants = open("constant_test.h", "w")
            output = ""
            cont = 0
            
            for constant_list in constants_list:
                output += "float block" + str(cont) + "["+ str(len(constant_list))+"] = {" 
                cont2 = 0
                for constant in constant_list:
                    output += str(constant)
                    if cont2 < len(constant_list)-1:
                        output += ", "
                    else:
                        output += "};\n"
                    cont2 += 1
                cont += 1

            file_constants.write(output)
            file_constants.close()


    def generate_main(self, Ts):
        output = """#include <stdio.h>
#include "example_func.c"

int main(){
    float time_counter = 0.0;
    float time_incr = """ + str(Ts) + """;

    while(true){
        net_update();

        block_exe();

        /* This part is only for an execution with blocks that requires time
        WARNING: variable overflow */
        /*block_exe(time_counter);
        time_counter += time_incr;*/
    }

    return 0;
}
"""

        file_main = open("main_test.c", "w")
        file_main.write(output)
        file_main.close()
    
    

    def block_exe_file(self, nets, blocks, constants):
        file = open("controlloop_functions.c", "w")
        output = "#include \"../Blocks/C_blocks/functions.c\""
        output += "\n#include \"constants.h\"\n\n"

        output += self.generate_init_func(nets, constants)
        output += self.generate_update_signal(nets)
        output += self.generate_block_exe(nets, blocks)
        file.write(output)
        file.close()



    def generate_init_func(self, nets, constants):
        output = ""
        if nets:
            output += "\n"
            for net in nets:
                output += "float " + net[0] + "_ant = 0;\n"
            output += "\n"
            for net in nets:
                output += "float " + net[0] + " = 0;\n"

        if constants:
            output += "\n"
            cont = 0
            for constant in constants:
                output += "float input" + str(cont) + "["+ str(len(constant)) +"];\n"
                cont += 1
        
        return output
    

    def generate_update_signal(self, nets):
        output = "\nvoid net_update(){\n"
        if nets:
            for net in nets:
                output += "\t" + net[0] + " = " + net[0] + "_ant;\n"
        output += "}"
        return output
    
    def generate_block_exe(self, nets, blocks):
        output = "\n\nvoid block_exe(){"
        if blocks:
            bck = Blocks("C")
            for block in blocks:
                output += "\n\t" + bck.writeBlocks(block, nets) 

        output += "\n}"

        return output