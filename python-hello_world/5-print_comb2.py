def print_numbers(start, end):
  """Prints numbers from start to end, separated by ,, followed by a space."""
  for i in range(start, end + 1):
    print(f"{i:02d}, ", end="")

  print()


if __name__ == "__main__":
  print_numbers(0, 100)
