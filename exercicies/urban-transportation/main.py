# FELIPE CARVALHO GODOI - 201920237
# PEDRO HENRIQUE MACIEL ALVES - 201920257
# Turma 10A

class Graph:
  def __init__(self):
    self.adjacencies = {}
  
  def add_edge(self, i, j):
    if i in self.adjacencies:
      self.adjacencies[i].append(j)
    else:
      self.adjacencies[i] = [j]
    
  def dfs(self):
    visited = set()
    ways = 1

    for vertex in self.adjacencies:
      if vertex not in visited:
        ways += self.depth_search(vertex, visited)

    return ways

  def depth_search(self, vertex, visited):
    visited.add(vertex)
    ways = 0

    if vertex in self.adjacencies:
      for neighbor in self.adjacencies[vertex]:
        if neighbor not in visited:
          ways += self.depth_search(neighbor, visited)
    else:
      ways += 1
  
    return ways
  
while 1:
  try:
    n,m = map(int, input().split())
    graph = Graph()

    for i in range(m):
      i,j = map(int, input().split())
      graph.add_edge(i,j)

    print(graph.dfs())

  except EOFError:   
    break
