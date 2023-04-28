# -*- coding: utf-8 -*-

import importlib
import numpy as np
from matplotlib import pyplot as plt
import functions as fn
import parameters

#%%
"C VALUES FOR SIMULATION"
c_vals = [ 1 ,   1.95,  2.45,  3.1   ]
newSim = [False, False, False, False ]
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
        
    "PLOT OPTIONS"
    golden  = np.sqrt(2)
    scale = 3
    linWidth = 2.5
    opac = .75
    
    "lOAD PLOT DATA"
    env_array = np.load('../DATA/envData'+simTag+'.npy')
    adap_array = np.load('../DATA/adapData'+simTag+'.npy')
    "MAKE FIGS"
    fig1 = plt.figure(figsize=(scale*golden,scale))
    ax1 = fig1.add_subplot(111)
    ax1.plot(adap_array,label='Adaptation',color='k', linewidth = linWidth,alpha=opac)
    ax1.plot(env_array,label='Environment',color='#005745', linewidth = linWidth,alpha = opac)
    ax1.set_ylabel('Environmental state, $x$')
    ax1.set_xlabel('Time')
    ax1.set_ylim((-.05,20.05))
    ax1.legend(loc='upper right')
    t_start = 0;
    t_end = np.min((2000,params_dict['NUMSTEPS']));
    ax1.set_xlim(t_start,t_end);

    
    "SAVE FIGS"
    save = False
    if save == True:
        fig1.savefig("../FIGS/dynamics_"+simTag+".pdf",bbox_inches='tight', dpi=150)
        fig1.savefig("../FIGS/dynamics_"+simTag+".png", bbox_inches='tight',dpi=150)