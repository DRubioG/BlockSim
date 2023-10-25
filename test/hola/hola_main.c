#include <stdio.h>
#include "hola_functions.c"

int main(){
    float time_counter = 0.0;
    float time_incr = 0.01;

    while(1){
        net_update();

        block_exe();

        /* This part is only for an execution with blocks that requires time
        WARNING: variable overflow */
        /*block_exe(time_counter);
        time_counter += time_incr;*/
    }

    return 0;
}
