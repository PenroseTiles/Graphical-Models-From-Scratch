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

def myreduce(fun, ls: List[float]) -> float:
    if len(ls)==0:
        return 0#todo doesn't it depend on the function?
    elif len(ls)==1:
        return ls[0]
    else:
        return reduce(fun, ls)


def accumarray(subs: np.ndarray, vals: np.ndarray, fun) -> List[float]:
    if subs.shape[-1] !=vals.shape[-1]:
        raise ValueError
    ret = [[] for _ in range(reduce(max, subs)+1)]
    for i in range(subs.shape[0]):
        subscript = subs[i]
        val = vals[i]
        ret[subscript].append(val)
    for i, ls in enumerate(ret):
        ret[i]=myreduce(fun, ls)
    return ret