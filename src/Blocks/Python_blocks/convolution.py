import numpy as np

def init_conv(lon):
    global input
    input = np.zeros(lon)


def conv(value, block): 
    global input

    input = np.insert(input, 0, value)
    input = np.delete(input, -1)


    # for i in input:

        # if i < len(x):
        #     input.insert(0, x[i])
        # else:
        #     input.insert(0, 0)


    c = input*block
    suma = sum(c)
    
    return suma