

#function used to find shortest distances
def dijkstrasAlgorithm(start, edges):
	unvisitedEdges = [False] * len(edges)
	tableofShortestPaths = [-1] * len(edges)
	#update the table for the first node
	if len(edges[start]) == 0:
		tableofShortestPaths[start] = 0
		return tableofShortestPaths
	node = start
	tableofShortestPaths[node] = 0
	while unvisitedEdges[node] is False:
		
		if len(edges[node]) == 0:
			unvisitedEdges[node] = True
			return tableofShortestPaths
		tableofShortestPaths = updateTableOfShortestPaths(tableofShortestPaths, node, edges, tableofShortestPaths[node])
		currentNode = node
		unvisitedEdges = updateUnvisitedEdges(unvisitedEdges, node)
		node = findNextNode(edges, node, unvisitedEdges)
	#execute passthrough of table here
	
	for i in range(len(unvisitedEdges)):
		if unvisitedEdges[i] is False and tableofShortestPaths[i] != -1:
			tableofShortestPaths = updateTableOfShortestPaths(tableofShortestPaths, i, edges, tableofShortestPaths[i])
	
	return tableofShortestPaths

#function used to find paths that acquired shortest distances
def dijkstrasAlgorithmNodePath(start, edges):
	unvisitedEdges = [False] * len(edges)
	tableofShortestPaths = [-1] * len(edges)
	#update the table for the first node
	if len(edges[start]) == 0:
		tableofShortestPaths[start] = 0
		return tableofShortestPaths
	node = start
	tableofShortestPaths[node] = 0
	seenLocations = []
	while unvisitedEdges[node] is False:
		
		if len(edges[node]) == 0:
			unvisitedEdges[node] = True
			return tableofShortestPaths
		tableofShortestPaths = updateTableOfShortestPaths(tableofShortestPaths, node, edges, tableofShortestPaths[node])
		currentNode = node
		unvisitedEdges = updateUnvisitedEdges(unvisitedEdges, node)
		node = findNextNode(edges, node, unvisitedEdges)
		seenLocations.append(node)
	#execute passthrough of table here
	
	for i in range(len(unvisitedEdges)):
		if unvisitedEdges[i] is False and tableofShortestPaths[i] != -1:
			tableofShortestPaths = updateTableOfShortestPaths(tableofShortestPaths, i, edges, tableofShortestPaths[i])
	
	return seenLocations
	

def updateTableOfShortestPaths(tableofShortestPaths, node, edges, minDistance):
	for i in range(0, len(edges[node])):
		
		updateNode = edges[node][i][0]
		distance = edges[node][i][1] + minDistance
		if tableofShortestPaths[updateNode] == -1 or distance < tableofShortestPaths[updateNode]:
			tableofShortestPaths[updateNode] = distance

	return tableofShortestPaths
			
			
def updateUnvisitedEdges(unvisitedEdges, node):
	unvisitedEdges[node] = True
	return unvisitedEdges

def findNextNode(edges, currentNode, unvisitedEdges):
	nextNode = edges[currentNode][0][0]
	minValue = edges[currentNode][0][1]
	if len(edges[currentNode]) == 1:
		nextNode = edges[currentNode][0][0]
	else:
		for i in range(1, len(edges[currentNode])):
			if minValue > edges[currentNode][i][1] and len(edges[edges[currentNode][i][0]]) != 0 and unvisitedEdges[edges[currentNode][i][0]] is False:
				nextNode = edges[currentNode][i][0]
				minValue = edges[currentNode][i][1]
			else:
				continue
	return nextNode

val = input("Enter the school you are starting from: ");
arr = ["Northpark", "Desert View", "Westridge", "Stagecoach", "Sage", "Eastside", "CAB", "RSJH", "RSHS", "Headstart", "Overland"]
if val == "Northpark" :
	start = 0
elif val == "Desert View":
	start = 1
elif val == "Westridge":
	start = 2
elif val == "Stagecoach":
	start = 3
elif val == "Sage":
	start = 4
elif val == "Eastside":
	start = 5
elif val == "CAB":
	start = 6
elif val == "RSJH":
	start = 7
elif val == "RSHS":
	start = 8
elif val == "Headstart":
	start = 9
elif val == "Overland":
	start = 10


edges = [
	[[1, 2.8], [2, 4.6], [3, 3.3],[4, 4.1], [5, 4.1],[6, 0.2],[7, 4.0], [8, 6.2],[9, 4.6], [10, 3.8]], 
	[[0, 2.8], [2, 4.2], [3, 2.6], [4, 3.3], [5, 3.0], [6, 2.8], [7, 3.2], [8, 4.3], [9, 2.4], [10, 3.0]], 
	[[0, 4.6], [1, 4.2], [3, 1.8], [4, 1.1], [5, 3.8], [6, 1.5], [7, 1.5], [8, 6.6], [9, 3.4], [10, 1.3]],
    [[0, 3.3], [1, 2.6], [2, 1.8], [4, 1.0], [5, 3.6], [6, 1.5], [7, 1.9], [8, 5.7], [9, 3.2], [10, 1.7]], 
	[[0, 4.1], [1, 3.3], [2, 1.1], [3, 1.0], [5, 3.9], [6, 1.3], [7, 1.7], [8, 6.0], [9, 3.5], [10, 1.5]], 
	[[0, 4.1], [1, 3.0], [2, 3.8], [3, 3.6], [4, 3.9], [6, 3.2], [7, 3.6], [8, .7], [9, .8], [10, 3.3]], 
	[[0, .5], [1, 2.8], [2, 1.5], [3, 1.5], [4, 1.3], [5, 3.2], [7, .2], [8, 5.3], [9, 2.8], [10, .3]], 
	[[0, 4.0], [1, 3.2], [2, 1.5], [3, 1.9], [4, 1.7], [5, 3.6], [6, .5], [8, 5.6], [9, 3.1], [10, .2]], 
	[[0, 6.2], [1, 4.3], [2, 6.6], [3, 5.7], [4, 6.0], [5, .7], [6, 5.3], [7, 5.6], [9, 1.4], [10, 5.4]], 
	[[0, 4.6], [1, 2.4], [2, 3.4], [3, 3.2], [4, 3.5], [5, .8], [6, 2.8], [7, 3.2], [8, 1.4], [10, 2.9]],
	[[0, 3.8], [1, 3.0], [2, 1.3], [3, 1.7], [4, 1.5], [5, 3.3], [6, .3], [7, .2], [8, 5.4], [9, 2.9]]
	]
	
output = dijkstrasAlgorithm(start, edges);
seen = dijkstrasAlgorithmNodePath(start, edges);
for i in range(len(output)):
	if seen[i] > output[i]:
		print("Distance to: " + arr[i] + " " + str(output[i]) + " miles.  Previous visited school: None\n")
	else:
		print("Distance to: " + arr[i] + " " + str(output[i]) + " miles.  Previous visited school: " + str(arr[seen[i]]) + "\n")
