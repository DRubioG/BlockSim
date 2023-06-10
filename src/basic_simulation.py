import numpy as np
from example_func import *
import matplotlib.pyplot as plt

time_sim = 10
Tstep = 10
time = np.linspace(0, time_sim, Tstep)
cont = 0
Ts = 0.1

scopes = []
init_func()

while cont != time_sim:

    if (cont%(Ts*Tstep))==0:
        #update signals
        update_signal()

        #execute with new values
        blocks_exe(cont)

    # if cont == 10.0:
    #     break
    #save the values in scopes
    scopes = scope()

    #update time index
    cont+= 1

var = 0
for i in scopes:
    var += 1
    plt.plot(i, label = "scope"+str(var))

plt.legend()
plt.grid()
plt.show()