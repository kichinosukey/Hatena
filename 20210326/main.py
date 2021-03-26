import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def get_multi_edge_nodes(G, threshold):
    node_list = list(G)
    A = nx.adjacency_matrix(G)
    A_flatten = np.ravel(A.todense())
    idx_sorted_list = np.where(A_flatten >= threshold)[0] # return value is tuple
    node_multi_edge_list = [node_list[(I % len(G.nodes))] for I in idx_sorted_list]
    return set(node_multi_edge_list)

def rand_edges(node_num, edge_num):
    def randint(low, high, size):
        return np.random.randint(low, high, size)
    return [(s, t) for s, t in zip(randint(0, node_num, edge_num), randint(0, node_num, edge_num))]

ADD_EDGE_SIZE = 30
THRESHOLD_MULTI_EDGE = 2

if __name__ == '__main__':

    G_01 = nx.karate_club_graph()
    G_02 = nx.MultiGraph()
    G_02.add_edges_from(G_01.edges)
    G_02.add_edges_from(rand_edges(len(G_02), ADD_EDGE_SIZE))

    ret2 = get_multi_edge_nodes(G_02, THRESHOLD_MULTI_EDGE)

    G_02_sub = G_02.subgraph(ret2)

    fig, (ax1, ax2) = plt.subplots(1, 2)
    nx.draw_networkx(G_01, ax=ax1)
    nx.draw_networkx(G_02_sub, ax=ax2)

    plt.savefig('test.png')