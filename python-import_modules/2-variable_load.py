def print_a():
    with open("variable_load_2.py", "r") as f:
        source = f.read()
    variable = a
    # Extract the variable a from the source code
    exec(source)
    print(a)

if __name__ == "__main__":
    print_a()
