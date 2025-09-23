"""
Created by Vitor Monteiro, 23/09/2025

Compute spatial correlation coefficients for PGA from California 1994 earthquake.

For more details please see: 
Boore, D. M. (2003). Estimated Ground Motion From the 1994 Northridge, California, Earthquake at the Site of the Interstate 
10 and La Cienega Boulevard Bridge Collapse, West Los Angeles, California. Bulletin of the Seismological Society of America, 
93(6), 2737–2751. https://doi.org/10.1785/0120020197
"""

import numpy as np

def SpatialcorrB03(h):
    rho = 1 - (1 - np.exp(-np.sqrt(0.6*h)))**2
    return rho


