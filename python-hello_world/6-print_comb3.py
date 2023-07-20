def print_comb3():
  """Prints all possible different combinations of two digits."""
  for i in range(10):
    for j in range(i + 1, 10):
      if i != j:
        print("{0:02d}, ".format(i * 10 + j), end="")

  print()

if __name__ == "__main__":
  print_comb3()
