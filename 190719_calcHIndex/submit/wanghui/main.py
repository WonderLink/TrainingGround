import networkx as nx

def HIndex(G,number):
    # G = nx.read_edgelist(network)
    N = number
    neighbors = {}  # key为节点 value为节点邻居的list
    nodes = G.nodes()
    for node in nodes:
        neighbors[node] = []
        for i in G.neighbors(node):
            neighbors[node].append(i)
    h_index = H_index(G, N, neighbors)
    # print(h_index)
    # h_index = dict(sorted(h_index.items(), key=lambda item: int(item[0]), reverse=False))
    result = []
    for i in h_index.values():
        result.append(i)
    return result
    # filename = 'result/dolphins_5' + str(n) + '.txt'
    # with open(filename, 'w') as file:
    #     for a, b in h_index.items():
    #         file.write(str(a) + ' ' + str(b) + '\n')
    #
    #     file.close()



def H_index(G, n, neighbors):  #G为网络 n为H_index的阶数
    if n == 1:
        degrees = {}
        nodes = G.nodes()
        h_index = {}
        for node in nodes:
            degrees[node] = G.degree(node)
        for node in nodes:
            h_index[node] = 0
            for i in range(1,degrees[node]+1):
                count = 0
                for neighbor in neighbors[node]:
                    if degrees[neighbor] >= i:
                        count += 1
                if count >= i:
                    h_index[node] = i
                else:
                    break
        return h_index
    else:
        degrees = H_index(G, n-1, neighbors)
        nodes = G.nodes()
        h_index = {}
        # for node in nodes:
        #     degrees[node] = G.degree(node)
        for node in nodes:
            h_index[node] = 0
            for i in range(1, degrees[node] + 1):
                count = 0
                for neighbor in neighbors[node]:
                    if degrees[neighbor] >= i:
                        count += 1
                if count >= i:
                    h_index[node] = i
                else:
                    break
        return h_index


        return neighbors

