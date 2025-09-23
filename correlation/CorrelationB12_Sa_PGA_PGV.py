"""
Created by Vitor Monteiro, 23/09/2025

Compute cross-correlation coefficients between Sa(T)-PGA and Sa(T)-PGV
for NGA-W1 database database for periods between [0.01-10.0]s.

For more details please see: 
Bradley, B. A. (2012). 
Empirical Correlations between Peak Ground Velocity and Spectrum-Based Intensity Measures. 
Earthquake Spectra, 28(1), 17–35. https://doi.org/10.1193/1.3675582
"""

import numpy as np

def corrB12(T, im = 'PGA'):
    if not (0.01 <= T <= 10.0):
        raise ValueError(f"T = {T} is outside the valid range [0.01, 10.0]")
    
    if im == 'PGA': # default
        if 0.01 <= T < 0.2:
            rho = ((1.00+0.895)/2)-((1.00-0.895)/2)*np.tanh(1.6*np.log(T/0.06))
        elif 0.2 <= T < 10:
            rho = ((0.97+0.25)/2)-((0.97-0.25)/2)*np.tanh(0.8*np.log(T/0.80))
        else:
            rho = np.nan
        return rho
    
    elif im == 'PGV':    
        if 0.01 <= T < 0.1:
            rho = ((0.73+0.54)/2)-((0.73-0.54)/2)*np.tanh(1.8*np.log(T/0.045))
        elif 0.1 <= T < 0.75:
            rho = ((0.54+0.81)/2)-((0.54-0.81)/2)*np.tanh(1.5*np.log(T/0.28))
        elif 0.75 <= T < 2.5:
            rho = ((0.80+0.76)/2)-((0.80-0.76)/2)*np.tanh(3.0*np.log(T/1.1))
        else:
            rho = ((0.76+0.70)/2)-((0.76-0.70)/2)*np.tanh(3.2*np.log(T/5.0))
        return rho 
          