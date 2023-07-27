import sys

def print_arguments():
    """Prints the number of and the list of its arguments."""
    args_number = len(sys.argv[1:])
    print(f"{args_number} arguments:")
    if args_number == 0:
        print(".")
    else:
        for i in range(1, args_number + 1):
            print(f"{i}: {sys.argv[i]}")

if __name__ == "__main__":
    print_arguments()
