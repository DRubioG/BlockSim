import numpy as np


def conv(value, block, input): 
    input = np.insert(input, 0, value)
    input = np.delete(input, -1)

    c = input*block
    suma = sum(c)
    
    return suma, input


def gain(x, G):
    return G*x


def step(x, t):
    return 1 * (x > t)


def add(a, b):
    return a+b


def res(a, b):
    return a-b