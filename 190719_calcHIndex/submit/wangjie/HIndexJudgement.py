import networkx as nx
import net2gml
import edgelist2gml
import time


def getGraphH0(G):
    H0Dic = {}
    for node in nx.nodes(G):
        H0Dic[node] = nx.degree(G, node)
    return H0Dic


def getGraphneighbor(G):
    neighborDic = {}
    for node in nx.nodes(G):
        neighborDic[node] = [neighbor for neighbor in G[node]]
    return neighborDic


def getH(temp):
    temp.sort(reverse=True)
    for index, item in enumerate(temp):
        if index + 1 == item:
            return index + 1
        elif index + 1 > item:
            return index
    return index + 1


def getNodeHn(neignborDic, H0Dic, node, n):
    if n == 0:
        return H0Dic[node]
    return getH([getNodeHn(neignborDic, H0Dic, neighborNode, n - 1) for neighborNode in neignborDic[node]])


def getGraphHn(G, n):
    HnDic = {}
    H0Dic = getGraphH0(G)
    neignborDic = getGraphneighbor(G)
    for node in nx.nodes(G):
        HnDic[node] = getNodeHn(neignborDic, H0Dic, node, n)
    return HnDic


def getGraph(graphFile):
    graphFileName, graphFileFormat = graphFile.split(".", 1)

    if graphFileFormat == 'edgelist':
        edgelist2gml.edgelist2gml(graphFile)
    elif graphFileFormat == 'net':
        net2gml.net2gml(graphFile)

    nxG = nx.read_gml(graphFileName + '.gml', label='id')
    return nxG

def HIndexJudgement(graphFile,n):
    G = getGraph(graphFile)

    star_time = time.perf_counter()
    GraphHnDic = getGraphHn(G, n)
    end_time = time.perf_counter()

    GraphHnSortedDicTuple = sorted(GraphHnDic.items(), key=lambda item: int(item[0]))
    GraphHnList = [dictuple[1] for dictuple in GraphHnSortedDicTuple]
    time_slice = end_time - star_time

    GraphHnSortedListString=[' '.join([str(NodeHnValue[0]),str(NodeHnValue[1])])+'\n' for NodeHnValue in GraphHnSortedDicTuple]
    with open('wang.txt','w') as f:
        f.writelines(GraphHnSortedListString)
        f.write(str(time_slice))
    print(GraphHnList, time_slice)
    return (time_slice,GraphHnList)

#if __name__ == '__main__':
#    # G = nx.read_edgelist('demo.edgelist', nodetype=int)
#    G = getGraph('demo.edgelist')
#
#    star_time = time.perf_counter()
#    GraphHnDic = getGraphHn(G, 3)
#    end_time = time.perf_counter()
#
#    GraphHnSortedDicTuple = sorted(GraphHnDic.items(), key=lambda item: item[0])
#    GraphHnList = [dictuple[1] for dictuple in GraphHnSortedDicTuple]
#    time_slice = end_time - star_time
#
#    GraphHnSortedListString=[' '.join([str(NodeHnValue[0]),str(NodeHnValue[1])])+'\n' for NodeHnValue in GraphHnSortedDicTuple]
#    with open('wang.txt','w') as f:
#        f.writelines(GraphHnSortedListString)
#        f.write(str(time_slice))
#    print(GraphHnList, time_slice)
