# let define a fuction hexa
def hexa():
  """Prints the numbers from 0 to 98 in hexadecimal format."""
  for i in range(99):
    print(i, "=", hex(i))

if __name__ == "__main__":
  hexa()
