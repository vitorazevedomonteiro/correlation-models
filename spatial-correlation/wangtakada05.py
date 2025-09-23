"""
Created by Vitor Monteiro, 23/09/2025

Compute spatial correlation coefficients for PGV, for Taiwan and Japanese earthquakes.

For more details please see: 
Wang, M., & Takada, T. (2005). Macrospatial Correlation Model of Seismic Ground Motions.
Earthquake Spectra, 21(4), 1137–1156. https://doi.org/10.1193/1.2083887
"""

import numpy as np

def SpatialcorrWT05(h, gmm, earthquake):
    if gmm == 'annaka':
        # With Annaka relationship
        if earthquake == 'Chi-Chi':
            b = 27.8  # Chi-Chi earthquake
        elif earthquake == 'Tottori-ken Seibu':
            b = 21.0  # Tottori-ken Seibu
        elif earthquake == 'Geiyo':
            b = 47.8  # Geiyo
        elif earthquake == 'Miyagi-ken-oki':
            b = 39.7  # Miyagi-ken-oki
        elif earthquake == 'Miyagi-ken Hokubu':
            b = 27.7  # Miyagi-ken Hokubu
        elif earthquake == 'Tokachi-oki':
            b = 24.5  # Tokachi-oki
    elif gmm == 'Midorikawa-Ohtake':
        # With Midorikawa-Ohtake relationship
        if earthquake == 'Chi-Chi':
            b = 27.3  # Chi-Chi earthquake
        elif earthquake == 'Tottori-ken Seibu':
            b = 28.6  # Tottori-ken Seibu
        elif earthquake == 'Geiyo':
            b = 35.8  # Geiyo
        elif earthquake == 'Miyagi-ken-oki':
            b = 21.6  # Miyagi-ken-oki
        elif earthquake == 'Miyagi-ken Hokubu':
            b = 24.0  # Miyagi-ken Hokubu
        elif earthquake == 'Tokachi-oki':
            b = 22.4  # Tokachi-oki

    rho = np.exp(-(h)/b)
    return rho



