#include <stdio.h>
// #include "definitions.h"
#include "example_func.c"

int main(){
    float time_sim = 10;
    float time_counter = 0.0;
    float time_incr = 0.1;

    while(time_counter < time_sim){
        net_update();

        block_exe(time_counter);

        time_counter += time_incr;
    }


    return 0;
}