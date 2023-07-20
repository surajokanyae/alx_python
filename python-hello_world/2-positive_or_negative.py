import random

def positive_or_negative(number):
  number = random.randint(-100, 100)
  if number > 0:
    print(f"{number} is positive")
  elif number == 0:
    print(f"{number} is zero")
  else:
    print(f"{number} is negative")

if __name__ == "__main__":
  positive_or_negative(-4)
  positive_or_negative(0)
  positive_or_negative(-3)
  positive_or_negative(-10)
  positive_or_negative(10)
  positive_or_negative(-5)
  positive_or_negative(6)
  positive_or_negative(7)
  positive_or_negative(5)
