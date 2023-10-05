from ReadBlockSim import *
from ExportPython import *
import control
import numpy as np


class BlockSim():
    def __init__(self, file):
        self.file = file
        self.nets = []
        self.blocks = []
        self.scopes = []
        self.generate()



    def generate(self):
        read_file = ReadBlockSim(self.file)
        self.nets, self.blocks, self.scopes, self.duration, self.Ts = read_file.read()

        # self.generate_file()
        self.samples = int(self.duration/self.Ts)
        self.sz_domain_blocks()

        # python_file = ExportPython(self.file)
        # python_file.generate_file()
        pass


    def sz_domain_blocks(self):
        for block in self.blocks:
            if block[1] == "tfs":
                self.get_constants(block[2], block[3])


    def get_constants(self, num , den, discrete = 0):
        self.constants = []
        if discrete == 0:
            H_s = control.tf(num, den)
            H_z = control.sample_system(H_s, self.Ts)

            num = list(H_z.num[0][0])
            den = list(H_z.den[0][0])
        
        dv_ant = 0
        for i in range(self.samples):
            num, den, dv_ant = self.discrete_value(num, den, dv_ant)
            self.constants.append(dv_ant)
        print()


    def discrete_value(self, num, den, dv_ant):
        if len(num) < len(den):
            num = list(num)
            num.append(0)
        elif len(num) == 0:
            pass
        else:
            dv = num[0]/den[0]
            dv_ant = dv

            den_mul = dv*np.array(den)
            num = num-den_mul

            num=num[1:]
            num = list(num)
            num.append(0)
            
        return num, den, dv_ant