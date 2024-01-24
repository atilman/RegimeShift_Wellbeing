# -*- coding: utf-8 -*-

import importlib
import numpy as np
from matplotlib import pyplot as plt
import functions as fn
import parameters
# plt.rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica']})
# plt.rc('text', usetex=True)
#%%
"C VALUES FOR SIMULATION"
c_vals = [ 1 ,   1.95,  2.45,  3.1   ]
newSim = [False, False, False, False ]
"PLOT OPTIONS"
golden  = np.sqrt(2)
scale = 6
linWidth = 2.5
opac = .75
fig1 = plt.figure(figsize=(scale*golden,scale))
ax1 = fig1.add_subplot(221)
ax2 = fig1.add_subplot(222)
ax3 = fig1.add_subplot(223)
ax4 = fig1.add_subplot(224)
AX = [ax1,ax2,ax3,ax4]
"RUN SIMULATIONS ONLY FOR CASES MARKED TRUE ABOVE"
for i in range(len(c_vals)):
    importlib.reload(parameters)
    from parameters import params_dict
    x0 = params_dict['INIT_X']
    params_dict['c'] = c_vals[i]
    simTag = str(c_vals[i]).replace('.','')
    if newSim[i] == True:
        x_array, i_array, y_array, util_array, pi_array = fn.run_model_flickering(x0,params_dict)
        np.save('../DATA/envData'+simTag,x_array)
        np.save('../DATA/adapData'+simTag,y_array)
        
    
    
    "lOAD PLOT DATA"
    env_array = np.load('../DATA/envData'+simTag+'.npy')
    adap_array = np.load('../DATA/adapData'+simTag+'.npy')
    "MAKE FIGS"

    AX[i].plot(adap_array,label='Adaptation',color='k', linewidth = linWidth,alpha=opac)
    AX[i].plot(env_array,label='Environment',color='#005745', linewidth = linWidth,alpha = opac)
    AX[i].set_ylabel('Environmental state, $x$')
    AX[i].set_xlabel('Time')
    AX[i].set_ylim((-.05,20.05))
    
    t_start = 0;
    t_end = np.min((2000,params_dict['NUMSTEPS']));
    AX[i].set_xlim(t_start,t_end);
ax4.legend(loc='upper right')

fig1.text(0.07, .87, 'a',weight='bold', fontsize = 16)
fig1.text(.495, .87, 'b', weight='bold',fontsize = 16)
fig1.text(.07, .46, 'c', weight='bold',fontsize = 16) 
fig1.text(.495, .46, 'd', weight='bold',fontsize = 16)
"SAVE FIGS"
save = False
if save == True:
    fig1.savefig("../FIGS/dynamics.pdf",bbox_inches='tight')
    fig1.savefig("../FIGS/dynamics.png", bbox_inches='tight',dpi=1500)