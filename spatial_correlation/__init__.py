# flake8: noqa
import inspect
from .aldeaEtAl22 import SpatialCrossAHP22
from .booreEtAl03 import SpatialCorrB03
from .duning21 import CrossSpatialCorrDN21
from .duwang13 import SpatialCorrDW13
from .espositoiervolino11 import SpatialCorrEI11
from .espositoiervolino12 import SpatialCorrEI12
from .godaatkinson09 import SpatialCorrGA09, CrossSpatialCorrGA09
from .godahong08 import SpatialCorrGH08_SA, SpatialCorrGH08_PGA, CrossSpatialCorrGH08
from .heresimiranda19 import SpatialCorrHM19
from .jayarambaker09 import SpatialCorrJB09
from .lothbaker13 import CrossSpatialCorrLB13
from .markhvidaEtAl18 import CrossSpatialCorrMCB18
from .schiappapietraEtAl22 import SpatialCorrS22_N, SpatialCorrS22_C, SpatialCorrS22_S
from .sokolovEtAl10 import SpatialCorrS10
from .sokolovwenzel13 import SpatialCorrSW13
from .wangdu13 import CrossSpatialCorrWD13
from .wangtakada05 import SpatialCorrWT05



ALIASES = {
    "aldeaetal22": SpatialCrossAHP22,
    "booreetal03": SpatialCorrB03,
    "duning21": CrossSpatialCorrDN21,
    "duwang13": SpatialCorrDW13,
    "espositoiervolino11": SpatialCorrEI11,
    "espositoiervolino12": SpatialCorrEI12,
    "godaatkinson09_spatialcorr": SpatialCorrGA09,
    "godaatkinson09_crossspatialcorr": CrossSpatialCorrGA09,
    "godahong08_spatialcorr_sa_sa": SpatialCorrGH08_SA,
    "godahong08_spatialcorr_sa_pga": SpatialCorrGH08_PGA,
    "godahong08_crossspatialcorr": CrossSpatialCorrGH08,
    "heresimiranda19": SpatialCorrHM19,
    "jayarambaker09": SpatialCorrJB09,
    "lothbaker13": CrossSpatialCorrLB13,
    "markhvidaetal18": CrossSpatialCorrMCB18,
    "schiappapietraetal22_north_region": SpatialCorrS22_N,
    "schiappapietraetal22_center_region": SpatialCorrS22_C,
    "schiappapietraetal22_south_region": SpatialCorrS22_S,
    "sokolovetal10": SpatialCorrS10,
    "sokolovwenzel13": SpatialCorrSW13,
    "wangdu13": CrossSpatialCorrWD13,
    "wangtakada05": SpatialCorrWT05,
}


def select_func_args(function):
    sig = inspect.signature(function)

    func_params = [param.name for param in sig.parameters.values()
                   if param.name != 'self']

    return func_params
