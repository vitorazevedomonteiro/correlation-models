"""
Created by Vitor Monteiro, 23/09/2025

Compute cross-spatial correlation coefficients between Sa(T) 
for NGA-W1 database database for periods between [0.01-10.0]s considering site effects.

For more details please see: 
Wang, G., & Du, W. (2013). 
Spatial cross-correlation models for vector intensity measures (PGA, Ia, PGV, and SAs) 
considering regional site conditions. Bulletin of the Seismological Society of America, 103(6), 3189–3204. 
https://doi.org/10.1785/0120130061
"""

import numpy as np

def CrossSpatialCorrWD13(T1, T2, h, Rvs30):

    # Validate inputs
    if T1 < 0.01 or T2 < 0.01:
        raise ValueError('The periods must be greater or equal to 0.01s')
    if T1 > 10 or T2 > 10:
        raise ValueError('The periods must be less or equal to 10s')
    if h < 0:
        raise ValueError('The separation distance must be positive')

    # Tlist and coefficients
    Tlist = np.array([0.01, 0.1, 0.2, 0.5, 1, 2, 5, 7.5, 10.0001])

    # Special case: perfect correlation only if periods are equal and distance is zero
    if T1 == T2 and h == 0:
        return 1.0

    # Model coefficients
    P01 = np.array([
        [0.96, 0.90, 0.80, 0.50, 0.15, 0.09, 0.10, 0.09, 0.04],
        [0.90, 0.96, 0.81, 0.36, 0.08, 0.04, 0.05, 0.05, 0.02],
        [0.80, 0.81, 0.93, 0.44, 0.10, 0.05, 0.09, 0.08, 0.05],
        [0.50, 0.36, 0.44, 0.76, 0.25, 0.17, 0.14, 0.13, 0.07],
        [0.15, 0.08, 0.10, 0.25, 0.62, 0.45, 0.34, 0.37, 0.31],
        [0.09, 0.04, 0.05, 0.17, 0.45, 0.54, 0.42, 0.42, 0.35],
        [0.10, 0.05, 0.09, 0.14, 0.34, 0.42, 0.47, 0.46, 0.39],
        [0.09, 0.05, 0.08, 0.13, 0.37, 0.42, 0.46, 0.57, 0.40],
        [0.04, 0.02, 0.05, 0.07, 0.31, 0.35, 0.39, 0.40, 0.56]
    ])

    P02 = np.array([
        [0.04, 0.00, 0.01, 0.04, 0.08, 0.02, 0.02, 0.00, 0.02],
        [0.00, 0.04, 0.01, 0.00, 0.01, 0.00, 0.00, 0.00, 0.00],
        [0.01, 0.01, 0.07, 0.08, 0.08, 0.01, 0.00, 0.00, 0.00],
        [0.04, 0.00, 0.08, 0.24, 0.28, 0.20, 0.15, 0.13, 0.13],
        [0.08, 0.01, 0.08, 0.28, 0.38, 0.22, 0.23, 0.18, 0.19],
        [0.02, 0.00, 0.01, 0.20, 0.22, 0.46, 0.32, 0.25, 0.25],
        [0.02, 0.00, 0.00, 0.15, 0.23, 0.32, 0.53, 0.43, 0.42],
        [0.00, 0.00, 0.00, 0.13, 0.18, 0.25, 0.43, 0.43, 0.41],
        [0.02, 0.00, 0.00, 0.13, 0.19, 0.25, 0.42, 0.41, 0.44]
    ])

    K = np.array([
        [0.04, 0.00, 0.01, 0.04, 0.08, 0.02, 0.02, 0.00, 0.02],
        [0.00, 0.04, 0.01, 0.00, 0.01, 0.00, 0.00, 0.00, 0.00],
        [0.01, 0.01, 0.07, 0.08, 0.08, 0.01, 0.00, 0.00, 0.00],
        [0.04, 0.00, 0.08, 0.24, 0.28, 0.20, 0.15, 0.13, 0.13],
        [0.08, 0.01, 0.08, 0.28, 0.38, 0.22, 0.23, 0.18, 0.19],
        [0.02, 0.00, 0.01, 0.20, 0.22, 0.46, 0.32, 0.25, 0.25],
        [0.02, 0.00, 0.00, 0.15, 0.23, 0.32, 0.53, 0.43, 0.42],
        [0.00, 0.00, 0.00, 0.13, 0.18, 0.25, 0.43, 0.43, 0.41],
        [0.02, 0.00, 0.00, 0.13, 0.19, 0.25, 0.42, 0.41, 0.44]
    ])

    # Find the interval in which input period is located
    for i in range(len(Tlist) - 1):
        if T1 - Tlist[i] >= 0 and T1 - Tlist[i + 1] < 0:
            index1 = i
        if T2 - Tlist[i] >= 0 and T2 - Tlist[i + 1] < 0:
            index2 = i

    # Linearly interpolate the corresponding value of each coregionalization matrix coefficient
    def interpolate(P, index1, index2, T1, T2, Tlist):
        coeff1 = P[index1, index2] + (P[index1 + 1, index2] - P[index1, index2]) / (
            Tlist[index1 + 1] - Tlist[index1]) * (T1 - Tlist[index1])
        coeff2 = P[index1, index2 + 1] + (P[index1 + 1, index2 + 1] - P[index1, index2 + 1]) / (
            Tlist[index1 + 1] - Tlist[index1]) * (T1 - Tlist[index1])
        coeff0 = coeff1 + (coeff2 - coeff1) / \
            (Tlist[index2 + 1] - Tlist[index2]) * (T2 - Tlist[index2])
        return coeff0

    P01coeff0 = interpolate(P01, index1, index2, T1, T2, Tlist)
    P02coeff0 = interpolate(P02, index1, index2, T1, T2, Tlist)
    Kcoeff0 = interpolate(K, index1, index2, T1, T2, Tlist)

    # Compute correlation coefficient (Equation 42)
    rho = P01coeff0 * np.exp(-3 * h / 10) + \
        P02coeff0 * np.exp(-3 * h / 70) + Kcoeff0*(Rvs30/10) * \
        (np.exp((-3*h)/70)-np.exp((-3*h)/10))

    return rho


