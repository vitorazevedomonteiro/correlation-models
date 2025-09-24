# flake8: noqa
import inspect
from .akkarEtAl14 import corrA14
from .bakerbradley17 import corrBB17
from .bakercornell06 import corrBC06xx, corrBC06xy
from .bakerjayaram08 import corrBJ08
from .bradley11 import corrB11
from .bradley12 import corrB12
from .cimellaro13 import corrC13
from .huanggalasso19 import corrHG19_SaIM, corrHG19_SaSa


ALIASES = {
    "akkaretal14": corrA14,
    "bakerbradley17": corrBB17,
    "bakercornell06xx": corrBC06xx,
    "bakercornell06xy": corrBC06xy,
    "bakerjayaram08": corrBJ08,
    "bradley11": corrB11,
    "bradley12": corrB12,
    "cimellaro13": corrC13,
    "huanggalasso19_sa_im": corrHG19_SaIM,
    "huanggalasso19_sa_sa": corrHG19_SaSa,
}


def select_func_args(function):
    sig = inspect.signature(function)

    func_params = [param.name for param in sig.parameters.values()
                   if param.name != 'self']

    return func_params