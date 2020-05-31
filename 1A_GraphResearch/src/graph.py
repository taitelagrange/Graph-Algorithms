
#imports

class Graph:
    def __init__(self):
        """
        -------------------------------------------------------
        Creates an empty graph.
        Use: graph = Graph()
        -------------------------------------------------------
        Postconditions:
            Initializes a graph. Size (number of vertices) is 0.
        -------------------------------------------------------
        """
        self._vertices = {}
        self._size = 0
        return

    def addVertex(self, key, edges):
        """
        -------------------------------------------------------
        Adds a node to the graph
        Use: graph.addVertex(key, edges)
        -------------------------------------------------------
        Preconditions:
            key - 'name' of vertex (str)
            edges - list of edges between new and pre-existing vertices (list of str)
                    None if none exist
        -------------------------------------------------------
        """
        if key not in self._vertices.keys():
            if edges is not None:
                self._vertices[key] = edges
            else:
                self._vertices[key] = []
            self._size += 1
        else:
            print("Vertex already exists.")
        return
    def addEdge(self, key1, key2):
        """
        -------------------------------------------------------
        Adds an edge between two given vertices.
        Use: graph.addEdge(key1, key2)
        -------------------------------------------------------
        Preconditions:
            key1 - first vertex (str)
            key2 - second vertex (str)
        -------------------------------------------------------
        """
        if key1 in self._vertices.keys() and key2 in self._vertices.keys():
            self._vertices[key1].append(key2)
            self._vertices[key2].append(key1)
        else:
            print("Invalid vertex.")
        return
    def getGraph(self):
        """
        -------------------------------------------------------
        Prints vertices and edges.
        Use: graph.getGraph()
        -------------------------------------------------------
        """
        for i, j in self._vertices.items():
            print(i, ":", sorted(j))
        return
    