from collections import defaultdict


class Graph:

	def __init__(self):

		self.graph = defaultdict(list)

	def addEdge(self,u,v):

		self.graph[u].append(v)

	def dfs_function(self,v,visited):

		visited.add(v)
		print(v,end=" ")

		for  neighbour in self.graph[v]:

			if neighbour not in visited:

				visited.add(neighbour)
				self.dfs(neighbour,visited)

	def dfs(self,v):

		visited = set()

		self.dfs_function(v,visited)

graph = Graph()

graph.addEdge(0,1)
graph.addEdge(0,2)
graph.addEdge(1,2)
graph.addEdge(2,0)
graph.addEdge(2,3)
graph.addEdge(3,3)


graph.dfs(2)