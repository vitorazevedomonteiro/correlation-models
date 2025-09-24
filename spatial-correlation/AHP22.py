"""
Created by Vitor Monteiro, 23/09/2025

Compute spatial correlation coefficients for Sa(T) and PGA for
Chilean earthquakes for periods between [0.0-10.0]s.

For more details please see: 
Aldea, S., Heresi, P., & Pastén, C. (2022). 
Within‐event spatial correlation of peak ground acceleration and spectral 
pseudo‐acceleration ordinates in the Chilean subduction zone. 
Earthquake Engineering & Structural Dynamics, 51(11), 2575–2590. https://doi.org/10.1002/eqe.3674
"""

import numpy as np

def SpatialCrossAHP22(T, h):
    # use T=0 for PGA
    
    if T <= 0.40:
        b = 14.400 - 17.00 * T
    elif 0.40 < T <= 0.75:
        b = 14.743 + 7.795 * np.log(T)
    elif 0.75 < T <= 3.00:
        b = 12.500
    else:
        b = 5.063 + 6.769 * np.log(T)

    rho = np.exp(-(h/b) ** 0.59)

    return rho
