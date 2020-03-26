import BN, Graph, numpy as np

graph = Graph.Graph()
bn = BN.BayesNet(graph)
for dist in bn.distributions:
    print(bn.distributions[dist])
print(len(bn.distributions['cond_likelihood']))