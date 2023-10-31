import importlib

def autoloader(args: list, global_vars):
    """
        Loads all the classes to the globals() passed as param. Class name and file name must be the same.
    Args:
        args (list): an array of string with the names of the classes/files.
        global_vars (_type_): the globals() of the script where the autoloader is executed.
    """
    for arg in args:
        try:
            module = importlib.import_module(arg)            
            global_vars[arg] = getattr(module, arg)
        except ImportError as e:
            print(f"Failed to import {arg}: {e}")