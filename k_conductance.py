
"""
Filename: K_conductance.py    
Description: Finds the explicit solutions to the the potassium 
conductance for a varying voltages
"""

import numpy as np
import matplotlib.pyplot as plt

lstgk = []
lstt = []
EndTime = 10 
TimeStep = .005
gbarK = 1
EndStep = EndTime/TimeStep
interval = range(-50,50,5)

print("Explicit Solution")
print("Hodgkin-Huxley")

for v in interval:
    AlphaN = 0.01*(v+10) / (np.exp((v+10)/10)-1)
    BetaN = 0.125*np.exp(v/80)

    Ninf = AlphaN/(AlphaN + BetaN)


    TauN = 1/(AlphaN + BetaN)
    

    #initial conditions
    N0 = 1

    for count in range(0,int(EndStep)):
        t = count * TimeStep
        n = Ninf - ((Ninf - N0)*np.exp(-t/TauN))
        
        gk = n**4 * gbarK
        
        lstt.append(t)
        lstgk.append(gk)

#plot shows the conductances during an action potential.
plt.scatter(lstt,lstgk,s=0.1)
plt.xlabel("Time (t)")
plt.ylabel("Potassium Conductance (gna)")
plt.savefig('Images/K_conductance.png', dpi = 300)
plt.show()