import numpy as np
import matplotlib.pyplot as plt
import control
import array

a = [10, 20]#9.1, 73.5, 125]#1]#6.3223, 17.9995881, 12.811206830175] #1.3223, 18, 12.811]# [ 10, 4]
b = [1, 10, 24]#17, -30]#1, 6, 5] #6, 11.3223, 18, 12.811]#[1,4,4]

a = [ 0.5151, -0.1452, -0.2963, 0.0528]
b = [1, -1.8528, 1.5906, -0.6642, 0.0528]
Ts = 0.1

H_s = control.tf(a,b)
# pt = control.c2d(H_s, Ts)
H_z = control.sample_system(H_s, Ts)

num = list(H_z.num[0][0])
den = list(H_z.den[0][0])

# a = [ 0.4673, -0.3393]
# b = [1, -1.5327, 0.6607]

# num = [0, 0.0891, 0.0108, -0.0679]#0, 0.0891, 0.0108, 0.15]
# den = [1, -2.2885, 1.8460, -0.5255]#1, -0, 0, 1]

num = [0, 0, 0, 0.3205, -0.1885]#         0.1867 , 0.0178, -0.1689]
den=[1, -1.3679, 0.3679, 0.3205, -0.1885]#                -1.9244, 1.2400, -0.2800]

values = []

x = np.linspace(0, 10, 40)
dv_ant = 0


def discrete_value(num, den, dv_ant):
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

ramp= np.ones(len(x)) #np.sin((np.array(x)*100))[:-1]  #np.array(x)*100 #np.ones(len(x)) #
r=[]
intr = []
int1 = 0
error = []
for i in range(len(x)-1):

    num, den, dv_ant = discrete_value(num, den, dv_ant)
    int1 += dv_ant
    intr.append(int1)
    values.append(dv_ant)
    r.append(ramp[i]*dv_ant)
    error.append(r[i]-ramp[i])

    # if len(a) < len(b):
    #     values.append(0)
    #     a = list(a)
    #     a.append(0)
    # elif len(a) == 0:
    #     values.append(0)
    # else:
    #     dv = a[0]/b[0]
    #     dv_ant += dv
    #     values.append(dv_ant)

    #     b_mul = dv*np.array(b)
    #     a = a-b_mul


    #     a=a[1:]
    #     a = list(a)
    #     a.append(0)

# y = np.sin(x*180/np.pi)[:-1]
# plt.plot(y*values)
# plt.plot(y)
# print(values)

# plt.plot(ramp)
# plt.plot(error)
plt.stem(intr)
print(values)
# plt.plot(r)#, 'o')
# # plt.ylim([-1,1])
# # plt.xlim([0,40])
# plt.legend(["rampa", "error", "coeficientes", "salida"])#, "valores de Z"])
plt.figure()
plt.stem(values)
plt.show()