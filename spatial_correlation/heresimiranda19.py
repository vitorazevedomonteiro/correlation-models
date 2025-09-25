"""
Created by Vitor Monteiro, 23/09/2025

Compute spatial correlation coefficients for Sa(T) and PGA for
NGA-West2 for periods between [0.1-6.0]s.

For more details please see: 
Heresi, P., & Miranda, E. (2019). Uncertainty in intraevent spatial
correlation of elastic pseudo-acceleration spectral ordinates.
Bulletin of Earthquake Engineering, 17(3), 1099–1115. https://doi.org/10.1007/s10518-018-0506-6
"""

import numpy as np
from openquake.hazardlib.correlation import hmcorrelation

def SpatialCorrHM19(T, h, uncertainty=0):
    # use T=0 for PGA
     
    if T < 1.37:
        median = 4.231 * T * T - 5.180 * T + 13.392
    else:
        median = 0.140 * T * T - 2.249 * T + 17.050

    Stdev = (4.63e-3 * T * T + 0.028 * T + 0.713)

    if uncertainty == 0:
        beta = median
    else:
        beta = np.random.lognormal(
            np.log(median), Stdev * uncertainty)

    corr = np.exp(-(h / beta)**0.55)
    
    return corr

