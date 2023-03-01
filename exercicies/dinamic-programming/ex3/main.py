# FELIPE CARVALHO GODOI - 201920237
# PEDRO HENRIQUE MACIEL ALVES - 201920257
# Turma 10A

def quantity(n, x, memoization):
  if (n,x) in memoization:
    return memoization[(n,x)]

  if n == 1:
    return x
  if x == 1:
    return 1
  
  memoization[(n,x)] = quantity(n-1, x, memoization) + quantity(n, x-1, memoization)

  return memoization[(n,x)]

while 1:
  n, x = map(int, input().split())
  if n == 0 and x == 0:
    break
  memoization = {}
  result = quantity(n,x, memoization)
  print(result%1000000)
  