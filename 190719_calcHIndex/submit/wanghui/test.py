import networkx as nx

degrees = {}
G = nx.read_edgelist('dolphins.edgelist')
neighbors = {}  # key为节点 value为节点邻居的list
nodes = G.nodes()

for node in nodes:
    neighbors[node] = []
    degrees[node] = G.degree(node)
    for i in G.neighbors(node):
        neighbors[node].append(i)
print(degrees)