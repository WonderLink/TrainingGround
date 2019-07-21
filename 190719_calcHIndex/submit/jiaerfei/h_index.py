# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 10:44:04 2019

@author: JEF
"""

import networkx as nx
 


def neighbor_degree(G, node):
    neighbor_degree_list = []
    for neighbor in nx.neighbors(G, node):
        neighbor_degree_list.append(G.degree(neighbor))
    return neighbor_degree_list

def h_index(G ,index_list): 
    index_list = sorted(index_list, reverse = True) #降序
    for i, c in enumerate(index_list):
        if i >= c:
            return i
    return len(index_list)     


def h_index_n(G_test, n):
    G = nx.read_edgelist('./dataset/{}'.format(G_test),nodetype = int)
    h_dic = {}
    neighbor_h_index_list = []
    nodes = nx.nodes(G)
    for node in nodes:
        neighbor_degree_list = neighbor_degree(G, node)
        h_dic[node] = h_index(G, neighbor_degree_list)
    h_index_dic = h_dic.copy()
    for node in nodes:
        for neighbor in nx.neighbors(G, node):
            neighbor_h_index_list.append(h_index_dic[neighbor])
        if n == 0:
            h_index_dic[node] = G.degree(node)
        if n == 1:
            h_index_dic[node] = h_index(G, neighbor_degree_list)
        if n == 2:
            h_index_dic[node] = h_index(G, neighbor_h_index_list)
        if n > 2:
            h_index_dic = h_index_n(G_test, n-1)
        neighbor_h_index_list = []
    
    return h_index_dic
    
    
h_index_n = h_index_n('dolphins.edgelist', 0)
    
        