import importlib

def import_variable(variable_name):
    """Imports the variable from the file variable_load_2.py and prints its value."""
    module = importlib.import_module("variable_load_2")
    variable = getattr(module, variable_name)
    print(variable)

if __name__ == "__main__":
    import_variable("a")
