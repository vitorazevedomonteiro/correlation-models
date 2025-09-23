"""
Created by Vitor Monteiro, 23/0/2025

Compute correlation coefficients for Sa(T) and PGA, for Californian earthquakes for periods between [0.1-3.0]s.

For more details please see: 
Goda, K., & Hong, H. P. (2008). Spatial Correlation of Peak Ground Motions and Response Spectra.
Bulletin of the Seismological Society of America, 98(1), 354–365. https://doi.org/10.1785/0120070078
"""


import numpy as np

def correlationGH08_SA(t, h, uncertainty='yes'):
    if not (0.1 <= t <= 3.0):
        raise ValueError(f"t = {t} is outside the valid range [0.1, 3.0].")
    
    if uncertainty == 'no':
        alpha = -0.16 * np.log(t) + 0.62
        beta = 0.5
        rho = np.exp(-alpha*(h**beta))
        return rho
    elif uncertainty == 'yes':
        alpha = -0.176 * np.log(t) + 0.68
        beta = 0.44
        rho = np.exp(-alpha*(h**beta))
        return rho
    else:
        print("Error")


def correlationGH08_PGA(h, uncertainty='yes'):
    if uncertainty == 'no':
        alpha = 0.93
        beta = 0.49
        rho = np.exp(-alpha*(h**beta))
        return rho
    elif uncertainty == 'yes':
        alpha = 0.9
        beta = 0.48
        rho = np.exp(-alpha*(h**beta))
        return rho
    else:
        print("Error")
