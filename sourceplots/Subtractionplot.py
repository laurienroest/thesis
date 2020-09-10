import numpy as np
import math
import scipy
from scipy import optimize
import matplotlib
from matplotlib import gridspec
from  matplotlib import rc
from matplotlib import cm
import matplotlib.pyplot as plt
import pandas as pd


########## Load data ####################################

mean_rep = pd.read_csv('Data/Subtracted_spectra_1.45.csv')


import matplotlib
from matplotlib import rc

nbins = 1861
rescolors = plt.rcParams['axes.prop_cycle'].by_key()['color']

########################################################################

def bandgap(x, amp, BG,b):
    return amp * (x - BG)**(b)

########################################################################


nrows, ncols = 1,1
gs = matplotlib.gridspec.GridSpec(nrows,ncols)
plt.figure(figsize=(ncols*9,nrows*7))

cm_subsection = np.linspace(0,1,24) 
colors = [cm.viridis(x) for x in cm_subsection]

hfont = rc('font',**{'family':'sans-serif','sans-serif':['Sans Serif']})
          
for i in range(1):
    ax = plt.subplot(gs[i])
    ax.set_xlim([0.5,2.5])
    ax.set_ylim([-1e1,2e3])
    ax.set_ylabel('Intensity (a.u.)', fontsize=26)
    ax.set_xlabel('Energy loss (eV)', fontsize=26)
    
    ax.tick_params(which='major',direction='in',length=10, labelsize=16)
    ax.tick_params(which='minor',length=10)
    ax.set_xticks([.5, 1, 1.5, 2, 2.5, 3])
    
    p1=ax.plot(np.linspace(-.3, 9, nbins), mean_rep['spectrum4'], 'k--',ls="dashdot",lw=2)

    
    p2=ax.plot(np.linspace(-.3, 9, nbins), mean_rep['match4_median'], color=rescolors[1],ls="dashed",lw=2)
    ax.fill_between(np.linspace(-.3, 9, nbins), mean_rep['match4_low'], mean_rep['match4_high'], \
                    color=rescolors[1], alpha=.2)
    p2b=ax.fill(np.NaN,np.NaN,color=rescolors[1],alpha=0.2)
    
    p3 = ax.plot(np.linspace(-.3, 9, nbins), mean_rep['dif4_median'], 'k-',color=rescolors[0],lw=2)
    ax.fill_between(np.linspace(-.3, 9, nbins), mean_rep['dif4_low'], mean_rep['dif4_high'], color=rescolors[0], alpha=.2)
    p3b=ax.fill(np.NaN,np.NaN,color=rescolors[0],alpha=0.2)
    ax.set_yticks([])

    ax.legend([(p1[0]),(p3[0],p3b[0]),(p2[0],p2b[0])],['sp4 (orig)','sp4 (subtr)',"ZLP"],loc='upper right', fontsize = 19)
    
    

plt.tight_layout()
plt.savefig('SubtractedEELS_plot_sp4.pdf')
print("Saved fig = SubtractedEELS_plot_sp4.pdf")


