import time

import networkx as nx
import igraph as ig

import edgelist2gml
import net2gml

def HIndexJudgement(graphFile,n):
	'''
	@author:
		JianglongHu@github.com
	@params:
		graphFile: full name of input graph;
	@return:
		calcTime: time for calculation;
		result: n-order H Index values of graph, type: List;
	'''
	graphFileName, graphFileFormat = graphFile.split(".",1)
	
	if graphFileFormat=='edgelist':
		edgelist2gml.edgelist2gml(graphFile)
	elif graphFileFormat=='net':
		net2gml.net2gml(graphFile)
	
	nxG = nx.read_gml(graphFileName+'.gml')
	#nxG = nx.convert_node_labels_to_integers(nxG)
	igG = ig.Graph.Read_GML(graphFileName+'.gml')
	
	start_time = time.clock()
	# demo: result = calcH0IndexValues(nxG,igG)
	# your solution:
	result = calcHIndexValues(nxG,igG,n)
	end_time = time.clock()
	calcTime = end_time - start_time
	
	return (calcTime,result)
	
def calcH0IndexValues(nxG,igG):
	result = [nxG.degree(v) for v in nx.nodes(nxG)]
	return result
	
def calcHIndexValues(nxG,igG,n):
	nxG = nx.convert_node_labels_to_integers(nxG)
	nodes = nxG.nodes()
	degree={}
	for i in nodes:
		degree[i]=[nx.degree(nxG,i)]
	for i in range(n+1):
		if i==0:
			continue
		for j in nodes:
			degree[j].append(hIndex([degree[x][i-1] for x in nx.neighbors(nxG,j)]))
	return [degree[i][n] for i in sorted(degree)]


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

'''
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
'''