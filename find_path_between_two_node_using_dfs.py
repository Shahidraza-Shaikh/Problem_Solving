from collections import defaultdict

graph = defaultdict(list)

edges = [[0,1],[0,2],[1,2],[2,3],[2,1],[3,3]]

for edge in edges:
	x,y = edge 

	graph[x].append(y)


def dfs(start,vis,dest):

	vis.add(start)
	if start ==dest :

		return True

	
	for neighbour in graph[start] :
		if neighbour not in vis:


			return dfs(neighbour,vis,dest)


def call_dfs(start,dest):

	visited = set()

	if dfs(start,visited,dest) :
		print(f"we can go from {start} to {dest}")
	else:
		print(f"There is not path from {start} to {dest}")

call_dfs(2,0)