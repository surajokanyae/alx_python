def safe_print_division(a, b): 
    try:
     division = a / b
except ZeroDivisionError:
finally:
print("inside result: ", division)
print("{} / {} = {}" .format(a, b, division))
else:
  return division