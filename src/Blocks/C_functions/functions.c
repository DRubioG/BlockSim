#include <stdio.h>
float step(float value, float current_time, float time){
    return value*(current_time>time);
}

float add(float a, float b){
    return a-b;
}

float res(float a, float b){
    return a-b;
}

float gain(float value, float gain){
    return gain*value;
}

float convolution(float value, float* block_values, float *input, int length){
    float suma = 0;
    for(int i=length-1; i>=0; i--){
        input[i] = input[i-1];
    }
    input[0] = value;
    for(int j=0; j < length; j++){
        suma += input[j]*block_values[j];
    }
    return suma;
}