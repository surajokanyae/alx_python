def fibonacci_sequence(n):
  """
  Generates the first n Fibonacci numbers.

  Args:
    n: The number of Fibonacci numbers to generate.

  Returns:
    A list of the first n Fibonacci numbers.
  """

  if n < 0:
    return []
  fibonacci_numbers = []
  for i in range(n):
    if i == 0:
      fibonacci_numbers.append(0)
    elif i == 1:
      fibonacci_numbers.append(1)
    else:
      fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
  return fibonacci_numbers
