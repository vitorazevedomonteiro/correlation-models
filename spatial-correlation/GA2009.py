"""
Created by Vitor Monteiro, 23/09/2025

Compute spatial correlation coefficients for Sa(T), for
Japanese earthquakes for periods between [0.0-5.0]s.

For more details please see: 
Goda, K., & Atkinson, G. M. (2009). Probabilistic Characterization
of Spatially Correlated Response Spectra for Earthquakes in Japan.
Bulletin of the Seismological Society of America, 99(5), 3003–3020.
https://doi.org/10.1785/0120090007
"""


import numpy as np
from scipy.interpolate import interp1d

# Periods and parameters
periods = np.array([0.0, 0.1, 0.2, 0.3, 0.5, 1.0, 2.0, 3.0, 5.0])
params = np.array([
    [0.095, 0.336, 2.60],
    [0.050, 0.308, 5.00],
    [0.162, 0.266, 2.24],
    [0.156, 0.231, 2.63],
    [0.220, 0.349, 1.44],
    [0.173, 0.314, 1.85],
    [0.221, 0.395, 1.31],
    [0.190, 0.467, 1.21],
    [0.134, 0.594, 1.12],
])

# Interpolate the parameters
interps = [interp1d(periods, params[:, i], kind='linear', fill_value='extrapolate') 
           for i in range(3)]


def SpatialcorrGA09(T, h):
    
    if not (0.0 <= T <= 5.0):
        raise ValueError(f"T = {T} is outside the valid range [0, 5.0].")
    
    # Interpolate alpha, beta, gamma for the requested period T
    alpha, beta, gamma = [f(T) for f in interps]

    # Calculate correlation
    rho = gamma * np.exp(-alpha * (h ** beta)) - gamma + 1
    return max(rho, 0)


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


def SpatialCrossCorrGA09(h, t1, t2):
    
    if not (0.0 <= t1 <= 5.0):
        raise ValueError(f"t1 = {t1} is outside the valid range [0, 5.0].")
    if not (0.0 <= t2 <= 5.0):
        raise ValueError(f"t1 = {t2} is outside the valid range [0, 5.0].")
    
    t_max = max(t1, t2)
    rho = corrBC06xy(t1, t2) * SpatialcorrGA09(h, t_max)

    return rho


