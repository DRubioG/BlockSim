import numpy as np
from example_func import *
import matplotlib.pyplot as plt

time = np.arange(0, 10, 1)
cont = 0

init_func()

while cont != len(time):
    #update signals
    update_signal()

    #execute with new values
    blocks_exe(cont)

    #save the values in scopes
    scopes = scope()

    #update time index
    cont+=1

var = 0
for i in scopes:
    var += 1
    plt.plot(time, i, label = "scope"+str(var))
    # plt.legend()

# plt.legend(["salida", "suma", "entrada2", "entrada1"])
plt.legend()
plt.grid()
plt.show()