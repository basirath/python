class Graph:
    def __init__(self,n):
        self.graph = [[0]*n for i in range(n)]
        self.dic = {"H":0 , "B":1 , "K":2 , "G":3 , "P":4}
    def insert(self,u,v):
        u , v = self.dic[u] , self.dic[v]
        self.graph[u][v]=1
        self.graph[v][u]=1

obj = Graph(4)
obj.insert("H","B")
obj.insert("H","K")
obj.insert("H","G")
obj.insert("B","K")
for i in obj.graph:
    print(i)
