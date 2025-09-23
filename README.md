# Correlation modelling functions
This repository provides python scripts to calculate different correlation coefficients. Here it can be found some inter/intra-IM non-spatial correlation models and inter/intra-IM spatial correlation models.
All the citations of each model presented in this repository are included within the python scripts and showed below.

For a more detailed review of the ground motion correlation modelling for regional seismic risk analysis please see the paper cited below:

# Reference
Monteiro, V.A and O’Reilly, G.J. (2025) ‘A review of ground motion correlation modelling for regional seismic risk analysis’, (Coming Soon)

# Models currently provided:



|        Function           |             Database                            | Inter-IM Spatial Correlation | Intra-IM Spatial Correlation |   Non-Spatial Correlation  |    Intensity Measures  |  Reference                 |
|   booreEtAl03.py          |  1994 Northridge earthquake                     |     -     |     X     |             -              |    PGA                                              | Boore et al. [2003]                 |
|   wangtakada05.py         |  Taiwan and Japanese earthquakes                |     -     |     X     |             -              |    PGV                                              | Wang and Takada [2005]              |
|   bakercornell06.py       |  PEER Strong Motion (2000)                      |     -     |     -     |             X              |    Sa(T)                                            | Baker and Cornell [2006]            |
|   godahong08.py           |  Chi-Chi and California earthquakes             |     X     |     X     |             -              |    PGA, PGV, Sa(T)                                  | Goda and Hong [2008]                |
|   godaatkinson09.py       |  K-net and KiK-net databases                    |     X     |     X     |             X              |    PGA, PGV, Sa(T)                                  | Goda and Atkinson [2009]            |
|   bakerjayaram08.py       |  NGA-W1 database                                |     -     |     -     |             X              |    Sa(T)                                            | Baker and Jayaram [2008]            |
|   jayarambaker09.py       |  NGA-W1 database                                |     -     |     X     |             -              |    Sa(T)                                            | Jayaram and Baker [2009]            |
|   SokolovEtAl10.py        |  TSMP network in Taiwan                         |     -     |     X     |             -              |    PGA                                              | Sokolov et al. [2010]               |
|   espositoiervolino11.py  |  ESM  and ITACA databases                       |     -     |     X     |             -              |    PGA, PGV                                         | Esposito and Iervolino [2011]       |
|   espositoiervolino12.py  |  ESM  and ITACA databases                       |     -     |     X     |             -              |    Sa(T)                                            | Esposito and Iervolino [2012]       |
|   bradley11.py            |  NGA-W1 database                                |     -     |     -     |             X              |    Sa(T), PGA, PGV, ASI, SI, DSI, CAV, Duration     | Bradley [2011]                      |  
|   bradley12.py            |  NGA-W1 database                                |     -     |     -     |             X              |    Sa(T), PGV                                       | Bradley [2012]                      |
|   piggottstafford12.py    |  1994 Northridge and 1999 Chi-Chi earthquakes   |     -     |     X     |             -              |    Ia                                               | Foulser-Piggott and Stafford [2012] |
|   lothbaker13.py          |  NGA-W1 database                                |     X     |     -     |             -              |    Sa(T)                                            | Loth and Baker [2013]               |
|   sokolovwenzel13.py      |  K-net and KiK-net databases                    |     -     |     X     |             -              |    PGA, PGV                                         | Sokolov and Wenzel [2013]           |
|   wangdu13.py             |  NGA-W1 database                                |     X     |     -     |             -              |    PGA, PGV, CAV, Sa(T)                             | Wang and Du [2013]                  |
|   duwang13.py             |  NGA-W1 database                                |     -     |     X     |             -              |    Sa(T)                                            | Du and Wang [2013]                  |
|   cimellaro13.py          |  ESM database                                   |     -     |     -     |             X              |    Sa(T)                                            | Cimellaro [2013]                    |
|   akkarEtAl14.py          |  RESORCE database                               |     -     |     -     |             X              |    Sa(T), PGA                                       | Akkar et al. [2014]                 |
|   bakerbradley17.py       |  NGA-W2 database                                |     -     |     -     |             X              |    Sa(T), PGA, PGV, Duration                        | Baker and Bradley [2017]            |
|   markhvidaEtAl18.py      |  NGA-W2 database                                |     X     |     -     |             -              |    Sa(T)                                            | Markhvida et al. [2018]             |
|   heresimiranda19.py      |  NGA-W2 database                                |     -     |     X     |             -              |    Sa(T), PGA                                       | Heresi and Miranda [2019]           |
|   huanggalasso19.py       |  ESM and ITACA databases                        |     -     |     -     |             X              |    Sa(T), PGA, PGV                                  | Huang and Galasso [2019]            |
|   dining21.py             |  NGA-W2                                         |     X     |     -     |             -              |    Sa(T), PGA, PGV, CAV, Ia, Duration               | Du and Ning [2021]                  |
|   schiappapietraEtAl22.py |  ESM database                                   |     -     |     X     |             -              |    Sa(T)                                            | Schiappapietra et al [2022]         |
|   aldeaEtAl22             |  Chilean earthquakes                            |     -     |     X     |             -              |    Sa(T), PGA                                       | Aldea et al. [2022]                 |
|   aristeidouEtAl24        |  NGA-W2 database                                |     -     |     -     |             X              |    Sa(T), PGA, PGV, PGD, Duration, FIV3, Saavg(T)   | Aristeidou et al. [2024]            |



