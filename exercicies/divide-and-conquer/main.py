import numpy as np

def merge(array, begin, mid, end):
  sizeLeft = mid - begin + 1
  sizeRight = end - mid

  L = np.arange(sizeLeft)
  R = np.arange(sizeRight)

  for i in range(0, sizeLeft):
    L[i] = array[begin + i]
  for i in range(sizeRight):
    R[i] = array[mid + i + 1]

  i = 0
  j = 0
  k = begin

  while i < len(L) and j < len(R):
    if L[i] <= R[j]:
      array[k] = L[i]
      i += 1
    else:
      array[k] = R[j]
      j += 1
    k += 1
 
  while i < len(L):
    array[k] = L[i]
    i += 1
    k += 1

  while j < len(R):
    array[k] = R[j]
    j += 1
    k += 1

  return array

def merge_sort(array, begin, end):
  if begin < end:
    mid = int((begin + end) / 2)
    merge_sort(array, begin, mid)
    merge_sort(array, mid + 1, end)

    return merge(array, begin, mid, end)
  
  return array

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
  merge_sort(array, 0, len(array) - 1)                            # O(nlgn)
  for i in range(size):                                           # O(nlgn)
    diffSumCurrent = abs(value - array[i])
    resultIndex = binary_search(array, 0, size - 1, diffSumCurrent)         
    if resultIndex != -1:
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
