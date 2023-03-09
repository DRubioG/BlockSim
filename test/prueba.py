import numpy as np
import matplotlib.pyplot as plt


def sum(a,b):
    return a + b

time = np.arange(0,10,0.01)

net1 = 0#np.zeros(len(time))
net2 = 0#np.zeros(len(time))
net3 = 0#np.zeros(len(time))

scope1 = []
scope2 = []
scope3 = []
scope4 = []

def step1(x):
    return 1 * (x > 0)

def step2(x):
    return 1 * (x > 30)

def gain(x, G):
    return G*x


cont = 0
net1_ant = 0
net2_ant = 0
net3_ant = 0
net4_ant = 0

while cont != len(time):
    net1 = net1_ant
    net2 = net2_ant
    net3 = net3_ant
    net4 = net4_ant

    net1_ant = step1(cont)
    net2_ant = step2(cont)
    net3_ant = sum(net1 ,net2)
    net4_ant = gain(net3, 3)
    print(net3_ant)

    scope1.append(net4_ant)
    scope2.append(net3_ant)
    scope3.append(net2_ant)
    scope4.append(net1_ant)

    cont += 1



plt.plot(time, scope1)
plt.plot(time, scope2)
plt.plot(time, scope3)
plt.plot(time, scope4)
plt.legend(["salida", "suma", "entrada2", "entrada1"])
plt.show()