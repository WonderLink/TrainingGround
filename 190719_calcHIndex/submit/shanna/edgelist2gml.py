import networkx as nx

def edgelist2gml(edgelistFormatFile):
	nxG = nx.read_edgelist(edgelistFormatFile)
	edgelistFormatFileName = edgelistFormatFile.split(".",1)[0] #分割1次
	nx.write_gml(nxG,edgelistFormatFileName+".gml")