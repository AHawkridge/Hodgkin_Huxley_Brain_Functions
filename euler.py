"""
Filename: Euler.py
Description: Finds the equilibrium of a simple two state 
markovian chain using the euler integration method
"""

import numpy as np
import matplotlib.pyplot as plt 

#Euler integration of a two state scheme.
Equations = 2
Constants = 2

steps = 2000
StartTime =0
EndTime=10
StepLength = (EndTime - StartTime)/steps

Alpha = 1
Beta = 1
#Initial state value
FracState1 = 1
FracState2 = 0
FracState = [1,0]
RateConstant1 = Alpha
RateConstant2 = Beta

lst_fs1 = []
lst_fs2 = []
lst_steps = range(0,steps)

for counter1 in range(0,steps):
    time = counter1 * StepLength
    roc1 = (RateConstant2 * FracState2) - (RateConstant1 * FracState1) 
    #Rate of Change 1
    roc2 = (RateConstant1 * FracState1) - (RateConstant2 * FracState2) 
    #Rate of Change 2
    FracState1 = FracState1 + (StepLength * roc1)
    FracState2 = FracState2 + (StepLength * roc2)
    lst_fs1.append(FracState1)
    lst_fs2.append(FracState2)

for counter2 in range(0,steps):
    time = counter2 * StepLength
    RateofChange1 = (RateConstant2 * FracState[1]) - (RateConstant1 * FracState[0]) #Rate of Change 1
    RateofChange2 = (RateConstant1 * FracState[0]) - (RateConstant2 * FracState[1]) #Rate of Change 2
    roc = [RateofChange1,RateofChange2]
    for i in range(0,Equations):
        FracState[i] = FracState[i] +(StepLength*roc[i])

plt.scatter(lst_steps,lst_fs1, label = 'FracState1', color = 'blue',s=2 )

plt.scatter(lst_steps,lst_fs2, label = 'FracState2', color = 'rebeccapurple',s=2)

plt.xlabel("Steps")
plt.ylabel("Fraction open/conductance")
plt.savefig('Images/euler.png', dpi = 300)
plt.legend()
plt.show()