# FELIPE CARVALHO GODOI - 201920237
# PEDRO HENRIQUE MACIEL ALVES - 201920257
# Turma 10A

num_swaps = 0

def merge_sort(arr):
    global num_swaps
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            num_swaps += len(left) - i
    
    result += left[i:]
    result += right[j:]
    
    return result



while 1:
  try:
    line = input()
  except EOFError:   
    break
  array_str = line.split()
  if len(array_str) > 0:
    array = [int(num) for num in array_str]
    array.pop(0)
    num_swaps = 0
    merge_sort(array)
    print("Eder" if num_swaps % 2 == 0 else "Wando")

