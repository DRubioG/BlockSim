#include <stdio.h>
#include "constant_test.h"

void main(){
    
    for(int i=0; i< 10000; i++){
        printf("%.20f\n", block0[i]);
    }
}