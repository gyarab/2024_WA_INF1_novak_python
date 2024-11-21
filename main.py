def fibonacci(n):
  if not isinstance(n, int) or n <= 0:
    return []
  elif n == 1:
    return [0]
  elif n == 2:
    return [0, 1]
  
  sequence = [0, 1]
  for i in range(2, n):
    next_value = sequence[-1] + sequence[-2]
    sequence.append(next_value)
  
  return sequence

print(fibonacci(10))