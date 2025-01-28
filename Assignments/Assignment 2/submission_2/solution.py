import warnings
warnings.filterwarnings('ignore')

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

import seaborn as sns
sns.set(style="whitegrid")

def visualize_graphs(graphs, N=100, p=0.1):
    N = 100
    id = 1
    for graph_type in graphs:
        if graph_type == "fast_gnp_random_graph":
            G = nx.fast_gnp_random_graph(N, p, directed=True)
        elif graph_type == "random_k_out_graph":
            G = nx.random_k_out_graph(N, k=30, alpha=0.9, self_loops=False)
        elif graph_type == "scale_free_graph":
            G = nx.scale_free_graph(N)
        else:
            continue

        pr = nx.pagerank(G, alpha=0.9)
        in_degree = dict(G.in_degree())
        normalized_in_degree = {k: v / (N-1) for k, v in in_degree.items()}

        plt.figure(figsize=(8,6))
        plt.scatter(list(pr.values()), list(normalized_in_degree.values()), c='orange', alpha=0.7)
        plt.xlabel('PageRank')
        plt.ylabel('Normalized Degree')
        plt.title(f'Plot id: {id} PageRank vs. Normalized Degree for {graph_type}')
        plt.savefig(f'plot-id-{id}-measure-plot-{graph_type}.png')

        plt.figure(figsize=(10,8))
        pos = nx.spring_layout(G)
        node_color = [pr[node] for node in G]
        node_size = [in_degree[node]*30 for node in G]
        nx.draw_networkx(G, pos, node_color=node_color, node_size=node_size, cmap=plt.cm.coolwarm, with_labels=False,
                         edge_color='gray', width=0.5, alpha=0.7)
        plt.title(f'Plot id: {id+1} Network Visualization with PageRank (Color) and Degree (Size) for {graph_type}')
        plt.savefig(f'plot-id-{id+1}-network-plot-{graph_type}.png')

        id += 2


graphs = ["fast_gnp_random_graph", "random_k_out_graph", "scale_free_graph"]
visualize_graphs(graphs)

def visualize_graph(graph, graph_type, id):

        N = len(G.nodes)
        pr = nx.pagerank(G, alpha=0.9)
        in_degree = dict(G.in_degree())
        normalized_in_degree = {k: v / (N-1) for k, v in in_degree.items()}

        plt.figure(figsize=(8,6))
        plt.scatter(list(pr.values()), list(normalized_in_degree.values()), c='orange', alpha=0.7)
        plt.xlabel('PageRank')
        plt.ylabel('Normalized Degree')
        plt.title(f'Plot id: {id} PageRank vs. Normalized Degree for {graph_type}')
        plt.savefig(f'plot-id-{id}-measure-plot-{graph_type}.png')

        if nx.is_directed(G):
                G_undirected = G.to_undirected()
        else:
                G_undirected = G

        largest_cc = max(nx.connected_components(G_undirected), key=len)
        G_largest_cc = G_undirected.subgraph(largest_cc).copy()

        plt.figure(figsize=(10,8))
        pos = nx.spring_layout(G_largest_cc)
        node_color = [pr[node] for node in G_largest_cc]
        node_size = [in_degree[node]*30 for node in G_largest_cc]
        nx.draw_networkx(G_largest_cc, pos, node_color=node_color, node_size=node_size, cmap=plt.cm.coolwarm, with_labels=False, 
                         edge_color='gray', width=0.5, alpha=0.7)
        plt.title(f'Plot id: {id+1} Largest Component ({len(G_largest_cc.nodes)} nodes) Visualization with PageRank (Color) and Degree (Size) for {graph_type}')
        plt.savefig(f'plot-id-{id+1}-network-plot-{graph_type}.png')

path = "data/p2p-Gnutella06.txt"

G = nx.read_edgelist(path, nodetype=int, create_using=nx.DiGraph)
visualize_graph(G, "p2p-Gnutella06", id=7)

###
path = "data/p2p-Gnutella08.txt"

G = nx.read_edgelist(path, nodetype=int, create_using=nx.DiGraph)
visualize_graph(G, "p2p-Gnutella08", id=9)

###
path = "data/p2p-Gnutella09.txt"

G = nx.read_edgelist(path, nodetype=int, create_using=nx.DiGraph)
visualize_graph(G, "p2p-Gnutella09", id=11)

print("12 plots produced.")