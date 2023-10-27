import control
import numpy as np

def sz_domain_blocks(blocks, Ts, samples):
    """
    This method calls the constants generator method for the blocks in s and z domain
    """
    contants = []
    for block in blocks:
        if block[1] == "tfs":
            contants.append(get_constants(block[2], block[3], Ts, samples))
        elif block[1] == "tfz":
            contants.append(get_constants(block[2], block[3], Ts, samples, discrete=1))
    return contants



def get_constants(num , den, Ts, samples, discrete = 0):
    """
    This method examines the type of input, based in continuous domain or in discrete domain
    Input:
        - num: list with the numerator
        - den: list with the numerator
        - discrete: a flag for discrete transfer function
    """
    if discrete == 0:
        H_s = control.tf(num, den)
        H_z = control.sample_system(H_s, Ts)

        num = list(H_z.num[0][0])
        den = list(H_z.den[0][0])
    
    dv_ant = 0
    list_constants = []
    for i in range(samples):
        num, den, dv_ant = discrete_value(num, den, dv_ant)
        list_constants.append(dv_ant)
    return list_constants


def discrete_value(num, den, dv_ant):
    """
    This method calculates the values for the block in discrete
    Input: 
        - num: list with the numerator
        - den: list with denominator
        - dv_ant: previous output value
    Return:
        - num: list with the new numerator
        - den: list with the new denominator
        - dev_ant: new value of the discrete block
    """
    if len(num) < len(den):
        num = list(num)
        num.append(0)
    elif len(num) == 0:
        pass
    else:
        dv = num[0]/den[0]
        dv_ant = dv

        den_mul = dv*np.array(den)
        num = num-den_mul

        num=num[1:]
        num = list(num)
        num.append(0)
        
    return num, den, dv_ant