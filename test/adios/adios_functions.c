#include "functions.c"
#include "adios_constants.h"


float net0_ant = 0;
float net1_ant = 0;
float net2_ant = 0;
float net3_ant = 0;
float net4_ant = 0;
float net5_ant = 0;

float net0 = 0;
float net1 = 0;
float net2 = 0;
float net3 = 0;
float net4 = 0;
float net5 = 0;

float input0[1000];
float input1[1000];
float input2[1000];

void net_update(){
	net0 = net0_ant;
	net1 = net1_ant;
	net2 = net2_ant;
	net3 = net3_ant;
	net4 = net4_ant;
	net5 = net5_ant;
}

void block_exe(float time){
	net0_ant = step(1.0, time, 0.0);
	net1_ant = add(net0, net5);
	net3_ant = add(net2, net4);
	
	net2_ant = convolution(net1, block0, input0, 1000);
	net4_ant = convolution(net3, block1, input1, 1000);
	net5_ant = convolution(net4, block2, input2, 1000);
	// printf("%lf, ", net4_ant);
	// printf("%lf, ", net3_ant);
	// printf("%lf, ", net2_ant);
	// printf("%lf, ", net1_ant);
	printf("%lf, ", net5_ant);
}