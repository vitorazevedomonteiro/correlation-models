# Correlation modelling functions
This repository provides python scripts to calculate different correlation coefficients. Here it can be found inter/intra-IM non-spatial correlation models and inter/intra-IM spatial correlation models.
All the citations of each model presented in this repository are included within the python scripts and showed below.

For a more detailed review of the ground motion correlation modelling for regional seismic risk analysis please see the paper cited below:

# Reference
Monteiro, V.A and O’Reilly, G.J. (2025) ‘A review of ground motion correlation modelling for regional seismic risk analysis’, (Coming Soon)

# Models currently provided:



|        Function        |             Database                |  Spatial Correlation  |   Non-Spatial Correlation  |    Intensity Measures     |  Reference                    |
|------------------------|-------------------------------------|-----------------------|----------------------------|---------------------------|-------------------------------|
|   booreEtAl03.py       |  1994 Northridge earthquake         |           X           |             -              |    PGA                    | Boore et al. [2003]           |
|   wangtakada05.py      |  Taiwan and Japanese earthquakes    |           X           |             -              |    PGV                    | Wang and Takada [2005]        |
|   bakercornell06.py    |  PEER Strong Motion (2000)          |           -           |             X              |    Sa(T)                  | Baker and Cornell [2006]      |
|   godahong08           |  Chi-Chi and California earthquakes |           X           |             X              |    PGA, PGV, Sa(T)        | Goda and Hong [2008]          |
|   godaatkinson09       |  K-net and KiK-net databases        |           X           |             X              |    PGA, PGV, Sa(T)        | Goda and Atkinson [2009]      |
|   bakerjayaram08       |  NGA-W1 database                    |           -           |             X              |    Sa(T)                  | Baker and Jayaram [2008]      |
|   jayarambaker09       |  NGA-W1 database                    |           X           |             -              |    Sa(T)                  | Jayaram and Baker [2009]      |
|   SokolovEtAl10        |  TSMP network in Taiwan             |           X           |             -              |    PGA                    | Sokolov et al. [2010]         |
|   espositoiervolino11  |  ESMD and ITACA databases           |           X           |             -              |    PGA, PGV               | Esposito and Iervolino [2011] |
|   espositoiervolino12  |  ESMD and ITACA databases           |           X           |             -              |    Sa(T)                  | Esposito and Iervolino [2012] |
|   bradley11a           |  NGA-W1 database                    |           -           |             X              |    D_{sxy}                       |                       |
|                        |                    |                       |                            |                           |                       |




