"""
Filename: Na_conductance.py    
Author: Alex Hawkridge

Description: Finds the explicit solutions to the the sodium
conductance for a varying voltages
"""

import numpy as np
import matplotlib.pyplot as plt

lstgna = []
lstt = []
EndTime = 10 
TimeStep = .005
gbarNa = 1
EndStep = EndTime/TimeStep
interval = range(-50,50)

print("Explicit Solution")
print("Hodgkin-Huxley")

for v in interval:
    AlphaM = (0.1 * (-v - 58 + 25))/(np.exp((- v - 58 + 25)/10)-1) 
    BetaM = 4*np.exp((-v-58)/18)

    AlphaH = 0.07*np.exp((-v - 58)/20)
    BetaH = 1/ (np.exp((-v - 58 + 30)/10)+1)

    Minf = AlphaM/(AlphaM + BetaM)
    Hinf = AlphaH/(AlphaH + BetaH)

    TauM = 1/(AlphaM + BetaM)
    TauH = 1/(AlphaH + BetaH)

    #initial conditions
    M0 = 0 
    H0 = 1

    for count in range(0,int(EndStep)):
        t = count * TimeStep
        m = Minf - ((Minf - M0)*np.exp(-t/TauM))
        h = Hinf - ((Hinf - H0)*np.exp(-t/TauH))
        gna = (m ** 3)* h * gbarNa
        
        lstt.append(t)
        lstgna.append(gna)

#plot shows the conductances during an action potential.
plt.plot(lstt,lstgna)
plt.xlabel("Time (t)")
plt.ylabel("Sodium Conductance (gna)")
plt.savefig('Images/Na_conductance.png', dpi = 300)
plt.show()