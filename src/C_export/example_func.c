// #include "example_func.h"
#include "../Blocks/C_blocks/functions.c"
// #include "definitions.h"
#include "constants.h"


float net1_ant = 0;
float net2_ant = 0;
float net3_ant = 0;
float net4_ant = 0;
float net5_ant = 0;
float net6_ant = 0;
float net7_ant = 0;

float net1 = 0;
float net2 = 0;
float net3 = 0;
float net4 = 0;
float net5 = 0;
float net6 = 0;
float net7 = 0;

float input1[100];
float input2[100];

struct Conv{
    float value;
    float input1[100];
};

float value1;
float value2;

void net_update(){
    net1 = net1_ant;
    net2 = net2_ant;
    net3 = net3_ant;
    net4 = net4_ant;
    net5 = net5_ant;
    net6 = net6_ant;
    net7 = net7_ant;
}

void block_exe(float time_counter){
    net1_ant = step(5, time_counter, 0);
    net2_ant = res(net1, net4);
    // value1 = conv(net2, block1, input1);
    // value2 = conv(net3, block2, input2);
    net3_ant = convolution(net2, block1, input1);
}

// float conv(float a, float *b, float *c){

//     return 0;
// }