import imp

def import_variable(variable_name):
    """Imports the variable from the file variable_load_2.py and prints its value."""
    module_name = "variable_load_2"
    module = imp.load_source(module_name, "variable_load_2.py")
    variable = getattr(module, variable_name)
    print(variable)
