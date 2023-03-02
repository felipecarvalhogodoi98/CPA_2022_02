# FELIPE CARVALHO GODOI - 201920237
# PEDRO HENRIQUE MACIEL ALVES - 201920257
# Turma 10A

class Point:
  x = 0
  y = 0
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def dist(self, p):
    return pow(pow(self.x - p.x, 2) + pow(self.y - p.y, 2), 1/2)
  
def find_nearest(point, candidates):
    nearest = None
    min_distance = float("inf")
    for candidate in candidates:
        distance = point.dist(candidate)
        if distance < min_distance:
            nearest = candidate
            min_distance = distance
    return nearest

def tsp(points):
    start = points.pop(0)
    current = start
    route = [start]
    while len(points) > 0:
        nearest = find_nearest(current, points)
        route.append(nearest)
        points.remove(nearest)
        current = nearest
    route.append(start)
    return route

def cost(points):
  min_route = tsp(points)

  min_distance = 0
  for i in range(len(min_route) - 1):
      min_distance += min_route[i].dist(min_route[i+1])
  
  return round(min_distance, 1)

while 1:
  try:
    line = input()
  except EOFError:   
    break

  quantity = int(line) if line != '' else 0
  points = []

  if quantity > 0:
    for i in range(quantity):
      x, y = map(int, input().split())
      p = Point(x,y)
      points.append(p)
    print(cost(points))