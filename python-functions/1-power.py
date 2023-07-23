def pow(a, b):
  """
  Computes a to the power of b and returns the value.

  Args:
    a: The base number.
    b: The exponent.

  Returns:
    The value of a to the power of b.
  """

  if type(a) is not int or type(b) is not int:
    raise TypeError("a and b must be integers")
  if b < 0:
    return 1 / pow(a, -b)
  else:
    result = 1
    for _ in range(b):
      result *= a
    return result
