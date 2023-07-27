def raise_exception():
    """Raises a type exception.

    Raises:
        TypeError: Always raises a type exception.
    """

    raise TypeError("This is a type exception")

if __name__ == "__main__":
    try:
        raise_exception()
    except TypeError as te:
        print("Exception raised")
