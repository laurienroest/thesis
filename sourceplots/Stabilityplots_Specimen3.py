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


########## def smooth function ##########################
def smooth(x, window_len, window='hanning'):
    s=np.r_[x[window_len-1:0:-1],x,x[-2:-window_len-1:-1]]

    if window == 'flat': 
        w=np.ones(window_len,'d')
    else:
        w=eval('np.'+window+'(window_len)')

    y=np.convolve(w/w.sum(),s,mode='valid')
    index = int(window_len/2)
    return y[(index-1):-(index)]


########## Load data ####################################

fnamebase = 'data/'
plot_bvalues = pd.read_csv(fnamebase + 'bvalues_specimen3.csv', usecols=range(1,28))
plot_bgvalues = pd.read_csv(fnamebase + 'bgvalues_specimen3.csv', usecols=range(1,28))

arr = np.arange(len(plot_bgvalues.columns)) % 3

df_bandgaps = plot_bvalues.iloc[:, arr == 0].to_numpy()
df_high = plot_bvalues.iloc[:, arr == 1].to_numpy()
df_low = plot_bvalues.iloc[:, arr == 2].to_numpy()

bg_bandgaps = plot_bgvalues.iloc[:, arr == 0].to_numpy()
bg_high = plot_bgvalues.iloc[:, arr == 1].to_numpy()
bg_low = plot_bgvalues.iloc[:, arr == 2].to_numpy()

# DeltaE1 array
dE1_array = [1.05, 1.15, 1.25, 1.35, 1.45, 1.55, 1.65, 1.75, 1.95]

print(bg_bandgaps[0])
l=len(bg_bandgaps[0])
print("\n *** bandgap values ***")

for i in range(l):
    print(dE1_array[i], '%6.2f' % bg_bandgaps[0,i],\
          '%6.2f' % (bg_high[0,i]-bg_bandgaps[0,i]), \
          '%6.2f' % (bg_low[0,i]-bg_bandgaps[0,i]) )

l=len(df_bandgaps[0])
print("\n *** b exponent values ***")
for i in range(l):
    print(dE1_array[i], '%6.2f' % df_bandgaps[0,i],\
          '%6.2f' % (df_high[0,i]-df_bandgaps[0,i]), \
          '%6.2f' % (df_low[0,i]-df_bandgaps[0,i]) )

########################################################################
########################################################################

nrows, ncols = 1,2
gs = matplotlib.gridspec.GridSpec(nrows,ncols)
plt.figure(figsize=(ncols*7,nrows*5))
meanmean=[]

cm_subsection = np.linspace(0,1,14) 
colors = [cm.viridis(x) for x in cm_subsection]
hfont = rc('font',**{'family':'sans-serif','sans-serif':['Sans Serif']})

label1 = 'Median'
label2 = '68% CL'
wl = 4

plt.title('Spectrum 14', fontsize=20)

mins = 0
maxs = mins + 2

for i in range(mins, maxs):
    ax = plt.subplot(gs[i-mins])
   
    ax.set_xlim([1.2, 1.6])
    
    ax.tick_params(labelbottom=True)
    ax.tick_params(which='major', direction='in', length= 10, labelsize=14)
    
    if i == mins:
        ax.set_ylim([-.1, 1.6])
        ax.set_yticks([0, .5, 1, 1.5, 2])
        ax.set_xlabel(r'$\Delta E_{\rm I}$ (eV)', fontsize=22)
        ax.set_ylabel(r'$b$', fontsize=22)
        
        ax.plot(dE1_array, smooth(df_bandgaps[i], wl), '--', color='steelblue', label=label1)
        ax.plot(dE1_array, smooth(df_high[i], wl), '-', color='steelblue',label=label2)
        ax.plot(dE1_array, smooth(df_low[i], wl), '-', color='steelblue', label=label2)
        ax.fill_between(dE1_array, smooth(df_high[i], wl), smooth(df_low[i], wl), color='steelblue', alpha=.2, label=label2)
        ax.axvline(x=1.4, linestyle='dashdot', color='black')
        ax.set_ylim([-.1, 1.4])
        
    if i == mins+1:
        ax.set_ylim([2, 3])
        ax.plot(dE1_array, smooth(bg_bandgaps[i-1], wl), '--', color='steelblue', label=label1)
        ax.plot(dE1_array, smooth(bg_high[i-1], wl), '-', color='steelblue', label = label2)
        ax.plot(dE1_array, smooth(bg_low[i-1], wl), '-', color='steelblue', label = label2)
        ax.fill_between(dE1_array, smooth(bg_high[i-1], wl), smooth(bg_low[i-1], wl), \
                    color='steelblue', alpha=.2, label=label2)
        ax.set_yticks([.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5])
        ax.set_ylabel(r'$E_{\rm BG}$ (eV)', fontsize=22)
        ax.set_xlabel(r'$\Delta E_{\rm I}$ (eV)', fontsize=22)
        ax.set_ylim([0.8, 1.4])
        ax.axvline(x=1.4, linestyle='dashdot', color='black')
    
    handles, labels = ax.get_legend_handles_labels()
    ax.legend((handles[0], (handles[1], handles[2], handles[3])), (labels[0], labels[1]), \
                  loc = 'upper left', fontsize=17)
    
plt.tight_layout()
plt.savefig('../plots/Stabilityplots_sp4.pdf')
print("Saved fig = ../plots/Stabilityplots_sp4.pdf")
