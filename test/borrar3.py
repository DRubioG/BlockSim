import numpy as np
import matplotlib.pyplot as plt

a = [ 1]
b = [1,-1]

values = []

if len(a) < len(b):
    for i in range(len(b)-len(a)):
        values.append(0)

x = np.linspace(0, 10)

for i in range(len(x)-1):
    dv = a[0]/b[0]
    values.append(dv)

    b_mul = dv*np.array(b)


    for j in range(len(b)-len(a)):
        # a.extend( 0)
        a = np.append(a,0)

    a = a-b_mul


    a=a[1:]

print(values)
plt.plot(x,values)
plt.show()