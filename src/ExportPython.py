from Blocks import *


class ExportPython():
    """
    This class generates the Python file for the BSIM file
    """
    def __init__(self, file):
        self.file = file


    def generate_file(self, nets, blocks, scopes, constants, duration, Ts):
        """
        This method generates the Python file
        """
        self.generate_file_constants(constants)
        self.generate_main(duration, Ts)
        self.block_exe_file(nets, blocks, scopes)
        # self.functions_export()

        


    def generate_file_constants(self, constants_list):
        if constants_list:
            file_constants = open("constant_test.py", "w")
            output = "import numpy as np\n\n"
            cont = 0
            
            for constant_list in constants_list:
                output += "block" + str(cont) + " = np.array([" 
                cont2 = 0
                for constant in constant_list:
                    output += str(constant)
                    if cont2 < len(constant_list)-1:
                        output += " ,"
                    else:
                        output += "])\n"
                    cont2 += 1
                cont += 1

            file_constants.write(output)
            file_constants.close()



    def generate_main(self, duration, Ts):
        output = """import numpy as np
from example_func import *
import matplotlib.pyplot as plt

time_sim = """ + str(duration) + """
time = 0.0
Ts = """ + str(Ts) +  """
time = np.arange(0, time_sim, Ts)


scopes = []
init_func()

while time < time_sim: 
    #update signals
    update_signal()

    #execute with new values
    blocks_exe(time)

    #save the values in scopes
    scopes = scope()

    #update time index
    time += Ts
    

var = 0
for i in scopes:
    var += 1
    plt.plot(time, i, label = "scope"+str(var))

plt.legend()
plt.grid()
plt.show()"""
        file_main = open("main_test.py", "w")
        file_main.write(output)
        file_main.close()


    def block_exe_file(self, nets, blocks, scopes):
        file = open("controlloop_functions.py", "w")
        output = "from Blocks.Python_blocks.functions import *\nfrom constants import *\n\n"
        output += self.generate_init_func(nets, scopes) + "\n"
        output += self.generate_update_signal(nets) + "\n"
        output += self.generate_block_exe(nets, blocks) + "\n"
        output += self.generate_scope(nets)
        file.write(output)
        file.close()


    def generate_init_func(self, nets, scopes):
        """
        This method generates init_func function
        """
        output = "def init_func():\n"
        if nets:
            output += "\tglobal "
            cont = 0
            for net in nets:
                output += net[0] + "_ant"
                cont += 1
                if cont < len(nets):
                    output += ", "
            output += "\n"
            for net in nets:
                output += "\t" + net[0] + "_ant = 0\n"
        if scopes:
            output += "\tglobal "
            cont = 0
            for scope in scopes:
                output += "scope" + str(cont+1)
                cont += 1
                if cont < len(scopes):
                    output += ", "
            output += "\n"
            cont = 0
            for scope in scopes:
                output += "\t" + "scope" + str(cont+1) + " = []\n"
                cont += 1
        return output


    def generate_update_signal(self, nets):
        """
        This method generates the update signal function
        """
        output = "def update_signal():\n"
        if nets:
            output += "\tglobal "
            cont = 0
            for net in nets:
                output += net[0]
                cont += 1
                if cont < len(nets):
                    output += ", "
            output += "\n"
            for net in nets:
                output += "\t" + net[0] + " = " + net[0] + "_ant\n"
        return output


    def generate_block_exe(self, nets, blocks):
        """
        This method generates the block exe function
        """
        output = "def block_exe(time):\n"
        if nets:
            output += "\tglobal "
            cont = 0
            for net in nets:
                output += net[0] + "_ant"
                cont += 1
                if cont < len(nets):
                    output += ", "
            output += "\n"
        
        if blocks:
            for block in blocks:
                if block[1] == "step":
                    for net in nets:
                        if net[1] == block[0]:
                            output += net[1] + "_ant = " + block[1] + "(" + str(block[2]) + ", time, " + str(block[3]) + ")"
                            print()

        return output


    def generate_scope(self, nets):
        """
        This method generates the scope function
        """
        output = "def scope():\n"
        if nets:
            cont = 1
            for net in nets:
                output += "\tscope" + str(cont) + ".append(" + net[0] + "_ant)\n"
                cont += 1
        return output


    
