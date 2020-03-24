from Graph import Graph
import numpy as np
from typing import List, Dict
from utils import *

class BayesNet():
    def __init__(self, graph: Graph):
        self.graph = graph
        self.distributions={}
        for node in graph.get_all_roots():
            self.distributions[node+'_prior'] = {}
            for z in z_values():
                self.distributions[node + '_prior'][z] =  1./z_values().shape[0]

        self.distributions['cond_likelihood']={}
        #representation is easy because all nodes are conditioned on the same 2 latent vars
        for z1val in z_values():
            for z2val in z_values():
                self.distributions['cond_likelihood'][(z1val, z2val)] = np.ones(shape=(1, num_observed()))/num_observed()
        return

    def get_cpds_from_graph(self):
        #reverse the graph and for every node, get its parents and form a combined CPD
        rev = self.graph.reverse()
        leaves = rev.get_all_roots()
        #construct the tree bottom up, we've already checked for no cycles
        return


graph = Graph()
bn = BayesNet(graph)
for dist in bn.distributions:
    print(bn.distributions[dist])
print(len(bn.distributions['cond_likelihood']))