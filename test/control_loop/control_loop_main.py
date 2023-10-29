import numpy as np
from control_loop_functions import *
import matplotlib.pyplot as plt

time_sim = 4.0
time = 0.0
Ts = 0.01
time_axis = np.arange(0, time_sim, Ts)


scopes = []
init_func()

while time < time_sim: 
    #update signals
    update_signal()

    #execute with new values
    block_exe(time)

    #save the values in scopes
    scopes = scope()

    #update time index
    time += Ts
    

var = 0
for i in scopes:
    plt.plot(time_axis, i[:-1], label = "net"+str(var))
    var += 1

plt.legend()
plt.grid()
plt.show()