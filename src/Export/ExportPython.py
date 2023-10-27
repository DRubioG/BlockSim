import shutil, os
from Blocks.Blocks import *


class ExportPython():
    """
    This class generates the Python file for the BSIM file
    """
    def __init__(self, file):
        self.file = file
        self.path_list = os.path.split(file)
        self.name = os.path.splitext(self.path_list[1])[0]
        self.path = self.path_list[0]
        self.generate_dir()


    def generate_dir(self):
        os.makedirs(os.path.join(self.path, self.name), exist_ok=True)
        self.path = os.path.join(self.path, self.name)


    def generate_file(self, nets, blocks, scopes, constants, duration, Ts):
        """
        This method generates the Python file
        """
        self.generate_file_constants(constants)
        self.generate_main(duration, Ts)
        self.block_exe_file(nets, blocks, scopes, constants)
        self.copy_func()

        


    def generate_file_constants(self, constants_list):
        if constants_list:
            file_constants = open(os.path.join(self.path, self.name+"_constants.py"), "w")
            output = "import numpy as np\n\n"
            cont = 0
            
            for constant_list in constants_list:
                output += "block" + str(cont) + " = np.array([" 
                cont2 = 0
                for constant in constant_list:
                    output += str(constant)
                    if cont2 < len(constant_list)-1:
                        output += ", "
                    else:
                        output += "])\n"
                    cont2 += 1
                cont += 1

            file_constants.write(output)
            file_constants.close()



    def generate_main(self, duration, Ts):
        output = """import numpy as np
from """ + self.name + """_functions import *
import matplotlib.pyplot as plt

time_sim = """ + str(duration) + """
time = 0.0
Ts = """ + str(Ts) +  """
time_axis = np.arange(0, time_sim, Ts)


scopes = []
init_func()

while time < time_sim: 
    #update signals
    update_signal()

    #execute with new values
    block_exe(time)

    #save the values in scopes
    scopes = scope()

    #update time index
    time += Ts
    

var = 0
for i in scopes:
    var += 1
    plt.plot(time_axis, i[:-1], label = "scope"+str(var))

plt.legend()
plt.grid()
plt.show()"""

        file_main = open(os.path.join(self.path, self.name+"_main.py"), "w")
        file_main.write(output)
        file_main.close()


    def block_exe_file(self, nets, blocks, scopes, constants):
        """
        This method creates the Python file
        """
        file = open(os.path.join(self.path, self.name+"_functions.py"), "w")
        output = "from functions import *\nfrom " + self.name + "_constants import *\n\n"
        output += self.generate_init_func(nets, scopes, blocks) + "\n"
        output += self.generate_update_signal(nets) + "\n"
        output += self.generate_block_exe(nets, blocks, constants) + "\n"
        output += self.generate_scope(nets)
        file.write(output)
        file.close()


    def generate_init_func(self, nets, scopes, blocks):
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
        if blocks:
            glob = "\tglobal "
            out = ""
            cont = 0
            flag = 0
            for block in blocks:
                if block[1] == "tfs":
                    if flag == 0:
                        glob += "input" + str(cont)
                        flag = 1
                    else:
                        glob += ", input" + str(cont)
                    out += "\n\tinput"+ str(cont) + " = np.zeros(len(block" + str(cont) + "))"
                    cont += 1
            output += glob + out + "\n"
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


    def generate_block_exe(self, nets, blocks, constants):
        """
        This method generates the block exe function
        """
        output = "def block_exe(time):\n"
        if blocks:
            glob = "\tglobal "
            cont = 0
            flag = 0
            for block in blocks:
                if block[1] == "tfs":
                    if flag == 0:
                        glob += "input" + str(cont)
                        flag = 1
                    else:
                        glob += ", input" + str(cont)
                    cont += 1
            output += glob + "\n"
        if nets:
            output += "\tglobal "
            cont = 0
            for net in nets:
                output += net[0] + "_ant"
                cont += 1
                if cont < len(nets):
                    output += ", "
            output += "\n\t"
        
        if blocks:
            bck = Blocks()
            for block in blocks:
                output += bck.writeBlocks(block, nets, constants) + "\n\t"

        return output


    def generate_scope(self, nets):
        """
        This method generates the scope function
        """
        output = "def scope():\n"
        ret = ""
        if nets:
            cont = 1
            flag = 0
            for net in nets:
                output += "\tscope" + str(cont) + ".append(" + net[0] + "_ant)\n"
                if flag == 0:
                    ret += "\treturn "
                    flag = 1
                else: 
                    ret += ", "
                ret += "scope" + str(cont)
                cont += 1
            
            output += ret
        return output


    def copy_func(self):
        shutil.copy("./Blocks/Python_functions/functions.py", self.path)