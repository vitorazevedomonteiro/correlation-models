# Correlation modelling functions
This repository provides python scripts to calculating a variety of correlation coefficients. It includes implementations of both inter- and intra-IM non-spatial correlation models, as well as inter- and intra-IM spatial correlation models.
Citations of each model are provided directly within the scripts and are also listed below.

For a more detailed review of the ground motion correlation modelling for regional seismic risk analysis please see the paper cited below:

# Reference
Monteiro, V.A., O’Reilly, G.J. A review of ground motion correlation modelling for regional seismic risk analysis. Bull Earthquake Eng (2026). https://doi.org/10.1007/s10518-026-02377-0

# How to use
Use "get_correlation.py" to get non-spatial correlation coefficients from several models. Inside you can find two simple example of how to use it.
Use "get_spatial_correlation.py" to get inter and/or intra-IM spatial correlation coefficients from several models. Inside you can find two simple example of how to use it.

# Models currently provided:



|        Function           |             Database                            | Spatial Correlation (Inter-IM) | Spatial Correlation (Intra-IM ) |   Non-Spatial Correlation  |    Intensity Measures  |  Reference                 |
|---------------------------|-------------------------------------------------|-----------|-----------|----------------------------|-----------------------------------------------------|-------------------------------------|
|   booreEtAl03.py          |  1994 Northridge earthquake                     |     -     |     X     |             -              |    PGA                                              | Boore et al. [2003](https://doi.org/10.1785/0120020197)                 |
|   wangtakada05.py         |  Taiwan and Japanese earthquakes                |     -     |     X     |             -              |    PGV                                              | Wang and Takada [2005](https://doi.org/10.1193/1.2083887)              |
|   bakercornell06.py       |  PEER Strong Motion (2000)                      |     -     |     -     |             X              |    Sa(T)                                            | Baker and Cornell [2006](https://doi.org/10.1785/0120050060)            |
|   godahong08.py           |  Chi-Chi and California earthquakes             |     X     |     X     |             -              |    Sa(T), PGA                                       | Goda and Hong [2008](https://doi.org/10.1785/0120070078)                |
|   godaatkinson09.py       |  K-net and KiK-net databases                    |     X     |     X     |             X              |    Sa(T), PGA                                       | Goda and Atkinson [2009](https://doi.org/10.1785/0120090007)            |
|   bakerjayaram08.py       |  NGA-W1 database                                |     -     |     -     |             X              |    Sa(T)                                            | Baker and Jayaram [2008](https://doi.org/10.1193/1.2857544)            |
|   jayarambaker09.py       |  NGA-W1 database                                |     -     |     X     |             -              |    Sa(T)                                            | Jayaram and Baker [2009](https://doi.org/10.1002/eqe.922)            |
|   SokolovEtAl10.py        |  TSMP network in Taiwan                         |     -     |     X     |             -              |    PGA                                              | Sokolov et al. [2010](https://doi.org/10.3319/TAO.2010.05.03.01(T))               |
|   espositoiervolino11.py  |  ESM  and ITACA databases                       |     -     |     X     |             -              |    PGA, PGV                                         | Esposito and Iervolino [2011](https://doi.org/10.1785/0120110117)       |
|   espositoiervolino12.py  |  ESM  and ITACA databases                       |     -     |     X     |             -              |    Sa(T)                                            | Esposito and Iervolino [2012](https://doi.org/10.1785/0120120068)       |
|   bradley11.py            |  NGA-W1 database                                |     -     |     -     |             X              |    Sa(T), PGA, PGV, Duration                        | Bradley [2011](https://doi.org/10.1080/13632469.2011.557140)                      |  
|   bradley12.py            |  NGA-W1 database                                |     -     |     -     |             X              |    Sa(T), PGV                                       | Bradley [2012](https://doi.org/10.1193/1.3675582)                      |
|   lothbaker13.py          |  NGA-W1 database                                |     X     |     -     |             -              |    Sa(T)                                            | Loth and Baker [2013](https://doi.org/10.1002/eqe.2212)              |
|   sokolovwenzel13.py      |  K-net and KiK-net databases                    |     -     |     X     |             -              |    PGA, PGV                                         | Sokolov and Wenzel [2013](https://doi.org/10.1007/s10518-013-9493-9)           |
|   wangdu13.py             |  NGA-W1 database                                |     X     |     -     |             -              |    Sa(T)                                            | Wang and Du [2013](https://doi.org/10.1785/0120130061)                  |
|   duwang13.py             |  NGA-W1 database                                |     -     |     X     |             -              |    Sa(T)                                            | Du and Wang [2013](https://doi.org/10.1785/0120120185)                  |
|   cimellaro13.py          |  ESM database                                   |     -     |     -     |             X              |    Sa(T)                                            | Cimellaro [2013](https://doi.org/10.1002/eqe.2248)                    |
|   akkarEtAl14.py          |  RESORCE database                               |     -     |     -     |             X              |    Sa(T), PGA                                       | Akkar et al. [2014](https://doi.org/10.1007/s10518-013-9537-1)                 |
|   bakerbradley17.py       |  NGA-W2 database                                |     -     |     -     |             X              |    Sa(T), PGA, PGV, Duration                        | Baker and Bradley [2017](https://doi.org/10.1193/060716eqs095m)            |
|   markhvidaEtAl18.py      |  NGA-W2 database                                |     X     |     -     |             -              |    Sa(T)                                            | Markhvida et al. [2018](https://doi.org/10.1002/eqe.3007)           |
|   heresimiranda19.py      |  NGA-W2 database                                |     -     |     X     |             -              |    Sa(T), PGA                                       | Heresi and Miranda [2019](https://doi.org/10.1007/s10518-018-0506-6)           |
|   huanggalasso19.py       |  ESM and ITACA databases                        |     -     |     -     |             X              |    Sa(T), PGA, PGV                                  | Huang and Galasso [2019](https://doi.org/10.1002/eqe.3216)            |
|   duning21.py             |  NGA-W2                                         |     X     |     -     |             -              |    Sa(T), PGA, PGV, Duration                        | Du and Ning [2021](https://doi.org/10.1177/8755293020952442)                  |
|   schiappapietraEtAl22.py |  ESM database                                   |     -     |     X     |             -              |    Sa(T)                                            | [Schiappapietra et al [2022](https://doi.org/10.1007/s10518-022-01413-z)|
|   aldeaEtAl22             |  Chilean earthquakes                            |     -     |     X     |             -              |    Sa(T), PGA                                       | [Aldea et al. [2022](https://doi.org/10.1002/eqe.3674)                  |
|   aristeidouEtAl24 (see https://github.com/Savvinos-Aristeidou/ANN_correlation_models.git)       |  NGA-W2 database                                |     -     |     -     |             X              |    Sa(T), PGA, PGV, PGD, Duration, FIV3, Saavg(T)   | Aristeidou et al. [2024](https://doi.org/10.1177/87552930241270)            |
|   MonteiroEtAl24 (see https://github.com/vitorazevedomonteiro/cross-spatial-correlation-model.git)       |  NGA-W2 and ESM database                          |     X     |     -     |             -              |    Sa(T), PGA, PGV, FIV3, Saavg(T)                  | Monteiro V.A. et al. [2025] (under revision)            |

Note that inter-IM spatial models also capture intra-IM spatial correlation by definition.

