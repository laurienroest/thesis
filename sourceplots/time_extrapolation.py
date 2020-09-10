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

fwhmvalues_mean_200 = np.loadtxt('data/fwhmvalues_time_mean_2.0')
fwhmvalues_mean_60 = np.loadtxt('data/fwhmvalues_time_mean_0.6')
up200 = np.loadtxt('data/fwhmvalues_time_up_2.0')
up60 = np.loadtxt('data/fwhmvalues_time_up_0.6')
low200 = np.loadtxt('data/fwhmvalues_time_down_2.0')
low60 = np.loadtxt('data/fwhmvalues_time_down_0.6')


################################################################################

def smooth(x, window_len, window='hanning'):
    s=np.r_[x[window_len-1:0:-1],x,x[-2:-window_len-1:-1]]

    if window == 'flat': 
        w=np.ones(window_len,'d')
    else:
        w=eval('np.'+window+'(window_len)')

    y=np.convolve(w/w.sum(),s,mode='valid')
    index = int(window_len/2)
    return y[(index-1):-(index)]

################################################################################





hfont = rc('font',**{'family':'sans-serif','sans-serif':['Sans Serif']})

nrows, ncols = 1,1

gs = matplotlib.gridspec.GridSpec(nrows,ncols)
wl = 4
color1 = 'red'
color2 = 'orange'

rescolors = plt.rcParams['axes.prop_cycle'].by_key()['color']

plt.figure(figsize=(ncols*5,nrows*3.5))

ax = plt.subplot(gs[0])
ax.plot(np.linspace(0,200,21), smooth(fwhmvalues_mean_60 * 1000, wl*2), color=rescolors[1], label = r'$E_b=60$ keV',ls="dashed")
ax.fill_between(np.linspace(0,200,21), smooth(up60 * 1000, wl*2), smooth(low60 * 1000, wl), color=rescolors[1], alpha=.2, label = r'$E_b=60$ keV',ls="dashed")
ax.plot(np.linspace(0,200,21), smooth(fwhmvalues_mean_200 * 1000, wl), color = rescolors[0], label  = r'$E_b=200$ keV')
ax.fill_between(np.linspace(0,200,21), smooth(up200 * 1000, wl), smooth(low200 * 1000, wl), color = rescolors[0], alpha=.2, label = r'$E_b=200$ keV')
ax.axvline(x=10, linestyle='dotted', color='k')
ax.axvline(x=100, linestyle='dotted', color='k')
ax.tick_params(which='major',direction='in',length=7, labelsize=11)
ax.tick_params(which='minor',length=8, labelsize=11)
ax.set_yticks([30, 40, 50, 60, 70, 80])
ax.set_ylabel('FWHM (meV)', fontsize = 15)
ax.set_xlim([0, 200])
#ax.set_ylim([10,44])
ax.set_xlabel(r'$t_{\rm exp}$ (ms)', fontsize = 15)
lables, handles = ax.get_legend_handles_labels() 
ax.legend([(lables[0], lables[2]), (lables[1], lables[3])], [(handles[0]), handles[1]], loc='upper center', fontsize=13)

plt.tight_layout()
plt.savefig('../plots/time_extrapolation.pdf')
print("Saved fig = ../plots/time_extrapolation.pdf")
