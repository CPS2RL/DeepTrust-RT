

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.gridspec as gridspec
import matplotlib.patches as patches



def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)



#n=5 task_response
x=[10,20,30,40,45,50,55,60,70,75,80]
x1=[10,20,30,40,45,50,55]
y=[0.1152,0.2881,0.3355,0.4498,0.51763,0.5259,0.62721]
y2=[0.0459,0.1131,0.1452,0.1975,0.25988,0.2719,0.3135,0.3276,0.44795,0.4592,0.4684]
y3=[0.04233,0.10427,0.1353,0.1849,0.2442,0.2564,0.29711,0.3109,0.42917,0.4407,0.4500]


fig = plt.figure(figsize=(10, 5))



#plt.gca().set_aspect('equal')  # Set aspect ratio equal
plt.xlabel("Utilization (%)",fontsize=35)
plt.ylabel("Sparsity",fontsize=35)
#plt.title("Response time analysis",fontsize=35)

plt.plot(x,y2,"o",markersize=8,linestyle='-',linewidth=4,color='#006400',label=r"DeepTrust$^\mathrm{RT}$-FUSION",markerfacecolor='white', markeredgecolor='#006400')
plt.plot(x1,y,"x",markersize=8,linestyle='--',linewidth=3,color='black',label=r"DeepTrust$^\mathrm{RT}$-LW",markerfacecolor='white', markeredgecolor='black')
plt.plot(x,y3,"s",markersize=8,linestyle='-.',linewidth=2,color='#8B0000',label="No-TEE",markerfacecolor='white', markeredgecolor='#8B0000')


plt.xticks(fontsize=35)
plt.yticks(fontsize=35)
#plt.legend(loc='upper left',fontsize='large')
#plt.savefig("task_response_n5.pdf", format="pdf", bbox_inches="tight")


# Set the x-axis and y-axis limits or ranges
plt.xlim(0,100)  # Set the x-axis range
plt.ylim(0,1)  # Set the y-axis range


# Define the coordinates and dimensions of the red rectangular box
x_left = 55
x_right = 80
y_bottom = plt.ylim()[0]
y_top = plt.ylim()[1]

# Create a red rectangular box
rectangle = patches.Rectangle((x_left, y_bottom), x_right - x_left, y_top - y_bottom,
                              linewidth=1, edgecolor='red', facecolor='red', alpha=0.2)

# Add the rectangle to the first subplot
plt.gca().add_patch(rectangle)


plt.legend(loc='upper left',fontsize=30,frameon=False)
#plt.suptitle("Model: AlexNet-squeezed, n=5", fontsize=16) 

plt.savefig("alex_n5_res.pdf", format="pdf", bbox_inches="tight")

# Adjust the spacing between subplots
#plt.tight_layout()
plt.show()
