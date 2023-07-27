def raise_exception_msg(message=""):
    """Raises a name exception with a message.

    Args:
        message (str): The message to include in the exception.

    Raises:
        NameError: Always raises a name exception.
    """

    raise NameError(message)

if __name__ == "__main__":
    try:
        raise_exception_msg("C is fun")
    except NameError as ne:
        print(ne)
