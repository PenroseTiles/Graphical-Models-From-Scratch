import BN, Graph, numpy as np
from utils import *

# graph = Graph.Graph()
# bn = BN.BayesNet(graph)
# for dist in bn.distributions:
#     print(bn.distributions[dist])
# print(len(bn.distributions['cond_likelihood']))

print(accumarray(np.array([1,2,1]),vals=np.arange(101,104), fun=plus))