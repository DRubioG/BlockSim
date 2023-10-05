

class ExportPython():
    def __init__(self, file):
        self.file = file


    
    def generate_init_func(self, nets):
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
        return output


    def generate_scope(self, nets):
        output = "def scope():\n"
        if nets:
            cont = 1
            for net in nets:
                output += "\tscope" + str(cont) + ".append(" + net[0] + "_ant)\n"
                cont += 1
        return output


    def generate_file(self, nets):
        file = open("controlloop_functions.py", "w")
        output = "from Blocks.Python_blocks.functions import *\nfrom constants import *\n\n"
        output += generate_init_func(nets) + "\n"
        output += generate_update_signal(nets) + "\n"
        output += generate_block_exe(nets, blocks) + "\n"
        output += generate_scope(nets)
        file.write(output)
        file.close()
