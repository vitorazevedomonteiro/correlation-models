"""
Created by Vitor Monteiro, 23/09/2025

Compute correlation and spatial correlation coefficients for Sa(T) and PGA, for
Californian earthquakes for periods between [0.1-3.0]s.

For more details please see: 
Goda, K., & Hong, H. P. (2008). Spatial Correlation of Peak Ground Motions and Response Spectra.
Bulletin of the Seismological Society of America, 98(1), 354–365. https://doi.org/10.1785/0120070078
"""


import numpy as np

def SpatialCorrGH08_SA(h, t, uncertainty='yes'):
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

def SpatialcorrGH08_PGA(h, uncertainty='yes'):
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


# Auxiliar correlation model for a Cross-Spatial correlation model calculated using Markov method
def corrBC06xy(T_a, T_b):

    T_min, T_max = min(T_a, T_b), max(T_a, T_b)

    I_Tmin = 1 if T_min < 0.189 else 0
    log_ratio = np.log(T_max / T_min)

    inner_term = (np.pi / 2) - (0.359 + 0.163 * I_Tmin *
                                np.log(T_min / 0.189)) * log_ratio
    inner_term = np.clip(inner_term, -np.pi, np.pi)

    rho = (0.79 - 0.023 * np.log(np.sqrt(T_b*T_a))) * (1 - np.cos(inner_term))
    return rho  


def SpatialCrossCorrGH08(t1, t2, h):
    if not (0.1 <= t1 <= 3.0):
        raise ValueError(f"t = {t1} is outside the valid range [0.1, 3.0].")
    if not (0.1 <= t2 <= 3.0):
        raise ValueError(f"t = {t2} is outside the valid range [0.1, 3.0].")
    
    t_max = max(t1, t2)
    rho = corrBC06xy(t1, t2) * SpatialCorrGH08_SA(h, t_max)

    return rho





