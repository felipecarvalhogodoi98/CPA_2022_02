# FELIPE CARVALHO GODOI - 201920237
# PEDRO HENRIQUE MACIEL ALVES - 201920257
# Turma 10A

def custo(n, x, y, matutina, vespertina):
  valor = 0
  for i in range(0, n):
    diferenca = (matutina[i] + vespertina[i]) - x
    if diferenca > 0:
      valor += diferenca*y
  return valor

while 1:
  n, x, y = map(int, input().split())

  if n == 0 and x == 0 and y == 0:
    break

  matutina = list(map(int, input().split()))
  vespertina = list(map(int, input().split()))

  matutina.sort()
  matutina = matutina[::-1]
  vespertina.sort()

  print(custo(n,x,y,matutina, vespertina))
  