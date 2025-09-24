"""
Created by Vitor Monteiro, 23/09/2025

Compute correlation coefficients for Sa(T), for ESM database for
a single horizontal orientation (x-x) for periods between [0.05-2.5]s.

For more details please see: 
Cimellaro, G. P. (2013). Correlation in spectral accelerations for earthquakes in Europe.
Earthquake Engineering & Structural Dynamics, 42(4), 623–633. https://doi.org/10.1002/eqe.2248
"""

import numpy as np

def corrC13(T1, T2):
    
    T_min, T_max = min(T1, T2), max(T1, T2)  # Ensure correct assignment
    rho = 1 - ((-0.0798+0.0431*np.log10(T_min)+0.0153*(np.log10(T_max))**2) /
               (1+0.1147*np.log10(T_max)-0.3502*(np.log10(T_min))**2)) * np.log(T_min/T_max)
    return rho  



