import importlib
import sys
import os
from typing import List

def autoloader(args: List[str], global_vars: dict, base_dir: str = '.'):
    """
    Loads all the classes to the globals() passed as param. Class name and file name must be the same.

    Args:
        args (list): an array of strings with the names of the classes/files.
        global_vars (dict): the globals() of the script where the autoloader is executed.
        base_dir (str): The directory to start the search from. Defaults to the current directory.
    """
    # Add the base directory and its subdirectories to the sys.path
    for root, dirs, files in os.walk(base_dir):
        sys.path.append(root)  # Add each directory to the search path

    for arg in args:
        try:
            # Dynamically import the module
            module = importlib.import_module(arg)
            # Dynamically fetch the class from the module
            global_vars[arg] = getattr(module, arg)
        except ImportError as e:
            print(f"Failed to import module {arg}: {e}")
        except AttributeError:
            print(f"Class {arg} not found in module {arg}.")