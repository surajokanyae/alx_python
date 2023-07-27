def print_a(a):
    with open("variable_load_2.py", "r") as f:
        source = f.read()

    exec(source, {"a": a})
    print(a)

if __name__ == "__main__":
    print_a(89)
    print_a(-100)
