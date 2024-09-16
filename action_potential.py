""""
Filename: action_potential.py    
Description: Creates a plot of the action potential by using 
solutions to the potassium, sodium and leakage conductances.
"""
import numpy as np
import matplotlib.pyplot as plt


def AlphaM(Vm):
    return 0.1 * (25-(Vm+65)) / (np.exp((25-(Vm+65))/10)-1)

def BetaM(Vm):
    return 4.0 * np.exp(-(Vm+65)/18)

def AlphaH(Vm):
    return 0.07 * np.exp(-(Vm+65)/20)

def BetaH(Vm):
    return 1.0 / (np.exp((30-(Vm+65))/10)+1)

def AlphaN(Vm):
    return 0.01 * (10-(Vm+65)) / (np.exp((10-(Vm+65))/10)-1)

def BetaN(Vm):
    return 0.125 * np.exp(-((Vm+65)+65)/80)

gbarNa = 120.0  
gbarK = 36.0  
gl = 0.3  

Vna = 50.0  
Vk = -77.0  
Vm = -65.0  

Cm =  1 

Vrest = Vm


EndTime = 50 
TimeStep = .01
EndStep = EndTime/TimeStep

Minf = AlphaM(Vm)/(AlphaM(Vm) + BetaM(Vm))
Hinf = AlphaH(Vm)/(AlphaH(Vm) + BetaH(Vm))
Ninf = AlphaN(Vm)/(AlphaN(Vm) + BetaN(Vm))

TauM = 1/(AlphaM(Vm) + BetaM(Vm))
TauH = 1/(AlphaH(Vm) + BetaH(Vm))
TauN = 1/(AlphaN(Vm) + BetaN(Vm))

m = 0.0
n = 0.0
h = 1.0

lstVm = []
lstt = []

for count in range(0,int(EndStep)):
    t = count * TimeStep

    m += TimeStep * (AlphaM(Vm) * (1.0 - m) - BetaM(Vm) * m)
    n += TimeStep * (AlphaN(Vm) * (1.0 - n) - BetaN(Vm) * n)
    h += TimeStep * (AlphaH(Vm) * (1.0 - h) - BetaH(Vm) * h)
    
    Itotal = (gl * (Vm-Vrest)) + (gbarK * n**4 * (Vm - Vk)) + (gbarNa * m**3 * h * (Vm - Vna))
    Vm += TimeStep / Cm * (-Itotal)
    
    lstVm.append(Vm)
    lstt.append(t)


plt.plot(lstt, lstVm)
plt.xlabel('Time (ms)')
plt.ylabel('Membrane potential (mV)')
plt.savefig('Images/action_potential.png', dpi = 300)
plt.show()