def convert_to_celsius(fahrenheit):
  """
  Converts a temperature in Fahrenheit to Celsius.

  Args:
    fahrenheit: The temperature in Fahrenheit.

  Returns:
    The temperature in Celsius.
  """

  if type(fahrenheit) is not int:
    raise TypeError("fahrenheit must be an integer")
  celsius = (fahrenheit - 32) * 5 / 9
  return celsius
