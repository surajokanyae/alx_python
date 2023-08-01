def update_dictionary(a_dictionary, key, value):
  """Replaces or adds key/value in a dictionary.

  Args:
    a_dictionary: The dictionary to update.
    key: The key to update.
    value: The new value.

  Returns:
    The updated dictionary.
  """

  if key in a_dictionary:
    a_dictionary[key] = value
  else:
    a_dictionary[key] = value
  return a_dictionary


if __name__ == "__main__":
  a_dictionary = {"key1": 1, "key2": 2}
  update_dictionary(a_dictionary, "key1", 3)
  update_dictionary(a_dictionary, "key3", 4)
  print(a_dictionary)
