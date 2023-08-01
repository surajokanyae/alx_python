def best_score(a_dictionary):
  """Returns a key with the biggest integer value.

  Args:
    a_dictionary: The dictionary to search.

  Returns:
    A key with the biggest integer value.
    If no score found, return None
  """

  best_score = None
  best_key = None
  for key, value in a_dictionary.items():
    if best_score is None or value > best_score:
      best_score = value
      best_key = key
  return best_key


if __name__ == "__main__":
  a_dictionary = {"John": 10, "Jane": 8, "Bill": 12}
  best_key = best_score(a_dictionary)
  print(best_key)
