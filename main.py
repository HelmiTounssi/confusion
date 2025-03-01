class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)
 
    def add_edge(self, u, v):
        self.graph[u].append(v)
 
    def dfs_rec(self, v, visited):
        visited.add(v)
        for nb in self.graph[v]:
            if nb not in visited:
                self.dfs_rec(nb, visited)

    def dfs(self, v):
        visited = set()
        self.dfs_rec(v, visited)