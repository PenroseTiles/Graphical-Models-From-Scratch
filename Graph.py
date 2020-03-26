class Graph():
    def __init__(self):
        self.vertices = ['z1', 'z2']
        for i in range(1, 785):
            self.vertices.append('x' + str(i))
        self.edges = {vertex: [] for vertex in self.vertices}
        self.edges['z1'] = ['x' + str(i) for i in range(1, 785)]
        self.edges['z2'] = ['x' + str(i) for i in range(1, 785)]
        return

    def dfs_cycle(self, vertex, recstack, visited):
        # returns True if any cycles were found
        visited[vertex] = True
        recstack[vertex] = True
        ret = []
        for nbr in self.edges[vertex]:
            if recstack[nbr]:
                return True
            elif visited[nbr]:
                continue
            else:
                ret.append(self.dfs_cycle(nbr, recstack, visited))
        recstack[vertex] = False
        return any(ret)

    def dfs_isroot(self, vertex, visited, isroot):
        visited[vertex] = True
        for nbr in self.edges[vertex]:
            if visited[nbr]:
                continue
            else:
                isroot[nbr] = False
                self.dfs_isroot(nbr, visited, isroot)
        return

    def has_cycle(self):
        # check for cycles in every component of the graph
        components = []
        i = 0
        visited = {vertex: False for vertex in self.vertices}
        for i in range(len(self.vertices)):
            if visited[self.vertices[i]]:
                continue
            source = self.vertices[i]
            recstack = {vertex: False for vertex in self.vertices}
            components.append(self.dfs_cycle(source, recstack, visited))
        return any(components)

    def get_all_roots(self):
        isroot = {vertex: True for vertex in self.vertices}
        visited = {vertex: False for vertex in self.vertices}
        for i in range(len(self.vertices)):
            if visited[self.vertices[i]]:
                continue
            else:
                self.dfs_isroot(self.vertices[i], visited, isroot)
        return filter(lambda x: isroot.get(x, False), self.vertices)

    def reverse(self):
        rev = Graph()
        rev.edges = {vertex:[] for vertex in rev.vertices}
        for node in self.vertices:
            for nbr in self.edges[node]:
                rev.edges[nbr].append(node)
        print(rev.edges)
        return rev
