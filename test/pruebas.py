import numpy as np 
import control
import matplotlib.pyplot as plt

def step(x, t):
    return 1 * (x > t)

time=np.arange(0,10,1)
cont=0
sal=[]
c = control.tf([1],[1 ,1])
while cont != len(time):
    esc = step(cont, 0)
    
    sal.append(esc*c)

    cont += 1

plt.plot(time, sal)
plt.show()