from graph import Graph

g = Graph()
nodes = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

for i in nodes:
    g.addVertex(i, None)

"""for i in range(1, 5, 2):
    g.addEdge(nodes[i-(i%2)],nodes[i])
g.addEdge("E", "F")
g.addEdge("C", "B")
g.addEdge("B", "F")
g.addEdge("C", "F")"""
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
print(g.checkDegrees())
paths = g.find_all_H_paths("A", "J")
paths[0] = ["J", "I", "H", "G", "F", "E", "D", "C", "B", "A"]
#print(g._exchange(paths[0], []))
g.runThomason(paths[0])
