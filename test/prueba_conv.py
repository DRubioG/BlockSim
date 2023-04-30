x = [0.5, 2, 0, 0, 0, 0]
h = [1, 1, 1, 0, 0, 0, 0]

for i in range(len(x)):
    c=0
    for j in range(len(h)-1):
        print("x[",j, "] = ", x[j])
        
        if i-j < 0:
            g = 0
            print("h[", i-j, "] = ", h[g])
            
        else:
            g = i-j
            print("h[", i-j, "] = ", h[g])
        c += x[j]*h[g]
    print(c)