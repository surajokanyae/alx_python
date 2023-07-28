def print_matrix_integer(matrix=[[]]):
  """Prints a matrix of integers.

  Args:
    matrix: The matrix to be printed.

  Returns:
    Nothing.
  """

  if not matrix:
    print("")
    return

  for row in matrix:
    for item in row:
      print("{:3}".format(item), end=" ")
    print()


def main():
  matrix = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
  ]

  print_matrix_integer(matrix)
  print("--")
  print_matrix_integer()


if __name__ == "__main__":
  main()
