import numpy as np
import matplotlib.pyplot as plt

x = [1,1,1,1,1,1]
h = np.array([0,0,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1])

x = [1,2,1,1]
h=np.array([1, -1, 0, 0, 1, 1])

x= [5, 4, 3, 2, 1, 0]
h=np.array([3, 2, 1])


x= [0, 1, 2, 3, 4]
h = np.array([0,0,0,0,0,1,1,1,1,1,1,1,1,1, 1, 1, 1,1 , 1, 1, 1,1 ])


input = list(np.zeros(len(h)))

graph = []

for i in range(24):

    input = list(input)
    if i < len(x):
        input.insert(0, x[i])
    else:
        input.insert(0, 0)
    input.pop(-1)
    input = np.array(input)
    
    c = input*h
    suma = sum(c)

    print(c)
    print(suma)

    graph.append(suma)
    
plt.stem(graph)
plt.show()




    # for j in range(len(h)-1):
    #     print("x[",j, "] = ", input[j])
        


    #     if i-j < 0:
    #         g = 0
    #         print("h[", i-j, "] = ", h[g])
            
    #     else:
    #         g = i-j
    #         print("h[", i-j, "] = ", h[g])


    #     c += x[j]*h[g]


    # print(c)