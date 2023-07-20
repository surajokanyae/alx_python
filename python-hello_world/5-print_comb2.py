def comb2():
  """Prints all two-digit combinations separated by commas."""
  for i in range(10):
    for j in range(10):
      print(str(i) + "," + str(j), end="")

if __name__ == "__main__":
    comb2()
