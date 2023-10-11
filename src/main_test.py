import numpy as np
from example_func import *
import matplotlib.pyplot as plt

time_sim = 10.0
time = 0.0
Ts = 0.001
time = np.arange(0, time_sim, Ts)


scopes = []
init_func()

while time < time_sim: 
    #update signals
    update_signal()

    #execute with new values
    blocks_exe(time)

    #save the values in scopes
    scopes = scope()

    #update time index
    time += Ts
    

var = 0
for i in scopes:
    var += 1
    plt.plot(time, i, label = "scope"+str(var))

plt.legend()
plt.grid()
plt.show()