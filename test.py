def fibonacci(n):
  if not isinstance(n, int) or n < 0:
    raise ValueError("n must be a non-negative integer")
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)
  

def celsius_to_fahrenheit(celsius):
  if not isinstance(celsius, (int, float)):
    raise ValueError("celsius must be a number")
  return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
  if not isinstance(fahrenheit, (int, float)):
    raise ValueError("fahrenheit must be a number")
  return (fahrenheit - 32) * 5/9

def is_prime(n):
  if not isinstance(n, int) or n < 0:
    raise ValueError("n must be a non-negative integer")
  if n < 2:
    return False
  for i in range(2, int(n**0.5)+1):
    if n % i == 0:
      return False
  return True

print(fibonacci(6))