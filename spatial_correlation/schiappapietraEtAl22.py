"""
Created by Vitor Monteiro, 23/09/2025

Compute spatial correlation coefficients for Sa(T) and PGA for
different regions in Italy for periods between [0.0-2.0]s.

For more details please see: 
Schiappapietra, E., Stripajová, S., Pažák, P., Douglas, J., & Trendafiloski, G. (2022).
Exploring the impact of spatial correlations of earthquake ground motions in
the catastrophe modelling process: a case study for Italy.
Bulletin of Earthquake Engineering, 20(11), 5747–5773. https://doi.org/10.1007/s10518-022-01413-z
"""

import numpy as np

def SpatialcorrS22_N(T, h): # north region
    # for PGA use T=0
    if T <= 0.55:
        b = 27.48 - 52.20 * (T-0.55)
    else:
        b = 27.48 + 15.81 * (T-0.55)
    
    return np.exp(-(3*h)/b)

def SpatialcorrS22_C(T, h): # center region
    # for PGA use T=0
    
    if T <= 1.0:
        b = 17.87 - 8.52 * (T-1.0)
    else:
        b = 17.87 + 7.85 * (T-1.0)
    
    return np.exp(-(3*h)/b)

def SpatialcorrS22_S(T, h): # south region
    # for PGA use T=0
    
    b = 23.25 - 5.44 * T
    
    return np.exp(-(3*h)/b)
