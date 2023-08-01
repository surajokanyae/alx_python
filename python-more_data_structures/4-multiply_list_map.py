def multiply_list_map(my_list=[], number=0):
  """Returns a list with all values multiplied by a number without using any loops.

  Args:
    my_list: The list to multiply.
    number: The number to multiply by.

  Returns:
    A new list:
      Same length as my_list
      Each value should be multiplied by number
    Initial list should not be modified
  """

  return list(map(lambda x: number * x, my_list))


if __name__ == "__main__":
  my_list = [1, 2, 3, 4, 6]
  new_list = multiply_list_map(my_list, 4)
  print(new_list)
  print(my_list)
