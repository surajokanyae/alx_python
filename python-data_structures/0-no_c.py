def no_c(my_string):
  """Removes all characters c and C from a string.

  Args:
    my_string: The string to be modified.

  Returns:
    The new string without characters c and C.
  """

  new_string = ""
  for char in my_string:
    code = ord(char)
    if code != ord("c") and code != ord("C"):
      new_string += char
  return new_string


def main():
  my_string = "Holberton School"
  print(no_c(my_string))
  my_string = "Chicago"
  print(no_c(my_string))
  my_string = "C is fun!"
  print(no_c(my_string))


if __name__ == "__main__":
  main()
