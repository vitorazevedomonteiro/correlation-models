"""
Created by Vitor Monteiro, 23/09/2025

Compute spatial correlation coefficients for for PGA and PGV,
for ESD database and ITACA database.

For more details please see: 
Esposito, S., & Iervolino, I. (2011). 
PGA and PGV Spatial Correlation Models Based on European Multievent Datasets. 
Bulletin of the Seismological Society of America, 101(5), 2532–2541. 
https://doi.org/10.1785/0120110117
"""

import numpy as np

def SpatialCorrEI11(h, im, database=1):
    if database == 1:  # ESD database
        if im == 'PGA':
            b = 13.5
            rho = 1 - (1 - np.exp(-(3*h)/b))
        elif im == 'PGV':
            b = 21.5
            rho = 1 - (1 - np.exp(-(3*h)/b))
            return rho
        else:
            print("IM can not be used in this model, just 'PGA' or 'PGV'")
    elif database == 2:  # ITACA database
            if im == 'PGA':
                b = 11.5
                rho = 1 - (1 - np.exp(-(3*h)/b))
            elif im == 'PGV':
                b = 14.5
                rho = 1 - (1 - np.exp(-(3*h)/b))
                return rho
            print("IM can not be used in this model, just 'PGA' or 'PGV'")
    


