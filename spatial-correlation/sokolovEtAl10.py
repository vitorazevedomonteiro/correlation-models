"""
Created by Vitor Monteiro, 23/09/2025

Compute spatial correlation coefficients for PGA for
Taiwanese earthquakes.

For more details please see: 
Sokolov, V., Wenzel, F., Jean, W.-Y., & Wen, K.-L. (2010). 
Uncertainty and Spatial Correlation of Earthquake Ground Motion in Taiwan. 
Terrestrial, Atmospheric and Oceanic Sciences, 21(6), 905. 
https://doi.org/10.3319/TAO.2010.05.03.01(T)
"""

import numpy as np

def SpatialcorrS10(h):
    """
    The parameters a and b are selected from Table 5 correspondent 
    to 'all data' after the correction.
    """
    a = -0.586
    b = 0.306
    rho = np.exp(a*(h**b))
    return rho
