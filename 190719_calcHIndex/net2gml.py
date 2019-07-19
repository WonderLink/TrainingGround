import igraph as ig
import networkx as nx

def net2gml(netFormatFile):
	igG = ig.Graph.Read_Pajek(netFormatFile)
	igG = igG.simplify(igG) #去除重复边
	nodes = igG.vs()
	for i in range(len(nodes)):
		igG.vs[i]["label"] = str(i+1)
	netFormatFileName = netFormatFile.split(".",1)[0] #分割1次
	ig.Graph.write_gml(igG,netFormatFileName+".gml")
