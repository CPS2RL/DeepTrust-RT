

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.gridspec as gridspec
import matplotlib.patches as patches



def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)


fig = plt.figure(figsize=(10, 5))


## n=15 task
x=[10,20,30,40,50,55,58,60,70,80,85,90]
y1=[100,100,100,100,99,42,14,4,0,0,0,0]
y2=[100,100,100,100,100,51,26,17,7,3,2,1]
y3=[100,100,100,100,100,100,100,100,96,94,92,90]

##n=10 task
x=[10,30,40,50,55,58,60,62,65,70,80,85,90]
y1=[100,100,100,100,100,90,20,2,0,0,0,0,0]
y2=[100,100,100,100,100,100,99,97,14,11,4,3,2]
y3=[100,100,100,100,100,100,100,98,89,58,19,12,9]

#n=5 task scheduling 

x=[10,20,30,40,45,50,55,60,70,75,80,90]
y1=[100,100,100,100,67,4,1,0,0,0,0,0]
y2=[100,100,100,100,100,58,14,9,4,2,1,0]
y3=[100,100,100,100,100,100,100,100,58,33,24,17]



plt.xlabel("Utilization (%)",fontsize=35)
plt.ylabel("Acceptance Ratio (%)",fontsize=35)
#plt.plot(X_,Y1_,linestyle='--',color='b',label="Vanilla RM Scheduling")
#plt.plot(X_,Y2_,linestyle='-',label="Proposed Work")
#plt.title("Feasible taskset",fontsize=35)
#plt.plot(x,y1,"^",markersize=4,linestyle='--',color='b',label="EDF-LW")
#plt.plot(x,y3,"s",markersize=4,linestyle='-.',color='orange',label="No-TEE")

plt.plot(x,y2,"p",markersize=8,linestyle='-',linewidth=4,color='#006400',label=r"DeepTrust$^\mathrm{RT}$-FUSION",markerfacecolor='white', markeredgecolor='#006400')
plt.plot(x,y1,"x",markersize=8,linestyle='--',linewidth=3,color='black',label=r"DeepTrust$^\mathrm{RT}$-LW",markerfacecolor='white', markeredgecolor='black')
plt.plot(x,y3,"s",markersize=8,linestyle='-.',linewidth=3,color='#8B0000',label="No-TEE",markerfacecolor='white', markeredgecolor='#8B0000')


plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
axes=plt.gca()

# Set the x-axis and y-axis limits or ranges
plt.xlim(0,100)  # Set the x-axis range
plt.ylim(0,105)  # Set the y-axis range





plt.legend(loc='center left',fontsize=30,frameon=False)
# Display the custom legend in a single row


#plt.suptitle("Model: AlexNet-squeezed, n=5", fontsize=16) 

plt.savefig("alex_n5_sched.pdf", format="pdf", bbox_inches="tight")

# Adjust the spacing between subplots
#plt.tight_layout()
plt.show()
