"""
Created by Vitor Monteiro, 23/09/2025

Compute correlation coefficients for Sa(T), PGA, and PGV for
Europe and the Middle East earthquakes for periods between [0.0-4.0]s.

For more details please see:
Huang, C., & Galasso, C. (2019). Ground‐motion intensity measure correlations
observed in Italian strong‐motion records.
Earthquake Engineering & Structural Dynamics, 48(15), 1634–1660.
https://doi.org/10.1002/eqe.3216
"""
# flake8: noqa: E501

import numpy as np

periods = np.array([0.010, 0.025, 0.040, 0.050, 0.070, 0.1, 0.150, 0.20, 0.250, 0.30, 0.350, 0.40,
                    0.450, 0.50, 0.60, 0.70, 0.75, 0.800, 0.900, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.5, 3.0, 3.5, 4.0])
Corr_Sa_PGA = np.array([0.999983, 0.997196, 0.980698,  0.969658, 0.954503, 0.952140, 0.953778, 0.945317, 0.922043, 0.900011, 0.874693, 0.844783, 0.816778, 0.790233,
                       0.745661, 0.709850, 0.689572, 0.672765, 0.640651, 0.612437, 0.568656, 0.526700, 0.498941, 0.478026, 0.458779, 0.430386, 0.408848, 0.393311, 0.390552])
Corr_Sa_PGV = np.array([0.860520, 0.850151, 0.808272, 0.773502, 0.730389, 0.727067, 0.766467, 0.806290, 0.845147, 0.867540, 0.885360, 0.895832, 0.898624, 0.899610,
                       0.896019, 0.890368, 0.883600, 0.876883, 0.864202, 0.851573, 0.827989, 0.804427, 0.786983, 0.770769, 0.755716, 0.732758, 0.714882, 0.704214, 0.702563])


def corrHG19_SaIM(period, corr_type='PGA'):
    """
    Interpolates correlation for a given period.

    Parameters:
        period (float): The period to get the correlation for.
        corr_type (str): 'PGA' or 'PGV' to select correlation type.

    Returns:
        float: Interpolated correlation.
    """
    if corr_type.upper() == 'PGA':
        corr_array = Corr_Sa_PGA
    elif corr_type.upper() == 'PGV':
        corr_array = Corr_Sa_PGV
    else:
        raise ValueError("corr_type must be 'PGA' or 'PGV'")

    rho = float(np.interp(period, periods, corr_array))

    return rho


def corrHG19_SaSa(T1, T2):

    if not (periods.min() <= T1 <= periods.max()):
        raise ValueError(
            f"T1={T1} is outside the valid range "
            f"[{periods.min()}, {periods.max()}]")
    if not (periods.min() <= T2 <= periods.max()):
        raise ValueError(
            f"T2={T2} is outside the valid range "
            f"[{periods.min()}, {periods.max()}]")

    T_min, T_max = min(T1, T2), max(T1, T2)

    # Model
    C1 = 1 - np.cos((np.pi / 2) - 0.2351 *
                    np.log(T_max / np.maximum(T_min, 0.1)))
    C2 = 1 - 0.0617 * (1 - (1 / (1 + np.exp(100 * T_max - 5)))
                       ) * ((T_max - T_min) / (T_max - 0.0099))
    C3 = C1 + 0.3131 * (np.sqrt(C1) - C1) * (1 + np.cos((np.pi * T_min) / 0.1))

    if T_max <= 0.1:
        rho = C2
    elif T_min > 0.1:
        rho = C1
    elif T_max <= 0.2:
        rho = min(C2, C3)
    else:
        rho = C3

    return rho
