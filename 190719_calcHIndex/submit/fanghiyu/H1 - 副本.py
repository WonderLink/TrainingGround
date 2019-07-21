# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 17:38:40 2019

@author: 77365
"""

import networkx as nx
G=nx.read_edgelist('karate.edgelist')

def H(G):
    n=2#所求阶数（大于等于1）
    x=1#一阶H1，取值为0（原始度）或1（当所求阶数大于等于1）
    #原始度H0
#    print('H',0)
#    degree_dict = [nx.degree(G, v) for v in range(G.number_of_nodes())]
#    neighbors=[nx.neighbors(G,i) for i in range(G.number_of_nodes())]
#    aa=[]
#    for v in neighbors.values():
#        aa.append(degree_dict[v])
#        neignode_de[a]=aa
#    print(degree_dict)
    degree_dict={}
    neighbors={}
    neignode_de={}
    for u in G:
        degree_dict[u]=nx.degree(G,u)#节点度
        neighbors[u]=nx.neighbors(G,u)#节点邻居
        nodegree=[]
        for v in neighbors[u]:
            nodegree.append(nx.degree(G,v))
            neignode_de[u]=nodegree#节点邻居度
#    print(degree_dict)
    
    while n>=x>0:#从H1开始
#        print('H',x)#阶数
        x=x+1
        for a,b in neignode_de.items():
            N = len(b)
            b.sort()
            h = 0
            for i, c in enumerate(b):
                h = max(h, min(N - i, c))
                degree_dict[a]=h  
#        print(degree_dict)  
        for a in neignode_de.keys():
            s=[]
            for e in neighbors[a]:
                s.append(degree_dict[e])
                neignode_de[a]=s  

    nf=open("result.txt","w")
    for k,v in degree_dict.items():
        nf.write('{}\t{}\n'.format(k,v))
    nf.close()
H(G)