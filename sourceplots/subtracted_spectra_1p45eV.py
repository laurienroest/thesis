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



########## Load data ###############################################

fnamebase = 'data/'
mean_rep = pd.read_csv(fnamebase + 'Subtracted_spectra_1.45.csv')

##############################################################
def smooth(x, window_len, window='hanning'):
    s=np.r_[x[window_len-1:0:-1],x,x[-2:-window_len-1:-1]]

    if window == 'flat': 
        w=np.ones(window_len,'d')
    else:
        w=eval('np.'+window+'(window_len)')

    y=np.convolve(w/w.sum(),s,mode='valid')
    index = int(window_len/2)
    return y[(index-1):-(index)]

##################################################################

nrows, ncols = 1,2
gs = matplotlib.gridspec.GridSpec(nrows,ncols)
plt.figure(figsize=(ncols*5,nrows*3.5))

rescolors = plt.rcParams['axes.prop_cycle'].by_key()['color']
hfont = rc('font',**{'family':'sans-serif','sans-serif':['Sans Serif']})

lines = ['solid', 'dotted', 'dashed', 'dashdot']

nbins = 1861
wl = 4
          
#for i in ([4,5,6,7]):
for i in ([4,5,6]):
    j = i - 4
    ax = plt.subplot(gs[0])
    ax.set_xlim([.8,2.5])
    ax.set_ylim([-1e1,1.5e3])
    ax.set_ylabel('Intensity (a.u.)', fontsize=18)
    ax.set_xlabel('Energy loss (eV)', fontsize=17)
    
    ax.tick_params(which='major',direction='in',length=10, labelsize=13)
    ax.tick_params(which='minor',length=10)
    ax.set_xticks([1, 1.5, 2, 2.5])
    label= '%(i)s'%{"i":str(i)}
    
    p1 = ax.plot(np.linspace(-.3, 9, nbins), smooth(mean_rep['dif%(i)s_median' % {"i": i}], wl), linestyle=lines[j],color=rescolors[j],lw=2, label= 'sp %(i)s'%{"i":i})
    ax.fill_between(np.linspace(-.3, 9, nbins), smooth(mean_rep['dif%(i)s_low'% {"i": i}], wl), smooth(mean_rep['dif%(i)s_high'% {"i": i}], wl), color=rescolors[j], alpha=.2)
    p1b =ax.fill(np.NaN,np.NaN,color=rescolors[j],alpha=0.2)
    ax.set_yticks([])
    ax.legend(loc='upper left', fontsize=15)
    plt.text(1.7,250,r"$\Delta E_{\rm I}=1.45~{\rm eV}$",fontsize=15)


mean_rep = pd.read_csv(fnamebase + 'Subtracted_spectra_1.55.csv')

for i in ([4,5,6]):
    j = i - 4
    ax = plt.subplot(gs[1])
    ax.set_xlim([.8,2.5])
    ax.set_ylim([-1e1,1.5e3])
    # ax.set_ylabel('Intensity (a.u.)', fontsize=17)
    ax.set_xlabel('Energy loss (eV)', fontsize=17)
    
    ax.tick_params(which='major',direction='in',length=10, labelsize=13)
    ax.tick_params(which='minor',length=10)
    ax.set_xticks([1, 1.5, 2, 2.5])
    label= '%(i)s'%{"i":str(i)}
    
    p1 = ax.plot(np.linspace(-.3, 9, nbins), smooth(mean_rep['dif%(i)s_median' % {"i": i}], wl), linestyle=lines[j],color=rescolors[j],lw=2, label= 'sp %(i)s'%{"i":i})
    ax.fill_between(np.linspace(-.3, 9, nbins), smooth(mean_rep['dif%(i)s_low'% {"i": i}], wl), smooth(mean_rep['dif%(i)s_high'% {"i": i}], wl), color=rescolors[j], alpha=.2)
    p1b =ax.fill(np.NaN,np.NaN,color=rescolors[j],alpha=0.2)
    ax.set_yticks([])
    ax.legend(loc='upper left', fontsize=15)
    plt.text(1.7,250,r"$\Delta E_{\rm I}=1.55~{\rm eV}$",fontsize=15)

    
plt.tight_layout()
plt.savefig('../plots/subtracted_spectra_comp.pdf')
print("Saved fig = ../plots/subtracted_spectra_comp.pdf")





####################################################################
####################################################################

