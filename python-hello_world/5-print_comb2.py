def saparate_numbers():
  """Prints numbers from 0 to 99."""
  for i in range(100):
    # Format the number as a two-digit string.
    number = "{:02d}".format(i)
    # Print the number, followed by a comma and a space.
    print(number, end=", ")
  # Print a newline at the end of the output.
  print()


if __name__ == "__main__":
  saparate_numbers()

