import numpy as np
from typing import List, Callable
from functools import reduce

def z_values() ->np.ndarray:
    return np.linspace(start=-3.0, stop=3.0, num=25)

def num_latent()->int:
    return 2

def num_observed() ->int:
    return 28*28

def plus(x: float,y:float) ->float:
    return x+y

def accumarray(subs: np.ndarray, vals: np.ndarray, fun) -> List[float]:
    ret = [[] for _ in subs]
    for i in range(subs.shape[0]):
        subscript = subs[i]
        val = vals[i]
        try:
            ret[subscript].append(val)
        except:
            ret[subscript] = [val]
    for i, ls in enumerate(ret):
        ret[i]=reduce(fun, ls)
    return ret