"""
Created by Vitor Monteiro, 23/09/2025

Compute spatial correlation coefficients for PGA and PGV
for Japanese earthquakes.

For more details please see: 
Sokolov, V., & Wenzel, F. (2013). 
Further analysis of the influence of site conditions and earthquake 
magnitude on ground-motion within-earthquake correlation: analysis of 
PGA and PGV data from the K-NET and the KiK-net (Japan) networks. 
Bulletin of Earthquake Engineering, 11(6), 1909–1926. https://doi.org/10.1007/s10518-013-9493-9
"""

import numpy as np

def SpatialCorrSW13(h, im):
    if im == 'PGA':
        b = 0.7156
        a = -0.0856
        rho = np.exp(a*(h**b))
        return rho
    elif im == 'PGV':
        b = 0.784
        a = -0.0837
        rho = np.exp(a*(h**b))
        return rho


