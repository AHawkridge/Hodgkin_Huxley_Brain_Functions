"""
Filename: SingleChannelSim.ipynb    
Author: Alex Hawkridge
Date: 31/01/2023
Description: Models a single sodium ion channel,
Number of runs can be changed by changing the EndCounter1 variable
"""


import numpy as np
import matplotlib.pyplot as plt 
import random

StartTime = 0
EndTime = 10
TimeDiv = 0.05
EndCounter1 = 5000
OpenSum = 0
OpenCount = 0

V = -10
AlphaM = (0.1*(-V -58 +25))/(np.exp((-V -58+25)/10)-1)
BetaM = 4*np.exp((-V -58)/10)
AlphaH = 0.07 * np.exp((-V-58)/20)
BetaH = 1/(np.exp((-V-58+30)/10)+1)
AlphaBlock = 0
BetaBlock = 0
Amplitude = 0
lstamp = []
lsttime = []

Occupancy = [1,0,0,0,0,0,0,0,0]
RateConstant =[
    3*AlphaM,
    2*AlphaM,
    1*AlphaM,
    3*BetaM,
    2*BetaM,
    1*BetaM,
    BetaH,
    AlphaH,
    BetaH,
    AlphaH,
    BetaH,
    AlphaH,
    BetaH,
    AlphaH,
    3*BetaM,
    2*BetaM,
    1*BetaM,
    3*AlphaM,
    2*AlphaM,
    1*AlphaM,
    BetaBlock,
    AlphaBlock]

R1=[]
R2=[]

for counter1 in range(int(EndCounter1)):

    Occupancy = [1,0,0,0,0,0,0,0,0]
    RateConstant =[
        3*AlphaM,
        2*AlphaM,
        1*AlphaM,
        3*BetaM,
        2*BetaM,
        1*BetaM,
        BetaH,
        AlphaH,
        BetaH,
        AlphaH,
        BetaH,
        AlphaH,
        BetaH,
        AlphaH,
        3*BetaM,
        2*BetaM,
        1*BetaM,
        3*AlphaM,
        2*AlphaM,
        1*AlphaM,
        BetaBlock,
        AlphaBlock]


    SimTime = StartTime
    DeltaTime = 0
    while SimTime <= EndTime:
        SimTime = SimTime + DeltaTime
        lstamp.append(Amplitude)
        lsttime.append(SimTime)
        if Occupancy[0] == 1:
            Amplitude = 0
            Sum = RateConstant[6] + RateConstant[0]
            DeltaTime = (-1/Sum)*np.log(random.random())
            Occupancy[0] = 0
            Dice = random.random ()* Sum

            if Dice <= RateConstant[6]:
                Occupancy[7] = 1
            else:
                Occupancy[1] = 1

        elif Occupancy[1] == 1:
            Amplitude = 0
            Sum = RateConstant[5] + RateConstant[8] + RateConstant[1]
            DeltaTime = (-1/Sum)*np.log(random.random())
            Occupancy[1] = 0
            Dice = random.random() * Sum

            if Dice <= RateConstant[5]:
                Occupancy[0]=1
            elif Dice > RateConstant[5] and Dice <= (RateConstant[5]
            +RateConstant[8]):
                Occupancy[6]=1
            else:
                Occupancy[2]=1

        elif Occupancy[2] ==1:
            Amplitude = 0
            Sum = RateConstant[4] + RateConstant[10] + RateConstant[2]
            DeltaTime = (-1/Sum)*np.log(random.random())
            Occupancy[2] = 0
            Dice = random.random() * Sum

            if Dice <= RateConstant[4]:
                Occupancy[1]=1
            elif Dice > RateConstant[4] and Dice <= (RateConstant[4]
            +RateConstant[10]):
                Occupancy[5]=1
            else:
                Occupancy[3]=1

        elif Occupancy[3] ==1:
            Amplitude = -1 # This is an open state
            Sum = RateConstant[3] + RateConstant[12] + RateConstant[20]
            DeltaTime = (-1/Sum)*np.log(random.random())
            OpenSum = OpenSum + DeltaTime
            OpenCount = OpenCount +1
            Occupancy[3] = 0
            Dice = random.random() * Sum

            if Dice <= RateConstant[3]:
                Occupancy[2]=1
            elif Dice > RateConstant[3] and Dice <= (RateConstant[3]
            +RateConstant[12]):
                Occupancy[4]=1
            else:
                Occupancy[8]=1


        elif Occupancy[4] ==1:
            Amplitude = 0
            Sum = RateConstant[14-1] + RateConstant[15-1] 
            DeltaTime = (-1/Sum)*np.log(random.random())
            Occupancy[5-1] = 0
            Dice = random.random() * Sum

            if Dice <= RateConstant[14-1]:
                Occupancy[4-1]=1
            else:
                Occupancy[5-1]=1

        elif Occupancy[6-1] ==1:
            Amplitude = 0
            Sum = RateConstant[20-1] + RateConstant[12-1] 
            + RateConstant[16-1]
            DeltaTime = (-1/Sum)*np.log(random.random())
            Occupancy[6-1] = 0
            Dice = random.random() * Sum

            if Dice <= RateConstant[20-1]:
                Occupancy[6-1]=1
            elif Dice > RateConstant[20-1] and Dice <= (RateConstant[20-1]
            +RateConstant[12-1]):
                Occupancy[3-1]=1
            else:
                Occupancy[7-1]=1
        
        elif Occupancy[7-1] ==1:
            Amplitude = 0
            Sum = RateConstant[19-1] + RateConstant[10-1]
            + RateConstant[17-1]
            DeltaTime = (-1/Sum)*np.log(random.random())
            Occupancy[7-1] = 0
            Dice = random.random() * Sum

            if Dice <= RateConstant[19-1]:
                Occupancy[8-1]=1
            elif Dice > RateConstant[19-1] and Dice <= (RateConstant[19-1]
            +RateConstant[10-1]):
                Occupancy[2-1]=1
            else:
                Occupancy[8-1]=1

        elif Occupancy[8-1]:
            Amplitude = 0
            Sum = RateConstant[18-1] + RateConstant[8-1] 
            DeltaTime = (-1/Sum)*np.log(random.random())
            Occupancy[8-1] = 0
            Dice = random.random() * Sum

            if Dice <= RateConstant[18-1]:
                Occupancy[7-1]
            else:
                Occupancy[1-1]=1

        elif Occupancy[9-1]:
            Amplitude = 0
            Sum = RateConstant[18-1] + RateConstant[8-1] 
            DeltaTime = (-1/Sum)*np.log(random.random())
            Occupancy[9-1]=0
            Occupancy[4-1]=1
        
        if SimTime + DeltaTime <= EndTime:
            FullCount = (SimTime + DeltaTime)/TimeDiv
        else:
            FullCount = EndTime / TimeDiv
        

        #Counter2 = SimTime/TimeDiv
        for Counter2 in range(int(SimTime/TimeDiv),int(FullCount)):
            R1.append(Counter2*TimeDiv)
            R2.append(Amplitude)


sub_list = np.array_split(R2,EndCounter1)

arrays = [np.array(x) for x in sub_list]
sol = [np.mean(k) for k in zip(*arrays)]
print(sol)

sub_list2 = np.array_split(R1,EndCounter1)
Tsol = sub_list2[0]
print(Tsol)

plt.plot(Tsol,sol) 
#plt.step(R1,R2)
plt.xlabel("Time (ms)")
plt.ylabel("Occupancy")
plt.savefig('Images/single_channel_sim.png', dpi = 300)

plt.show()