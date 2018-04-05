# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 22:42:28 2018

@author: Arthurim
"""

import numpy as np
import numpy.random as npr

def cost(x, l=1):
    return l*x^2

def U(x, gamma=0.5):
    return -np.exp(-gamma*x)

def almgrenchriss(q0, S0, sigma, V, T, N, k):
    
    """
    Discrete time implementation of the Almgren Chriss algo
    
    Parameters:
    - T is the period the trader has to unwind
    - N is the discretization step
    - q0 is the quantity the trader has to unwind (q0>0 he has to sell, q0<0 he has to buy)
    - S0 is the initial stock price
    - sigma is the initial vol
    - k is the magnitude of the permanent market impact
    - V is a vector of market volume
    """
    
    
    dt = T/N
    
    q = np.zeros(N)
    S = np.zeros(N)
    v = np.zeros(N)
    X = np.zeros(N)
    
    q[0] = q0
    S[0] = S0
    
    for i in range(N):
        v[i+1] = ?
        q[i+1] = q[i] + v[i+1]*dt
        S[i+1] = S[i] + sigma * np.sqrt(dt) * npr.rand() + k*v[i+1]*dt
        X[i+1] = X[i] - v[i+1] *S[i]  *dt - cost(v[i+1]/V[i+1]) *V[i+1]*dt 
        
        
        
        
        
        
        
        
        
        
        
        
        
        