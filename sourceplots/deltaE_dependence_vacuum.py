import numpy as np
from numpy import loadtxt
import math
import scipy
#import sklearn
from scipy import optimize
from scipy import signal
from scipy import interpolate
from scipy.optimize import leastsq
from io import StringIO
from matplotlib import gridspec
from  matplotlib import rc
from  matplotlib import cm
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

###################### Load data ################################################


energy_file = pd.read_csv('data/interpolation120file')

#################################################################################

ncols, nrows = 2,2

gs = matplotlib.gridspec.GridSpec(nrows,ncols)
plt.figure(figsize=(ncols*7,nrows*4.5))

ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])
lines=['-', 'dotted', 'dashdot']

for j,i  in enumerate([['(0.1, 0.6)', 60], ['(0.1, 1.2)', 120], ['(0.1, 2.0)', 200]]):
    k = 0
    ax=plt.subplot(gs[k])
    ax.set_title(r'$t_{\rm exp}=10~{\rm ms}$', fontsize = 15)
    ax.set_ylabel('Intensity (a.u.)', fontsize = 17)
    ax.set_xlim([-90, 90])
    ax.set_yticks([])
    ax.set_xticks([-80, -40, 0, 40, 80])
    ax.set_xlabel('Energy loss (meV)', fontsize = 15)
    ax.tick_params(which='major',direction='in',length=10, labelsize=11)
    ax.tick_params(which='minor',length=10, labelsize=11)
    
    lab = r"$E_b=$"+str(i[1])+" keV"
    
    ax.plot(energy_file['x'], energy_file['mean%(i)s'%{"i": i[0]}], linestyle=lines[j], linewidth = 2, label=lab)
    ax.fill_between(energy_file['x'], energy_file['up%(i)s'%{"i": i[0]}], \
                    energy_file['down%(i)s'%{"i": i[0]}], alpha=.3)
    ax.legend(fontsize = 12)
    
for j,i  in enumerate([['(1.0, 0.6)', 60], ['(1.0, 1.2)', 120], ['(1.0, 2.0)', 200]]):
    k = 1
    ax=plt.subplot(gs[k])
    ax.set_title(r'$t_{\rm exp}=100~{\rm ms}$', fontsize = 15)
        #ax.set_ylim([0, 1])
    lab = r"$E_b=$"+str(i[1])+" keV"
    
    ax.set_xlim([-90, 90])
    ax.set_yticks([])
    ax.set_xticks([-80, -40, 0, 40, 80])
    ax.set_xlabel('Energy loss (meV)', fontsize = 15)
    ax.tick_params(which='major',direction='in',length=10, labelsize=11)
    ax.tick_params(which='minor',length=10, labelsize=11)
    
    ax.plot(energy_file['x'], energy_file['mean%(i)s'%{"i": i[0]}], linestyle=lines[j], linewidth = 2, label=lab)
    ax.fill_between(energy_file['x'], energy_file['up%(i)s'%{"i": i[0]}], \
                    energy_file['down%(i)s'%{"i": i[0]}], alpha=.3)
    ax.legend(fontsize = 12)



for j,i  in enumerate([['(0.1, 0.6)', 60], ['(0.1, 1.2)', 120], ['(0.1, 2.0)', 200]]):
    k = 0
    ax=plt.subplot(gs[2])
    ax.set_title(r'$t_{\rm exp}=10~{\rm ms}$', fontsize = 15)
    ax.set_ylabel('relative uncertainty', fontsize = 17)
    ax.set_ylim(0.2,2)
    ax.set_xlim([-90, 90])
    #ax.set_yscale("log")
    #ax.set_yticks([])
    ax.set_xticks([-80, -40, 0, 40, 80])
    ax.set_xlabel('Energy loss (meV)', fontsize = 15)
    ax.tick_params(which='major',direction='in',length=10, labelsize=11)
    ax.tick_params(which='minor',length=10, labelsize=11)
    
    lab = r"$E_b=$"+str(i[1])+" keV"
    
    ax.plot(energy_file['x'], energy_file['mean%(i)s'%{"i": i[0]}]/energy_file['mean%(i)s'%{"i": i[0]}], linestyle=lines[j], linewidth = 2, label=lab)
    ax.fill_between(energy_file['x'], energy_file['up%(i)s'%{"i": i[0]}]/energy_file['mean%(i)s'%{"i": i[0]}], \
                    energy_file['down%(i)s'%{"i": i[0]}]/energy_file['mean%(i)s'%{"i": i[0]}], alpha=.3)

for j,i  in enumerate([['(1.0, 0.6)', 60], ['(1.0, 1.2)', 120], ['(1.0, 2.0)', 200]]):
    k = 1
    ax=plt.subplot(gs[3])
    ax.set_title(r'$t_{\rm exp}=100~{\rm ms}$', fontsize = 15)
        #ax.set_ylim([0, 1])
    lab = r"$E_b=$"+str(i[1])+" keV"

    ax.set_ylim(0.2,2)
    ax.set_xlim([-90, 90])
    #ax.set_yticks([])
    ax.set_xticks([-80, -40, 0, 40, 80])
    ax.set_xlabel('Energy loss (meV)', fontsize = 15)
    ax.tick_params(which='major',direction='in',length=10, labelsize=11)
    ax.tick_params(which='minor',length=10, labelsize=11)
    
    ax.plot(energy_file['x'], energy_file['mean%(i)s'%{"i": i[0]}]/energy_file['mean%(i)s'%{"i": i[0]}], linestyle=lines[j], linewidth = 2, label=lab)
    ax.fill_between(energy_file['x'], energy_file['up%(i)s'%{"i": i[0]}]/energy_file['mean%(i)s'%{"i": i[0]}], \
                    energy_file['down%(i)s'%{"i": i[0]}]/energy_file['mean%(i)s'%{"i": i[0]}], alpha=.3)
    ax.legend(fontsize = 12)


    
plt.tight_layout()
plt.savefig('../plots/deltaE_dependence_vacuum.pdf')
print("Saved figure = ../plots/deltaE_dependence_vacuum.pdf")



