#include "functions.c"
#include "control_loop_constants.h"


float net0_ant = 0;
float net1_ant = 0;
float net2_ant = 0;
float net3_ant = 0;
float net4_ant = 0;

float net0 = 0;
float net1 = 0;
float net2 = 0;
float net3 = 0;
float net4 = 0;

float input0[40];
float input1[40];

void net_update(){
	net0 = net0_ant;
	net1 = net1_ant;
	net2 = net2_ant;
	net3 = net3_ant;
	net4 = net4_ant;
}

// void block_exe(){
// 	net0_ant = step(1.0, time, 1.0);
// 	net1_ant = add(net0, net4);
// 	net3_ant = convolution(net2, block0, input0, 40);
// 	net4_ant = convolution(net3, block1, input1, 40);
// 	net2_ant = gain(net1, 5);
// }


void block_exe(float time){
	net0_ant = step(1.0, time, 1.0);
	net1_ant = add(net0, net4);
	net3_ant = convolution(net2, block0, input0, 40);
	net4_ant = convolution(net3, block1, input1, 40);
	net2_ant = gain(net1, 5);
}