import time

from wangjie import *

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
	'''
	@params:
		nxG: networkx object;
		igG: igraph object;
		n: n-order;
	@return:
		results: n-order H Index values of graph, type: List;
	'''
    GraphHnDic = getGraphHn(nxG, n)
    GraphHnSortedDicTuple = sorted(GraphHnDic.items(), key=lambda item: item[0])
    result = [dictuple[1] for dictuple in GraphHnSortedDicTuple]
	return result
