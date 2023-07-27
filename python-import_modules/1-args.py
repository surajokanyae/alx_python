import sys

def print_arguments():
    """Prints the number of and the list of its arguments."""
      number = len(sys.argv)
    print(f"{number} arguments:")
    if number == 0:
        print(".")
    else:
        for i in range(1, number + 1):
            print(f"{i}: {sys.argv[i - 1]}")

if __name__ == "__main__":
    print_arguments()
