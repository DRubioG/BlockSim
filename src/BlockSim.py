from ReadBlockSim import *
from Export.ExportPython import *
from Export.ExportC import *
from samples import *
import control
import numpy as np


class BlockSim():
    """
    This is the main class of the project, it uses the other different classes for working
    """
    def __init__(self, file, tipo="Python"):
        self.file = file
        self.nets = []
        self.blocks = []
        self.scopes = []
        self.constants = []
        self.tipo = tipo
        self.generate()


    def generate(self):
        """
        This method executes the different options
        """
        read_file = ReadBlockSim(self.file)
        self.nets, self.blocks, self.scopes, self.duration, self.Ts = read_file.read()

        self.samples = int(self.duration/self.Ts)
        self.constants = sz_domain_blocks(self.blocks, self.Ts, self.samples)

        if self.tipo == "Python":
            python_file = ExportPython(self.file)
            python_file.generate_file(self.nets, self.blocks, self.scopes, self.constants, self.duration, self.Ts)
        elif self.tipo == "C":
            python_file = ExportC(self.file)
            python_file.generate_file(self.nets, self.blocks, self.constants, self.Ts)


    # def sz_domain_blocks(self):
    #     """
    #     This method calls the constants generator method for the blocks in s and z domain
    #     """
    #     for block in self.blocks:
    #         if block[1] == "tfs":
    #             self.get_constants(block[2], block[3])
    #         elif block[1] == "tfz":
    #             self.get_constants(block[2], block[3], discrete=1)



    # def get_constants(self, num , den, discrete = 0):
    #     """
    #     This method examines the type of input, based in continuous domain or in discrete domain
    #     Input:
    #         - num: list with the numerator
    #         - den: list with the numerator
    #         - discrete: a flag for discrete transfer function
    #     """
    #     if discrete == 0:
    #         H_s = control.tf(num, den)
    #         H_z = control.sample_system(H_s, self.Ts)

    #         num = list(H_z.num[0][0])
    #         den = list(H_z.den[0][0])
        
    #     dv_ant = 0
    #     list_constants = []
    #     for i in range(self.samples):
    #         num, den, dv_ant = self.discrete_value(num, den, dv_ant)
    #         list_constants.append(dv_ant)
    #     self.constants.append(list_constants)


    # def discrete_value(self, num, den, dv_ant):
    #     """
    #     This method calculates the values for the block in discrete
    #     Input: 
    #         - num: list with the numerator
    #         - den: list with denominator
    #         - dv_ant: previous output value
    #     Return:
    #         - num: list with the new numerator
    #         - den: list with the new denominator
    #         - dev_ant: new value of the discrete block
    #     """
    #     if len(num) < len(den):
    #         num = list(num)
    #         num.append(0)
    #     elif len(num) == 0:
    #         pass
    #     else:
    #         dv = num[0]/den[0]
    #         dv_ant = dv

    #         den_mul = dv*np.array(den)
    #         num = num-den_mul

    #         num=num[1:]
    #         num = list(num)
    #         num.append(0)
            
    #     return num, den, dv_ant