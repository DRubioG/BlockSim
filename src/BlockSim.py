from ReadBlockSim import *
from ExportPython import *


class BlockSim():
    def __init__(self, file):
        self.file = file
        self.generate()



    def generate(self):
        read_file = ReadBlockSim(self.file)

        self.generate_file()



    def generate_file(self, nets):
        file = open("controlloop_functions.py", "w")
        output = "from Blocks.Python_blocks.functions import *\nfrom constants import *\n\n"
        output += generate_init_func(nets) + "\n"
        output += generate_update_signal(nets) + "\n"
        output += generate_block_exe(nets, blocks) + "\n"
        output += generate_scope(nets)
        file.write(output)
        file.close()