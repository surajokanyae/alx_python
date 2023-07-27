import sys

def import_variable(variable_name):
    """Imports the variable from the file variable_load_2.py and prints its value."""
    module_name = "variable_load_2"
    module = __import__(module_name)
    variable = getattr(module, variable_name)
    print(variable)

if __name__ == "__main__":
    import_variable("a")
