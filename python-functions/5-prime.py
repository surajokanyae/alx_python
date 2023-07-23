def is_prime(number):
  """
  Checks if a number is prime.

  Args:
    number: The number to check.

  Returns:
    True if the number is prime, and False otherwise.
  """

  if number <= 1:
    return False
  for i in range(2, number):
    if number % i == 0:
      return False
  return True
