import numpy as np
import control
import matplotlib . pyplot as plt
# % Generating a z - transfer function of a time delay :
Ts = 0.5
Td = 0
nd = int ( Td / Ts )
denom_tf = np . append ([1] , np . zeros ( nd ))
H_delay = control . tf ([1] , [1,0] )
H_delay2 = control.sample_system(H_delay , Ts)
# % Displaying the z - transfer function :
print(' H_delay ( z ) = ' , H_delay )
print(' H_delay2 ( z ) = ' , H_delay2 )
# % Sim of step response of time delay transfer function :
t = np . arange (0 , 20+ Ts , Ts )
(t , y ) = control . step_response ( H_delay2 , t )
y = y-1

yx = np.sin(t)
u = y*yx

# y = y [0 ,:] # Turning 2 D array into 1 D array for plotting
plt . plot (t , y, t, yx, t, u)
plt . xlabel( ' t [ s ] ')
plt . grid ()
plt.show()
# % Generating pdf file of the plotting figure :
# plt . savefig ( ' s t e p _ r e s p o n s e _ h z _ t i m e _ d e l a y . pdf ')
# %
