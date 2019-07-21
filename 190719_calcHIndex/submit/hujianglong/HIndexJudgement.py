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
	igG = ig.Graph.Read_GML(graphFileName+'.gml')
	
	start_time = time.clock()
	# demo: 
	# result = calcH0IndexValues(nxG,igG)
	# result = calcH1IndexValues(nxG,igG)
	# your solution:
	result = calcHIndexValues(nxG,igG,n)
	end_time = time.clock()
	calcTime = end_time - start_time
	
	return (calcTime,result)
	
def calcH0IndexValues(nxG,igG):
	result = [nxG.degree(v) for v in nxG.nodes()]
	return result
	
def calcH1IndexValues(nxG,igG):
	# 准备工作0：计算网络的基本量
	number_of_nodes = nxG.number_of_nodes()
	# 准备工作1：存储一下各节点对应的下标
	nodesIndexDict = {node_i:i for i,node_i in enumerate(nxG.nodes())}
	# 准备工作2：计算每个节点的邻点下标组成的列表，并计算每个节点的邻点数量
	neighborsIndexesDict = {}
	neighborsNumberDict = {}
	for i,node_i in enumerate(nxG.nodes()):
		neighborsIndexesDict[i] = [nodesIndexDict[neighbor_j] for neighbor_j in nxG.neighbors(node_i)]
		neighborsNumberDict[i] = len(neighborsIndexesDict[i])
	
	# 步骤1：计算每个节点的度（也是H0值）
	degreeList = [nxG.degree(v) for v in nxG.nodes()]
	
	# 步骤2：计算每个节点的H1值
	h1ValuesList = []
	neighborsH0ValuesDict = {}
	for i in range(number_of_nodes):
		# 步骤2.1：计算当前节点的对应的由邻居节点的H0值由高到低组成的有序列表
		neighborsH0ValuesDict[i] = sorted([neighborsNumberDict[j] for j in neighborsIndexesDict[i]],reverse=True)
		# 步骤2.2：计算当前节点的h1值
		j = neighborsNumberDict[i]-1
		while (j+1)>neighborsH0ValuesDict[i][j]:
			j = j - 1
		h1ValuesList.append( j + 1 )
	return h1ValuesList	
	

	
def calcHIndexValues(nxG,igG,n):
	'''
	@params:
		nxG: networkx object;
		igG: igraph object;
		n: n-order;
	@return:
		results: n-order H Index values of graph, type: List;
	'''
	
	# 准备工作0：计算网络的基本量
	number_of_nodes = nxG.number_of_nodes()
	# 准备工作1：存储一下各节点对应的下标
	nodesIndexDict = {node_i:i for i,node_i in enumerate(nxG.nodes())}
	# 准备工作2：计算每个节点的邻点下标组成的列表，并计算每个节点的邻点数量
	neighborsIndexesDict = {}
	neighborsNumberDict = {}
	for i,node_i in enumerate(nxG.nodes()):
		neighborsIndexesDict[i] = [nodesIndexDict[neighbor_j] for neighbor_j in nxG.neighbors(node_i)]
		neighborsNumberDict[i] = len(neighborsIndexesDict[i])
	
	# 步骤0：计算每个节点的度（也是H0值）
	h0ValuesList = [nxG.degree(v) for v in nxG.nodes()]
	
	hAValuesList = h0ValuesList
	for times in range(n): #执行n次
		# 步骤X：计算每个节点的H1值
		hBValuesList = []
		neighborsHAValuesDict = {}
		for i in range(number_of_nodes):
			# 步骤X.1：计算当前节点的对应的由邻居节点的HA值由高到低组成的有序列表
			neighborsHAValuesDict[i] = sorted([hAValuesList[j] for j in neighborsIndexesDict[i]],reverse=True)
			# 步骤X.2：计算当前节点的hB值
			j = neighborsNumberDict[i]-1
			while (j+1)>neighborsHAValuesDict[i][j]:
				j = j - 1
			hBValuesList.append( j + 1 )
		hAValuesList = hBValuesList
	
	result = hBValuesList
	return result