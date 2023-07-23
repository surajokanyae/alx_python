def reverse_string(string):
  """
  Reverses a string.

  Args:
    string: The string to reverse.

  Returns:
    The reversed string.
  """

  if type(string) is not str:
    raise TypeError("string must be a string")
  reversed_string = ""
  for i in range(len(string) - 1, -1, -1):
    reversed_string += string[i]
  return reversed_string
