from graph import Graph

g = Graph()
nodes = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

for i in nodes:
    g.addVertex(i, None)

g.addEdge("A","B")
g.addEdge("A","J")
g.addEdge("A","F")
g.addEdge("B","C")
g.addEdge("B","J")
g.addEdge("C","I")
g.addEdge("C","D")
g.addEdge("D","H")
g.addEdge("D","E")
g.addEdge("E","F")
g.addEdge("E","G")
g.addEdge("F","G")
g.addEdge("G","H")
g.addEdge("H","I")
g.addEdge("I","J")

g.getGraph()
path = ["J", "I", "H", "G", "F", "E", "D", "C", "B", "A"]
g.runThomason(path)
