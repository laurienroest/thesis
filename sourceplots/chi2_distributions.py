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
chi_data = pd.read_csv('data/chi_data_vacuum')

####################
fig, ax = plt.subplots((1))
fig.set_size_inches((7.5,5))

plt.title('$\chi^2$ distribution (vacuum spectra)', fontsize=20)
plt.xlabel('$\chi^2$', fontsize=16)
plt.xlim([0.3, 2.5])

rescolors = plt.rcParams['axes.prop_cycle'].by_key()['color']

plt.hist(chi_data['train'], density=True, bins=30, range=[0.5, 3], alpha=0.7, label='training',histtype=u'step',lw=2.5,color=rescolors[0],fill=True,ec='darkslateblue')
plt.hist(chi_data['val'], density=True, bins=30, range=[0.5, 3], alpha=0.7, label='validation',histtype=u'step',lw=2.5,color=rescolors[1],fill=True,ec='chocolate')
plt.legend(fontsize=18)
#plt.ylabel('Occurence', fontsize=16)
ax.tick_params(which='major',direction='in',length=10, labelsize=16)

plt.tight_layout()
plt.savefig('../plots/chi2_distributions.pdf')
print("Saved plot = ../plots/chi2_distributions.pdf")
