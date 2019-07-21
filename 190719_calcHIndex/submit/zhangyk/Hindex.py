import networkx as nx
import datetime

def hIndex(citations):
    citations.sort()
    index = 1
    num = 0
    for i in range(len(citations) - 1, -1, -1):
        if citations[i] >= index:
            index += 1
            num += 1
        else:
            return num
    return num


def HIndex(citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    l1 = [0 for j in range(len(citations) + 1)]
    for i in citations:
        if i > len(citations):
            l1[-1] += 1
        else:
            l1[i] = l1[i] + 1
    s = 0
    i = len(citations)
    while i >= 0:
        s += l1[i]
        if s >= i:
            return i
        i -= 1


def CalHIndex(G, n):
    nodes = G.nodes()
    degree={}
    for i in nodes:
        degree[i]=[nx.degree(G,i)]
    for i in range(n+1):
        if i==0:
            continue
        for j in nodes:
            degree[j].append(HIndex([degree[x][i-1] for x in nx.neighbors(G,j)]))
    return [degree[i][n] for i in sorted(degree)]

G=nx.read_edgelist('./demo.edgelist',nodetype=int)
start = datetime.datetime.now()
CalHIndex(G,3)
end = datetime.datetime.now()
print((end - start).microseconds)