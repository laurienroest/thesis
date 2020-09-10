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
from scipy.interpolate import UnivariateSpline
from matplotlib import gridspec
from  matplotlib import rc
from  matplotlib import cm
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

###################### Load data ################################################

energy_file_full = pd.read_csv('data/prediction_120keV_full')
energy_file_cut = pd.read_csv('data/prediction_120keV_cut')
energy_file_cut_big = pd.read_csv('data/Energy_extrapolation_cut_big')


hfont = rc('font',**{'family':'sans-serif','sans-serif':['Sans Serif']})

groups_full = energy_file_full.groupby(['time', 'energy'])
groups_cut = energy_file_cut.groupby(['time', 'energy'])
groups_cut_big  = energy_file_cut_big.groupby(['time', 'energy'])
ncols, nrows = 1,1

gs = matplotlib.gridspec.GridSpec(nrows,ncols)
plt.figure(figsize=(ncols*6,nrows*4))
ax = plt.subplot(gs[0])


rescolors = plt.rcParams['axes.prop_cycle'].by_key()['color']

for name, group in groups_cut_big:
    mean_prediction = group.iloc[:, 4:].mean(axis=1).to_numpy()
    std_prediction = group.iloc[:, 4:].std(axis=1).to_numpy()
    
    if group['time'].max() == 1 and group['energy'].max() == 2:
        p3=ax.plot(group.x*1000, np.divide(mean_prediction, mean_prediction), label='with data cut at 50meV',color=rescolors[2],ls="dotted")
        p3a=ax.fill_between(group.x*1000, np.divide(mean_prediction + std_prediction, mean_prediction), \
                        np.divide(mean_prediction - std_prediction, mean_prediction), alpha=.3,color=rescolors[2])     
        
for name, group in groups_full:
    mean_prediction = group.iloc[:, 4:].mean(axis=1).to_numpy()
    std_prediction = group.iloc[:, 4:].std(axis=1).to_numpy()
    
    if group['time'].max() == 1 and group['energy'].max() == 2:
        p1=ax.plot(group.x*1000, np.divide(mean_prediction, mean_prediction),color=rescolors[1])
        p1a=ax.fill_between(group.x*1000, np.divide(mean_prediction + std_prediction, mean_prediction), \
                        np.divide(mean_prediction - std_prediction, mean_prediction), alpha=.3,color=rescolors[1])  


for name, group in groups_cut:
    mean_prediction = group.iloc[:, 4:].mean(axis=1).to_numpy()
    std_prediction = group.iloc[:, 4:].std(axis=1).to_numpy()
    
    if group['time'].max() == 1 and group['energy'].max() == 2:
        p2=ax.plot(group.x*1000, np.divide(mean_prediction, mean_prediction), label='with data cut at 100meV',color=rescolors[0],ls="dashed")
        p2a=ax.fill_between(group.x*1000, np.divide(mean_prediction + std_prediction, mean_prediction), \
                        np.divide(mean_prediction - std_prediction, mean_prediction), alpha=.3,color=rescolors[0])
        
ax.axvline(x=50, linestyle='dashdot', color='black') 
ax.axvline(x=100, linestyle='dashdot', color='black') 
ax.axvline(x=800, linestyle='dashdot', color='black')
ax.set_ylabel(r'relative uncertainty in $I_{\rm EEL}(\Delta E)$', fontsize = 13)
ax.set_title('$t_{exp}$ = 100 ms, $E_b$ = 200 keV', fontsize = 15)
ax.set_xlabel('Energy loss (meV)', fontsize = 15)  
ax.set_xlim([10, 1.1e3])
ax.set_ylim([0.90, 1.15])
ax.set_xscale("log")
ax.tick_params(which='major',direction='in',length=5, labelsize=12)
ax.tick_params(which='minor',direction='in',length=5, labelsize=12)


ax.legend([(p1[0],p1a),(p2[0],p2a),(p3[0],p3a) ],[r"no $\Delta E_{\rm cut}$ cut",r"$\Delta E_{\rm cut}=100$ meV",r"$\Delta E_{\rm cut}=50$ meV"], frameon=True,loc=[0.53,0.74],prop={'size':11})


plt.tight_layout()

plt.savefig('../plots/prediction_with_cut_100ms.pdf')
print("saved fig = ../plots/prediction_with_cut_100ms.pdf")

