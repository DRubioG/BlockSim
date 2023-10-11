import numpy as np
from example_func import *
import matplotlib.pyplot as plt

time_sim = 1
cont = 0.0
Ts = 0.1
time = np.arange(0, time_sim, Ts)


scopes = []
init_func()

while cont < time_sim: 
    #update signals
    update_signal()

    #execute with new values
    blocks_exe(cont)

    #save the values in scopes
    scopes = scope()

    #update time index
    cont += Ts
    

var = 0
for i in scopes:
    var += 1
    plt.plot(time, i, label = "scope"+str(var))

plt.legend()
plt.grid()
plt.show()