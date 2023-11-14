from kact import *
from kact.utils import *
from kact.utils.functions import relu

KRELU_METHODS = {"cdd": krelu_with_cdd,
                 "pycdd": krelu_with_pycdd,
                 "triangle": krelu_with_triangle,
                 "fast": fkrelu,
                "sci": krelu_with_sci,
                 "sciplus": krelu_with_sciplus,
                 }

KSIGMOID_METHODS = {"cdd": ksigm_with_cdd,
                    "fast": fksigm,
                    "orthant": fsigm_orthant,
                    "sci": ksigm_with_sci_old2,
                    "sciplus": ksigm_with_sciplus_old2,
                    }

KTANH_METHODS = {"cdd": ktanh_with_cdd,
                 "fast": fktanh,
                 "orthant": ftanh_orthant,
                 "sci": ktanh_with_sci_old2,
                 "sciplus": ktanh_with_sciplus_old2,
                 }

METHODS_DIC = {"relu": KRELU_METHODS,
               "sigmoid": KSIGMOID_METHODS,
               "tanh": KTANH_METHODS}

ACT_FUNCTIONS = {"relu": relu,
                 "sigmoid": sigmoid,
                 "tanh": tanh}

CONSTRAINTS_SAMPLE1 = [[1, 1],
                       [1, -1]]
CONSTRAINTS_SAMPLE2 = [[1., 0., -1.],
                       [2., 0., 1.],
                       [1., -1., -1.],
                       [3., 1., 1.],
                       [3., -1., 1.]]
CONSTRAINTS_SAMPLE3 = [[2, 1, 1],
                       [2, 1, -1],
                       [1.2, -1, 0],
                       [2, -1, 1],
                       [2, -1, -1]]
