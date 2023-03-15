import numpy as np
import matplotlib.pyplot as plt
import control
import array

a =  [ 1]
b = [2, 1, 1]
Ts = 0.001

H_s = control.tf(a,b)
H_z = control.sample_system(H_s, Ts)

num = list(H_z.num[0][0])
den = list(H_z.den[0][0])

# a = [ 0.4673, -0.3393]
# b = [1, -1.5327, 0.6607]

# num = [0, 0.0891, 0.0108, -0.0679]#0, 0.0891, 0.0108, 0.15]
# den = [1, -2.2885, 1.8460, -0.5255]#1, -0, 0, 1]

values = []

x = np.linspace(0, 1, 10000)
dv_ant = 0


def discrete_value(num, den, dv_ant):
    if len(num) < len(den):
        num = list(num)
        num.append(0)
    elif len(num) == 0:
        pass
    else:
        dv = num[0]/den[0]
        dv_ant += dv

        den_mul = dv*np.array(den)
        num = num-den_mul

        num=num[1:]
        num = list(num)
        num.append(0)
        
    return num, den, dv_ant

ramp= (np.array(x)*1)[:-1]      #np.sin((np.array(x)*100))[:-1]
r=[]
error = []
for i in range(len(x)-1):

    num, den, dv_ant = discrete_value(num, den, dv_ant)
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

plt.plot(ramp)
plt.plot(error)
plt.plot(values)
print(values)
plt.plot(r)#, 'o')
# plt.ylim([-1,1])
# plt.xlim([0,40])
plt.legend(["rampa", "error", "coeficientes", "salida"])#, "valores de Z"])
plt.show()