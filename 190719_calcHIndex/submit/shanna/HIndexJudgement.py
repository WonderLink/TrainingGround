import networkx as nx


# 计算h_index
def count_h_index(h_list):
    # 降序排序
    h_list = sorted(h_list, reverse=True)
    _len = len(h_list)
    i = 0
    while (i < _len and h_list[i] > i):
        i += 1
    return i


def cal_h_index(G, n, h_neg_dic):
    assert n >= 0, 'n>=0'  # 保证n>=0,否则报错

    # 0阶
    if n == 0:
        h_index_dic = {}  # 每个节点的0阶h指数
        for n_i in nx.nodes(G):
            h_index_dic[n_i] = nx.degree(G, n_i)
        return h_index_dic
    else:
        h_index_dic = {}
        n = n - 1
        h0_index_dic = cal_h_index(G, n, h_neg_dic)
        # print(n,h0_index_dic)
        for n_i in nx.nodes(G):
            h_list = []
            for neg in h_neg_dic[n_i]:
                h_list.append(h0_index_dic[neg])
            h_index_dic[n_i] = count_h_index(h_list)
        return h_index_dic


def HIndexJudgement(filename, n):
    G = nx.read_edgelist(filename, nodetype=int)  # 如果输入不是filename的话，我这里可以省很多时间
    h_neg_dic = {}  # 保存每个节点的邻居节点
    for n_i in nx.nodes(G):
        a = []
        for neg in nx.neighbors(G, n_i):
            a.append(neg)
        h_neg_dic[n_i] = a

    result_dic = cal_h_index(G, n, h_neg_dic)
    result_list = []
    for val in result_dic.values():
        result_list.append(val)

    # print(result_list)
    return result_list


HIndexJudgement('polblogs.edgelist', 0)
#!/usr/bin/env python

# -*- coding: UTF-8 -*-

'''

@author: Hannah

@file: HIndexJudgement.py

@time: 2019/7/21 9:34

'''
import networkx as nx

#计算h_index
def count_h_index(h_list):
    #降序排序
    h_list = sorted(h_list, reverse=True)
    _len = len(h_list)
    i = 0
    while(i<_len and h_list[i]>i):
        i += 1
    return i


def cal_h_index(G,n,h_neg_dic):
    assert n >= 0, 'n>=0' #保证n>=0,否则报错

    #0阶
    if n == 0:
        h_index_dic = {} #每个节点的0阶h指数
        for n_i in nx.nodes(G):
            h_index_dic[n_i] = nx.degree(G,n_i)
        return h_index_dic
    else :
        h_index_dic = {}
        n = n-1
        h0_index_dic = cal_h_index(G,n,h_neg_dic)
        # print(n,h0_index_dic)
        for n_i in nx.nodes(G):
            h_list = []
            for neg in h_neg_dic[n_i]:
                h_list.append(h0_index_dic[neg])
            h_index_dic[n_i] = count_h_index(h_list)
        return h_index_dic

def HIndexJudgement(filename,n):
    G = nx.read_edgelist(filename, nodetype=int)  # 如果输入不是filename的话，我这里可以省很多时间
    h_neg_dic = {}  # 保存每个节点的邻居节点
    for n_i in nx.nodes(G):
        a = []
        for neg in nx.neighbors(G, n_i):
            a.append(neg)
        h_neg_dic[n_i] = a


    result_dic = cal_h_index(G,n,h_neg_dic)
    result_list = []
    for val in result_dic.values():
        result_list.append(val)

    return result_list

# HIndexJudgement('polblogs.edgelist',0)