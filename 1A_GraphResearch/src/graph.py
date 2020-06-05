
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
        self._exchanges = 0
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
        Adds an edge between two given vertices. Edge must not already exist.
        Vertices must already exist.
        Use: graph.addEdge(key1, key2)
        -------------------------------------------------------
        Preconditions:
            key1 - first vertex (str)
            key2 - second vertex (str)
        -------------------------------------------------------
        """
        if key1 in self._vertices.keys() and key2 in self._vertices.keys() and key2 not in self._vertices[key1]:
            self._vertices[key1].append(key2)
            self._vertices[key2].append(key1)
        else:
            print("Invalid edge.")
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
    
    def checkDegrees(self):
        """
        -------------------------------------------------------
        Asserts that all vertices in the graph are odd degree.
        Use: valid = graph.checkDegrees()
        -------------------------------------------------------
        Postconditions:
            True if all vertices of odd degree, False otherwise
        -------------------------------------------------------
        """
        for i in self._vertices.keys():
            if len(self._vertices[i]) % 2 == 0:
                return False
        return True
    
    def find_all_H_paths(self, start, end, path=[]):
        """
        Sourced from https://www.python.org/doc/essays/graphs/ with minor modifications.
        ******For testing
        """
        path = path + [start]
        if start == end:
            return [path]
        if start not in self._vertices.keys():
            return []
        paths = []
        for node in self._vertices[start]:
            if node not in path:
                newpaths = self.find_all_H_paths( node, end, path)
                for newpath in newpaths:
                    if len(newpath) == self._size:
                        paths.append(newpath)
        return paths
    
    def _exchange(self, path, removed):
        """
        -------------------------------------------------------
        Helper function. Performs an exchange between an edge connected to the
        last vertex but not in the path and an edge in the path to create a new path.
        Use: graph._exchange(path)
        -------------------------------------------------------
        Preconditions:
            path - vertices in order of traversal from start to finish (list of str)
            removed - edges already deleted through exchange (list of str)
        -------------------------------------------------------
        """
        flag = 0
        newpath = []
        #get edge to add
        i = 0
        newend = self._vertices[path[-1]][i]
        newedge = [path[-1], newend]
        
        while (newend is path[0] or newedge == removed or path[-2] == newend) and i < len(self._vertices[path[-1]])-1:
            i+=1
            newend = self._vertices[path[-1]][i]
            newedge = [path[-1], newend]
            
        if newedge == removed:
            #no exchange possible
            return None, None
        i = 0
        
        #add new edge and remove edge
        while path[i] != newend:
            newpath.append(path[i])
            i+=1
        newpath.append(newend)
        for j in path[len(path):i:-1]:
            newpath.append(j)
                
        #print(newpath)
        #removed.append([newpath[-1], newend])
        removed = [newpath[-1], newend]
        self._exchanges += 1
        if newpath[0] in self._vertices[newpath[-1]]:
            flag = 1
        return newpath, removed, flag
        
    def runThomason(self, path):
        """
        -------------------------------------------------------
        Runs Thomason's Algorithm on a given graph. Every vertex must be of odd degree.
        Use: graph.runThomason(edge, path)
        -------------------------------------------------------
        Preconditions:
            edge - the edge that must be contained in every cycle, the starting edge
                    of the path in form [v1, v2] (list of str)
            path - vertices in order of traversal from start to finish (list of str)
        Postconditions:
        
        -------------------------------------------------------
        """
        if not self.checkDegrees():
            #not a valid graph for algorithm
            return
        
        #exchangeG = Graph()
        removed = []
        newpath = path
        flag = 0
        while newpath is not None and not flag:
            newpath, removed, flag = self._exchange(newpath, removed)
            """"if newpath is not None:
                exchangeG.addVertex(newpath, None)
                exchangeG.addEdge(newpath, )"""
            print(newpath, removed)
     
        #create exchange graph
        #possibly make it only store last removed edge, in case there is new path with that edge
        #would need to check H path is not already in graph, otherwise infinite loop
        return
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
