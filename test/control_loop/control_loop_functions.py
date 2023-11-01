from functions import *
from control_loop_constants import *

def init_func():
	global net0_ant, net1_ant, net2_ant, net3_ant, net4_ant
	net0_ant = 0
	net1_ant = 0
	net2_ant = 0
	net3_ant = 0
	net4_ant = 0
	global scope1, scope2, scope3, scope4, scope5
	scope1 = []
	scope2 = []
	scope3 = []
	scope4 = []
	scope5 = []
	global input0, input1
	input0 = np.zeros(len(block0))
	input1 = np.zeros(len(block1))

def update_signal():
	global net0, net1, net2, net3, net4
	net0 = net0_ant
	net1 = net1_ant
	net2 = net2_ant
	net3 = net3_ant
	net4 = net4_ant

def block_exe(time):
	global input0, input1
	global net0_ant, net1_ant, net2_ant, net3_ant, net4_ant
	net0_ant = step(1.0, time, 1.0)
	net1_ant = add(net0, net4)
	net3_ant, input0 = conv(net2, block0, input0)
	net4_ant, input1 = conv(net3, block1, input1)
	net2_ant = gain(net1, 3)
	
def scope():
	scope1.append(net0_ant)
	scope2.append(net1_ant)
	scope3.append(net2_ant)
	scope4.append(net3_ant)
	scope5.append(net4_ant)
	return scope1, scope2, scope3, scope4, scope5