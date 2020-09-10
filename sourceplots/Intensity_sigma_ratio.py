#!/usr/bin/env python
# coding: utf-8

# In[53]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import copy
import warnings
warnings.filterwarnings('ignore')



######################################################

mean = []
columns = ['x', 'y_norm', 'sigma', 'time', 'energy']

file10_60 = pd.read_csv('data/meanfile_10_60_.csv', skiprows = 1, names=columns)
file100_60 = pd.read_csv('data/meanfile_100_60_.csv', skiprows = 1, names=columns)
file10_200 = pd.read_csv('data/meanfile_10_200_.csv', skiprows = 1, names=columns)
file100_200= pd.read_csv('data/meanfile_100_200_.csv', skiprows = 1, names=columns)

######################################################

def smooth(x,window_len=10,window='hanning'):
    s=np.r_[x[window_len-1:0:-1],x,x[-2:-window_len-1:-1]]

    if window == 'flat': #moving average
        w=np.ones(window_len,'d')
    else:
        w=eval('np.'+window+'(window_len)')

    y=np.convolve(w/w.sum(),s,mode='valid')
    
    index = int(window_len/2)
    return y[(index-1):-(index)]
######################################################

linestyles = ['solid', 'dotted', 'dashed', 'dashdot']

plt.figure(figsize=(5,3.5))

for i, file in enumerate([file10_60, file100_60, file100_200, file10_200]):
    E_min = -.1
    E_max = 1


    wl = 14
    
    plt.axhline(y=1, linestyle='--', color='black')
    
    plt.xlim([-.1, 1])
    #plt.title('Intensity to uncertainty ratio', fontsize=16)
    plt.axvline(x = .2, color='black',ls="dashed",alpha=0.2)
    plt.axvline(x = .25, color='black',ls="dashed",alpha=0.2)
    plt.axvline(x = .9, color='black',ls="dashed",alpha=0.2)
    plt.xlabel('Energy loss (eV)', fontsize=16)
    plt.ylabel(r'$I^{(\rm exp)}_{\rm EEL}/\sigma^{(\rm exp)}~(\Delta E)$', fontsize=16)
    plt.xticks(fontsize=11)
    plt.yticks(fontsize=11)

    labelp = r"$t_{\rm exp}=$"+str(file['time'].max())+" ms, $E_b=$"+str(file['energy'].max())+" keV"
    
    plt.plot(file['x'], smooth(file['y_norm']/file['sigma'], wl), \
             linestyle=linestyles[i], linewidth = 2, label=labelp)
    
    plt.legend(loc='upper right', fontsize=9)

plt.tight_layout()
plt.savefig('intensity_to_error_ratio.pdf')
print("Saved figure: intensity_to_error_ratio.pdf")


# In[ ]:




