class Graph:
    def __init__(self):
         self.graph = {}

    def insert(self,u,v=""):
         if v=="":
             self.graph[u]=[]
             return
         for i in range(2):
             if u in self.graph:
                 self.graph[u].append(v)
             else:
                 self.graph[u]=[v]
             u , v = v , u

obj  = Graph()
obj.insert("H","B")
obj.insert("H","K")
obj.insert("H","G")
obj.insert("K","B")
obj.insert("P")
obj.insert("M")
print(obj.graph)


