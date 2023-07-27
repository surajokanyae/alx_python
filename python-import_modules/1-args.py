import sys

def print_arguments():
    """Prints the number of and the list of its arguments."""
    args_number = len(sys.argv)
    if args_number == 1:
        print("No arguments.")
    else:
        print(f"{args_number - 1} arguments:")
        for i in range(1, args_number):
            print(f"{i}: {sys.argv[i - 1]}")

if __name__ == "__main__":
    print_arguments()
