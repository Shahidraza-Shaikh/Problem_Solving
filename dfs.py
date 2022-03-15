from collections import defaultdict

graph = defaultdict(list)

edges = [[0,1],[0,2],[1,2],[2,0],[2,3],[3,3]]

for edge in edges:
	x,y = edge 

	graph[x].append(y)

# st = []
print(graph)
def dfs(start,vis):

	vis.add(start)
	print(start,end="->")

	for neighbour in graph[start] :
		if neighbour not in vis:

			dfs(neighbour,vis)


def call_dfs(start):

	visited = set()

	dfs(start,visited)
call_dfs(2)