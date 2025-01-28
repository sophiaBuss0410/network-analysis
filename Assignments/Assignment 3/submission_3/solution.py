# %%
import warnings
warnings.filterwarnings('ignore')

import numpy as np
import seaborn as sns
import networkx as nx
import matplotlib.pyplot as plt
from tqdm.autonotebook import tqdm

import seaborn as sns
sns.set(style="whitegrid")

def frequencies(N, ps, num_trials):
    frequencies = []

    for p in ps:
        connected_count = 0
        for _ in tqdm(range(num_trials)):
            G = nx.fast_gnp_random_graph(N, p)
            if nx.is_connected(G):
                connected_count += 1
        
        frequencies.append(connected_count / num_trials)

    plt.figure(figsize=(10, 6))
    plt.scatter(ps, frequencies, c = 'orange')
    plt.xlabel('p')
    plt.ylabel('Empirical Relative Frequency')
    plt.title('Plot id: 1 Relative Frequency of Graph Being Connected vs p')
    plt.grid(True)
    plt.savefig('plot-id-1-empirical-relative-frequency.png')
    # plt.show()

def size(N, ps, num_trials):
    avg_largest_cc_size = []

    for p in ps:
        connected_count = 0
        largest_cc_sizes = []
        for _ in tqdm(range(num_trials)):
            G = nx.fast_gnp_random_graph(N, p)
            if nx.is_connected(G):
                connected_count += 1
            largest_cc = max(nx.connected_components(G), key=len)
            largest_cc_sizes.append(len(largest_cc))
        
        avg_largest_cc_size.append(np.mean(largest_cc_sizes))

    plt.figure(figsize=(10, 6))
    plt.scatter(ps, avg_largest_cc_size, c = 'green')
    plt.xlabel('p')
    plt.ylabel('Empirical Average Size of Largest Connected Component')
    plt.title('Plot id: 2 Average Size of Largest Connected Component vs p')
    plt.grid(True)
    plt.savefig('plot-id-2-empirical-average-size.png')
    # plt.show()


# %%
def frequencies_small(N, ps, num_trials):
    frequencies = []

    for p in ps:
        connected_count = 0
        for _ in tqdm(range(num_trials)):
            G = nx.fast_gnp_random_graph(N, p)
            if nx.is_connected(G):
                connected_count += 1
        
        frequencies.append(connected_count / num_trials)

    plt.figure(figsize=(10, 6))
    plt.scatter(ps, frequencies, c = 'orange')
    plt.xlabel('p')
    plt.ylabel('Empirical Relative Frequency')
    plt.title('Plot id: 3 Relative Frequency of Graph Being Connected vs small p')
    plt.grid(True)
    plt.savefig('plot-id-3-empirical-relative-frequency-small.png')
    # plt.show()

def size_small(N, ps, num_trials):
    avg_largest_cc_size = []

    for p in ps:
        connected_count = 0
        largest_cc_sizes = []
        for _ in tqdm(range(num_trials)):
            G = nx.fast_gnp_random_graph(N, p)
            if nx.is_connected(G):
                connected_count += 1
            largest_cc = max(nx.connected_components(G), key=len)
            largest_cc_sizes.append(len(largest_cc))
        
        avg_largest_cc_size.append(np.mean(largest_cc_sizes))

    plt.figure(figsize=(10, 6))
    plt.scatter(ps, avg_largest_cc_size, c = 'green')
    plt.xlabel('p')
    plt.ylabel('Empirical Average Size of Largest Connected Component')
    plt.title('Plot id: 4 Average Size of Largest Connected Component vs small p')
    plt.grid(True)
    plt.savefig('plot-id-4-empirical-average-size-small.png')
    # plt.show()

############################################

N = 500
num_trials = 50

ps1 = np.linspace(0.001, 0.03, 20)
ps2 = np.linspace(0.025, 1, 10)
ps = np.concatenate((ps1, ps2))

frequencies(N, ps, num_trials)

# %%
ps1 = np.linspace(0.001, 0.015, 20)
ps2 = np.linspace(0.01, 1, 10)
ps = np.concatenate((ps1, ps2))

size(N, ps, num_trials)

# %%
ps = np.linspace(0.001, 0.03, 10)

frequencies_small(N, ps, num_trials)

ps = np.linspace(0.001, 0.015, 10)

size_small(N, ps, num_trials)


# %%
