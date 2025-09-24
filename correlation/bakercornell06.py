"""
Created by Vitor Monteiro, 23/0/2025

Compute correlation coefficients for Sa(T), for PEER Strong Motion database for
same orientation (x-x) or orthogonal orientations (x-y) for periods between
[0.05-5.0]s.

For more details please see:
Baker, J. W., & Cornell, C. A. (2006). Correlation of Response Spectral Values
for Multicomponent Ground Motions. Bulletin of
the Seismological Society of America,
96(1), 215-227. https://doi.org/10.1785/0120050060
"""


import numpy as np


def corrBC06xx(T1, T2):

    # Check valid input range
    if not (0.05 <= T1 <= 5.0):
        raise ValueError(
            f"T_a = {T1} is outside the valid range [0.05, 5.0].")
    if not (0.05 <= T2 <= 5.0):
        raise ValueError(
            f"T_b = {T2} is outside the valid range [0.05, 5.0].")

    T_min, T_max = min(T1, T2), max(T1, T2)

    I_Tmin = 1 if T_min < 0.189 else 0
    log_ratio = np.log(T_max / T_min)

    inner_term = (np.pi / 2) - (0.359 + 0.163 * I_Tmin *
                                np.log(T_min / 0.189)) * log_ratio
    inner_term = np.clip(inner_term, -np.pi, np.pi)

    rho = 1 - np.cos(inner_term)
    return rho


def corrBC06xy(T1, T2):

    # Check valid input range
    if not (0.05 <= T1 <= 5.0):
        raise ValueError(
            f"T_a = {T1} is outside the valid range [0.05, 5.0].")
    if not (0.05 <= T2 <= 5.0):
        raise ValueError(
            f"T_b = {T2} is outside the valid range [0.05, 5.0].")

    T_min, T_max = min(T1, T2), max(T1, T2)

    I_Tmin = 1 if T_min < 0.189 else 0
    log_ratio = np.log(T_max / T_min)

    inner_term = (np.pi / 2) - (0.359 + 0.163 * I_Tmin *
                                np.log(T_min / 0.189)) * log_ratio
    inner_term = np.clip(inner_term, -np.pi, np.pi)

    rho = (0.79 - 0.023 * np.log(np.sqrt(T2*T1))) * (1 - np.cos(inner_term))
    return rho
