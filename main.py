class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)
 
    def add_edge(self, u, v):
        self.graph[u].append(v)
 
    def dfs_rec(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.dfs_rec(neighbour, visited)

    def dfs(self, v):
        visited = set()
        self.dfs_rec(v, visited)