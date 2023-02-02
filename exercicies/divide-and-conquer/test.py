def busca_binaria_sem_ordenar(array, target):
    closest_indices = None
    closest_distance = float("inf")

    for i in range(len(array) - 1):
        left = i + 1
        right = len(array) - 1
        while left <= right:
            mid = (left + right) // 2
            current_sum = array[i] + array[mid]

            if current_sum == target:
                return (i, mid)

            # Mantém a distância atual do alvo como a menor
            if abs(current_sum - target) < closest_distance:
                closest_distance = abs(current_sum - target)
                closest_indices = [i, mid]

            if array[i] + array[left] <= target:
                if abs(array[i] + array[left] - target) < closest_distance:
                    closest_distance = abs(array[i] + array[left] - target)
                    closest_indices = [i, left]
                left += 1
            elif array[i] + array[right] <= target:
                if abs(array[i] + array[right] - target) < closest_distance:
                    closest_distance = abs(array[i] + array[right] - target)
                    closest_indices = [i, right]
                right -= 1
            else:
                right -= 1

    return closest_indices


size = int(input())
array = [int(x) for x in input().split()]
sum = int(input())

result = busca_binaria_sem_ordenar(array, sum)
# result = busca_binaria_sem_ordenar(array, sum)
print(result)
