from graph import Graph

g = Graph()
nodes = ["A", "B", "C", "D", "E", "F"]

for i in nodes:
    g.addVertex(i, None)

for i in range(1, 5, 2):
    g.addEdge(nodes[i-(i%2)],nodes[i])
g.addEdge("A", "C")
g.getGraph()