import numpy as np


def conv(value, block, input): 
    input = np.insert(input, 0, value)
    input = np.delete(input, -1)

    c = input*block
    suma = sum(c)
    
    return suma, input


def gain(x, G):
    return G*x


def step(value, x, t):
    return value * (x > t)


def add(a, b):
    return a-b


def saturation(value, limit):
    if value >= limit and limit > 0:
        return limit
    elif value <= limit and limit < 0:
        return limit
    else:
        return value

# def sum(a, b):
#     return a-b