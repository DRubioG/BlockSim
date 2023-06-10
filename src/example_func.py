from Blocks.Python_blocks.add import *
from Blocks.Python_blocks.gain import *
from Blocks.Python_blocks.step import *
from Blocks.Python_blocks.convolution import *
from constants import *


def init_func():
    global net1_ant, net2_ant, net3_ant, net4_ant, net5_ant, net6_ant, net7_ant
    net1_ant = 0
    net2_ant = 0
    net3_ant = 0
    net4_ant = 0
    net5_ant = 0
    net6_ant = 0
    net7_ant = 0
    global scope1, scope2, scope3, scope4, scope5, scope6, scope7
    scope1 = []
    scope2 = []
    scope3 = []
    scope4 = []
    scope5 = []
    scope6 = []
    scope7 = []
    init_conv(len(block1))

def update_signal():
    global net1, net2, net3, net4, net5, net6, net7
    net1 = net1_ant
    net2 = net2_ant
    net3 = net3_ant
    net4 = net4_ant
    net5 = net5_ant
    net6 = net6_ant
    net7 = net7_ant


def blocks_exe(cont):
    global net1_ant, net2_ant, net3_ant, net4_ant, net5_ant, net6_ant, net7_ant
    
    net1_ant = step(cont, 0)
    net2_ant = step(cont, 3)
    net3_ant = add(net1, net2)
    net4_ant = res(net3, net6)
    net5_ant = gain(net4, 2)
    net6_ant = gain(net5, 0.1)
    # net5_ant = conv(net4, block1)
    # net6_ant = conv(net5, block1)
    net7_ant = conv(net6, block1)

    # net3_ant = add(net1 ,net2)
    # net4_ant = gain(net3, 3)

def scope(): 
    scope1.append(net1_ant)
    scope2.append(net2_ant)
    scope3.append(net3_ant)
    scope4.append(net4_ant)
    scope5.append(net5_ant)
    scope6.append(net6_ant)
    scope7.append(net7_ant)


    return scope1, scope2, scope3, scope4, scope5, scope6, scope7