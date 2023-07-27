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


def fake_add(a, b):
    """My fake addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return (a - b)


if __name__ == "__main__":
    a = 1
    b = 2
    print(f"1 + 2 = {add(a, b)}, FAKE add() => {fake_add(a, b)}.format(1, 2)")

