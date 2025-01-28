# %%
import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
# %matplotlib inline 

# %% [markdown]
# ## Question 1

# %%

path = "course_network_l2.adjlist"

df = pd.read_csv(path, sep=" ", names=["Node_u", "Node_v", "Weight"])

G = nx.from_pandas_edgelist(df, source="Node_u", target="Node_v", edge_attr="Weight")

max_degree = max(dict(G.degree()).values())
print(max_degree)

# %% [markdown]
# ## Question 2

# %%
degrees = dict(G.degree())
top_3_nodes = sorted(degrees, key=degrees.get, reverse=True)[:3]

node_sizes = [degrees[node] * 15 for node in G.nodes()]

edge_widths = [G[u][v]['Weight'] for u, v in G.edges()]

labels = {node: node if node in top_3_nodes else "" for node in G.nodes()}

pos = nx.spring_layout(G, seed=42)

# %%
plt.figure(figsize=(8, 8))
nx.draw(
    G,
    pos,
    with_labels=False,
    node_size=node_sizes,
    node_color='yellow',
    edge_color='orange',
    width=edge_widths
)

nx.draw_networkx_labels(G, pos, labels=labels, font_size=12, font_color="black")
plt.title("Course Network")
plt.show()


