from Blocks.Python_blocks.add import *
from Blocks.Python_blocks.gain import *
from Blocks.Python_blocks.step import *

def init_func():
    global net1_ant, net2_ant, net3_ant, net4_ant
    net1_ant = 0
    net2_ant = 0
    net3_ant = 0
    net4_ant = 0
    global scope1, scope2, scope3, scope4
    scope1 = []
    scope2 = []
    scope3 = []
    scope4 = []

def update_signal():
    global net1, net2, net3, net4
    net1 = net1_ant
    net2 = net2_ant
    net3 = net3_ant
    net4 = net4_ant

def blocks_exe(cont):
    global net1_ant, net2_ant, net3_ant, net4_ant
    net1_ant = step(cont, 0)
    net2_ant = step(cont, 5)
    net3_ant = add(net1 ,net2)
    net4_ant = gain(net3, 3)

def scope(): 
    scope1.append(net4_ant)
    scope2.append(net3_ant)
    scope3.append(net2_ant)
    scope4.append(net1_ant)

    return scope1, scope2, scope3, scope4