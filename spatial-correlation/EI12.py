"""
Created by Vitor Monteiro, 23/09/2025

Compute spatial correlation coefficients for Sa(T)
for ESD database and ITACA database for periods between [0.1-2.0]s.

For more details please see: 
Esposito, S., & Iervolino, I. (2012). 
Spatial Correlation of Spectral Acceleration in European Data. 
Bulletin of the Seismological Society of America, 102(6), 2781–2788. 
https://doi.org/10.1785/0120120068
"""

import numpy as np

# T=0.1s to T=2.85s
def SpatialCorrEI12(T, h, database=1):
    if not (0.1 <= T <= 2.0):
        raise ValueError(f"T = {T} is outside the valid range [0.1, 2.0].")
    
    if database == 1:  # ESD database
        b = 11.7 + 12.7 * T
        rho = np.exp(-(3*h)/b)
        return rho
    elif database == 2: # ITACA database
        b = 8.6 + 11.6 * T
        rho = np.exp(-(3*h)/b)
        return rho
        

