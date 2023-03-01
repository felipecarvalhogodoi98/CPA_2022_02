# FELIPE CARVALHO GODOI - 201920237
# PEDRO HENRIQUE MACIEL ALVES - 201920257
# Turma 10A

def binary_search(array, left, right, item):
  if right < left:
    return -1
  mid = (left + right) // 2
  if array[mid] == item:
    return mid
  elif array[mid] > item:
    return binary_search(array, left, mid - 1, item)
  else: 
    return binary_search(array, mid + 1, right, item)

def check_suppliers(array, value):
  pi = 0
  pj = 0
  minSum = 1000001

  size = len(array)
  array = sorted(array)                                               # O(nlgn)
  for i in range(size):                                               # O(nlgn)
    diffSumCurrent = abs(value - array[i])
    resultIndex = binary_search(array, 0, size - 1, diffSumCurrent)
    if resultIndex != -1 and resultIndex != i:
      piCurrent = array[i]
      pjCurrent = array[resultIndex]
      diff = max(piCurrent, pjCurrent) - min(piCurrent, pjCurrent)    
      if diff < minSum:
        minSum = diff
        pi = piCurrent
        pj = pjCurrent

  return [min(pi, pj), max(pi, pj)]

#main
size = int(input())
array = [int(x) for x in input().split()]
sum = int(input())

result = check_suppliers(array, sum)
print(result[0], result[1])
