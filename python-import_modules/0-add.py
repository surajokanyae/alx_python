from add_0 import add
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)


if __name__ == "__main__":
    a = 1
    b = 2
    print(f"{a} + {-b} = {add(a, b)}".format(1, 2))
