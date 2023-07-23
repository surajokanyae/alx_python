def print_numbers(start, end):
  for i in range(start, end + 1):
    if i < 10:
      formatted_number = f"0{i:02}"
    else:
      formatted_number = f"{i:02}"
    print(formatted_number, end=", ")
  print()

print_numbers(0, 100)

