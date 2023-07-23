def print_hexa(number):
  """
  Prints the given number in decimal and in hexadecimal.

  Args:
    number: The number to print.
  """
for number in range(0, 99):
  print("{0:d} = 0x{1:x}".format(number, number))


  