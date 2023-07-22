import random

def positive_or_negative():
  number = random.randint(-10, 10)
  if number > 0:
    print(f"{number} is positive")
  elif number == 0:
    print(f"{number} is zero")
  else:
    print(f"{number} is negative")

if __name__ == "__main__":
  positive_or_negative()
