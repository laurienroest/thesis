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
from numpy import linalg as LA
from numpy.linalg import inv
from scipy.interpolate import UnivariateSpline
import matplotlib.pyplot as plt
import os,sys
import lhapdf
import matplotlib.pyplot as py
import shutil
from matplotlib import gridspec
from  matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text',usetex=True)
from pylab import *
#get_ipython().run_line_magic('matplotlib', 'inline')

# Model for ZLP
def IZLP(DeltaE):
    sigma = 0.3 # eV (variance)
    A = 1e10 # normalisation
    izlp = A*math.exp( -DeltaE**2/sigma**2 )
    return izlp

def IZLP_der(DeltaE):
    sigma = 0.3 # eV (variance)
    A = 1e10 # normalisation
    izlp = -2*DeltaE/sigma**2 * IZLP(DeltaE)
    return izlp

# Model for signal
def Isample(DeltaE):
    b = 0.5 # exponent
    Ebg = 1.5 # bandgap energy (eV)
    Bnorm = 0.1
    isample = 0
    if(DeltaE > Ebg):
        isample = Bnorm * ( DeltaE - Ebg)**b
    return isample

def Isample_der(DeltaE):
    b = 0.5 # exponent
    Ebg = 1.5 # bandgap energy (eV)
    Bnorm = 0.1
    isample = 0
    if(DeltaE > Ebg):
        isample = b/(DeltaE-Ebg) * Isample(DeltaE)
    return isample

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(5,3.5))

# Min and max values of the EEL spectra
deltaE_min = -4 # eV, adjust for each spectrum
deltaE_max = 5 # eV, adjust for each spectrum
l=2000
deltaE = np.zeros(l)
EELtot = np.zeros(l)
EELZLP = np.zeros(l)
EELsample = np.zeros(l)
EELtot_der = np.zeros(l)
EELZLP_der = np.zeros(l)
EELsample_der = np.zeros(l)
for i in range(l):
    deltaE[i] = deltaE_min + (deltaE_max-deltaE_min)*(1.0*i)/(l-1.0)
    EELtot[i] = Isample(deltaE[i]) +  IZLP(deltaE[i])
    EELZLP[i] = IZLP(deltaE[i])
    EELsample[i] = Isample(deltaE[i])
    EELtot_der[i] = Isample_der(deltaE[i]) +  IZLP_der(deltaE[i])
    EELZLP_der[i] = IZLP_der(deltaE[i])
    EELsample_der[i] = Isample_der(deltaE[i])


plt.plot(deltaE,EELtot,linewidth=2.5,color="black",label=r"${\rm total}$")
plt.plot(deltaE,EELZLP,linewidth=2.5,color="blue",ls="dashed",label=r"${\rm ZLP}$")
plt.plot(deltaE,EELsample,linewidth=2.5,color="red",ls="dashdot",label=r"${\rm sample}$")


# Now produce the plot        
plt.xlabel(r"${\rm Energy~loss~(eV)}$",fontsize=17)
plt.ylabel(r"${\rm Intensity~(a.u.)}$",fontsize=17)
plt.xlim(1.45,2.0)
plt.ylim(0,0.09)
#plt.grid(True)
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
plt.yticks([])

plt.legend(frameon=True,loc=[0.46,0.67],prop={'size':12.5})

yline_xx=np.array([1.52,1.52])
yline_yy=np.array([-20,1e6])
plt.plot(yline_xx, yline_yy,color='grey',lw=1.9,ls="dotted")

yline_xx=np.array([1.687,1.687])
yline_yy=np.array([-20,1e6])
plt.plot(yline_xx, yline_yy,color='grey',lw=1.9,ls="dotted")

plt.text(1.525,0.0035,r"$\Delta E_I$",fontsize=12)
plt.text(1.635,0.0035,r"$\Delta E_{II}$",fontsize=12)
plt.text(1.475,0.077,r"$I$",fontsize=20)
plt.text(1.6,0.077,r"$II$",fontsize=20)
plt.text(1.9,0.077,r"$III$",fontsize=20)


# Create an inset
inset = fig.add_axes([0.55, 0.25, 0.38, 0.30])  # Fraction of figure size (3, 2.4)
inset.axes.get_xaxis().set_visible(True)
inset.axes.get_yaxis().set_visible(True)
#inset.set_ylabel(r"$d I/d\Delta E$",fontsize=12)
props = dict(boxstyle='round', facecolor='white', alpha=1,lw=0.5)
inset.text(1.60,-1.35,r"$d I/d\Delta E$",fontsize=12,bbox=props)
inset.set_xlim(1.45, 1.7)
inset.set_ylim(-2, 1)
inset.tick_params(which='both',direction='in',labelsize=8,right=True)
inset.tick_params(which='major',length=3)
inset.tick_params(which='minor',length=3)
#inset.set_yticks([])

print(EELtot_der)

inset.plot(deltaE,EELtot_der,linewidth=1.5,color="black",label=r"${\rm total}$")
inset.plot(deltaE,EELZLP_der,linewidth=1.5,color="blue",ls="dashed",label=r"${\rm ZLP}$")
inset.plot(deltaE,EELsample_der,linewidth=1.5,color="red",ls="dashdot",label=r"${\rm sample}$")
inset.grid(True)

plt.tight_layout()
plt.savefig("EELS_toy.pdf")

