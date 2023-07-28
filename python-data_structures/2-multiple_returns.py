def multiple_returns(sentence):
  """Returns a tuple with the length of a string and its first character.

  Args:
    sentence: The string to be processed.

  Returns:
    A tuple with the length of the string and its first character.
  """

  if not sentence:
    return (0, None)
  else:
    return (len(sentence), sentence[0])


def main():
  sentence = "At Holberton school, I learnt C!"
  length, first = multiple_returns(sentence)
  print("Length: {:d} - First character: {}".format(length, first))


if __name__ == "__main__":
  main()
