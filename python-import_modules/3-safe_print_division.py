def safe_print_division(a, b):
    """Divides 2 integers and prints the result.

    Args:
        a (int): The first number to divide.
        b (int): The second number to divide.

    Returns:
        The value of the division, otherwise: None.
    """

    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result

if __name__ == "__main__":
    a = 12
    b = 2
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))

    a = 12
    b = 0
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))
