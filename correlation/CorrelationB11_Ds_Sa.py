"""
Created by Vitor Monteiro, 23/09/2025

Compute cross-correlation coefficients between Sa(T)-Duration
for NGA-W1 database database for periods between [0.01-10.0]s.

For more details please see: 
Bradley, B. A. (2011). 
Correlation of significant duration with amplitude and cumulative
intensity measures and its use in ground motion selection. 
Journal of Earthquake Engineering, 15(6), 809–832. 
https://doi.org/10.1080/13632469.2011.557140
"""

import numpy as np

def corrB11(T, duration='Ds575'):
    if not (0.01 <= T <= 10.0):
        raise ValueError(f"T = {T} is outside the valid range [0.01, 10.0]")
    
    if duration == 'Ds575': # default
        if 0.01 <= T < 0.09:
            rho = -0.45 + (np.log(T / 0.01) / np.log(0.09 / 0.01)) * (-0.39 + 0.45)
        elif 0.09 <= T < 0.3:
            rho = -0.39 + (np.log(T / 0.09) / np.log(0.30 / 0.09)) * (-0.39 + 0.39)
        elif 0.3 <= T < 1.4:
            rho = -0.39 + (np.log(T / 0.30) / np.log(1.4 / 0.3)) * (-0.06 + 0.39)
        elif 1.4 <= T < 6.5:
            rho = -0.06 + (np.log(T / 1.4) / np.log(6.5 / 1.4)) * (0.16 + 0.06)
        else:
            rho = 0.16 + (np.log(T / 6.5) / np.log(10 / 6.50)) * (0.00 - 0.16)
        return rho
    elif duration == 'Ds595':
        if 0.01 <= T < 0.04:
            rho = -0.41 + (np.log(T / 0.01) / np.log(0.04 / 0.01)) * (-0.41 + 0.41)
        elif 0.04 <= T < 0.08:
            rho = -0.41 + (np.log(T / 0.04) / np.log(0.08 / 0.04)) * (-0.38 + 0.41)
        elif 0.08 <= T < 0.26:
            rho = -0.38 + (np.log(T / 0.08) / np.log(0.26 / 0.08)) * (-0.35 + 0.38)
        elif 0.26 <= T < 1.4:
            rho = -0.35 + (np.log(T / 0.26) / np.log(1.4 / 0.26)) * (-0.02 + 0.35)
        elif 1.4 <= T < 6.00:
            rho = -0.02 + (np.log(T / 1.4) / np.log(6.00 / 1.4)) * (0.23 + 0.02)
        else:
            rho = 0.23 + (np.log(T / 6.00) / np.log(10.00 / 6.00)) * (0.02 - 0.23)
        return rho
        