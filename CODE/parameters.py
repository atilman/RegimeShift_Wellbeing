# -*- coding: utf-8 -*-

import numpy as np

" MODEL PARAMETERS"

"SIMULATION PARAMS"
dt = 1 # time step (year)
NUMYEARS = 300000
NUMSTEPS = int(NUMYEARS/dt) # number of steps to run 

###! Demographic parameters
r = 1
K = 10
h = 1 #half saturation constant for type 3 fn response

###! white noise (drawn from a Gaussian distribution)
mu = 0
sigma = 0.0

###! red noise parameters
i0 = 0.01# initial red noise
mu_i = 0 #mean red noise
beta = 0.07 #variance red noise
T = 30/dt #timescale of red noise


###! adaptation parameters
y0 = 5 #initial adaptation state
l = .01 # learning rate \in [0,1]
a = 3 # importance of adaptation (range of reasonable outcomes)
m = 5 
n = 1/2 #pi(x) = m + n*x

###! Transformation parameters
m_tr = 23/4
n_tr = 1/10
a_tr = 5


###PARAMETER SWEEP SIMULATION
x0 = 6
l_low = .001
l_mid = .01
l_high = .1
c_sweep = np.linspace(0.25,3.5,100)
c = 1

params_dict = {'dt':dt,
        'INIT_X':x0,
        'NUMSTEPS': NUMSTEPS, 
        'r': r, 
        'K': K,
        'c': c,
        'c_sweep':c_sweep,
        'h': h,
        'mu': mu,
        'sigma': sigma,
        'i0':i0,
        'mu_i':mu_i,
        'T':T,
        'beta':beta,
        'y0':y0,
        'l_low': l_low,
        'l_mid': l_mid,
        'l_high': l_high,
        'a':a,
        'm':m,
        'n':n,
        'm_tr':m_tr,
        'n_tr':n_tr,
        'a_tr':a_tr
         }