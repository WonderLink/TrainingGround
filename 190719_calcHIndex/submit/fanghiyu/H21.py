# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 10:59:54 2019

@author: 95768
"""

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
	# demo: result = calcH0IndexValues(nxG,igG)
	# your solution:
	result = calcHIndexValues(nxG,igG,n)
	end_time = time.clock()
	calcTime = end_time - start_time
	
	return (result,calcTime)
	
def calcH0IndexValues(nxG,igG):
	result = [nxG.degree(v) for v in nx.nodes(nxG)]
	return result
	
#计算h_index
def Hindex(G,n):
    x=1#一阶H1，取值为0（原始度）或1（当所求阶数大于等于1）
    #原始度H0
#    degree_dict = [nx.degree(G, v) for v in range(G.number_of_nodes())]
#    neighbors=[nx.neighbors(G,i) for i in range(G.number_of_nodes())]
    degree_dict={}
    neighborsa={}
    neignode_de={}
    for u in G:
        degree_dict[u]=nx.degree(G,u)#节点度
        neighborsa[u]=list(nx.neighbors(G,u))#节点邻居        
        nodegree=[]
        for v in neighborsa[u]:
            nodegree.append(nx.degree(G,v))
            neignode_de[u]=nodegree#节点邻居度
    while n>=x>0:#从H1开始
        x=x+1
        for a,b in neignode_de.items():
            N = len(b)
            b.sort()
            h = 0
            for i, c in enumerate(b):
                h = max(h, min(N - i, c))
                degree_dict[a]=h  
        for a in neignode_de.keys():
            s=[]
            for e in neighborsa[a]:
                s.append(degree_dict[e])
                neignode_de[a]=s 
    return degree_dict



def calcHIndexValues(nxG,igG,n):
     result_dic = Hindex(nxG,n)
     result = []
     for val in result_dic.values():
         result.append(val)
     return result
