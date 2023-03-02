import math

class Point:
  x = 0
  y = 0
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def dist(self, p):
    return math.pow(pow(self.x - p.x, 2) + pow(self.y - p.y, 2), 1/2)
  
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
    remaining = set(points)
    start = remaining.pop()
    current = start
    route = [start]
    while remaining:
        nearest = find_nearest(current, remaining)
        route.append(nearest)
        remaining.remove(nearest)
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