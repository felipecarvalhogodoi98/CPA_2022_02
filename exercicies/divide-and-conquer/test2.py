def find_min_price_difference(prices, b):
  prices = sorted(prices)
  min_difference = float('inf')
  left = 0
  right = len(prices) - 1

  itemI = 0
  itemJ = 0

  while left < right:
    current_sum = prices[left] + prices[right]
    if current_sum == b:
      itemI = prices[left]
      itemJ = prices[right]
      if abs(b - current_sum) < min_difference:
        min_difference = abs(b - current_sum)
    if current_sum < b:
      left += 1
    else:
      right -= 1

  return [itemI, itemJ]

n = int(input())
prices = [int(x) for x in input().split()]
b = int(input())
result = find_min_price_difference(prices, b)
print(result[0], result[1])