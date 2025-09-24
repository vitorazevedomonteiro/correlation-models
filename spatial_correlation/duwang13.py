"""
Created by Vitor Monteiro, 23/09/2025

Compute spatial correlation coefficients for Sa(T) and PGA 
for NGA-W1 database database for periods between [0.2-5.0]s.

For more details please see: 
Du, W., & Wang, G. (2013). 
Intra-Event Spatial Correlations for Cumulative Absolute Velocity, Arias Intensity, 
and Spectral Accelerations Based on Regional Site Conditions. Bulletin of the Seismological 
Society of America, 103(2A), 1117–1129. https://doi.org/10.1785/0120120185
"""

import numpy as np
from scipy.interpolate import interp1d


periods = np.array([0.2, 0.5, 1.0, 2.0, 5.0])
params = np.array([
    [4.4, 1.1],
    [8.5, 1.1],
    [22.8, 0.8],
    [32.3, 0.5],
    [41.4, 0.4],
])

# Interpolate the parameters
interps = [interp1d(periods, params[:, i], kind='linear', fill_value='extrapolate') 
           for i in range(2)]


def SpatialCorrDW13(t, h, beta_vs30):
    """
    beta_vs30 is the range of Vs30
    """
    
    if t == 0: # PGA
        beta = 7.45 * np.exp(0.07 * beta_vs30)
        rho = np.exp((-3 * h) / beta)
        return rho
    
    else:
        if not (0.2 <= t <= 5.0):
            raise ValueError(f"t = {t} is outside the valid range [0.2, 5.0].")
        
        c1, c2 =[f(t) for f in interps]

        beta = c1 + c2 * beta_vs30
        rho = np.exp((-3 * h) / beta)
        return rho


