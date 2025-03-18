# README
---
**Autor:** *CoderLotl - 30/10/2023*

## Intro

Sencilla función que tiene por finalidad la importación automática de clases en una sola línea, evitando múltiples líneas y pathing a través de diversas carpetas o fuentes de recursos.
Esta función tiene 2 requerimientos:
1. Que cada archivo tenga 1 clase, y solo 1 clase.
2. Que tanto el nombre del archivo como de la clase sean exactamente el mismo.


## 1- Código
    import importlib
    import sys
    import os
    from typing import List

    def autoloader(args: List[str], global_vars: dict, base_dir: str = '.'):

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

El código es autoexplicativo:

Recibe un array de str con los nombres de los archivos/clases a cargar, y la variable *globals()* del script en donde se ejecutará la función **autoloader**.
La función hará la búsqueda de las clases y las importará, añadiéndolas a la variable *globals()* para que posteriormente puedan utilizarse dichas clases de una manera más cómoda.

Esta idea fue concebida para emular un poco la utilidad del autoloader de PHP.

## 2- Estructura del repositorio

    [ROOT]
    ├── classes
    |       └── Animal.py
    ├── autoloader.py
    ├── index.py
    └── Person.py

## 3- Ejemplo de uso

    from autoloader import autoloader

    autoloader(['Person', 'Animal'], globals()) # la clase Person es cargada dinámicamente

    a = Person(['John', 30]) # la clase Person es instanciada. No se requirió escribir el import.
    b = Animal(['Dog', 'GUAU GUAU!!'])

    print(a.name)
    b.emit_sound()

- - - 

** 18/03/2025 **

UPDATE: se actualizó el autoloader para que busque dentro de las carpetas del directorio dado o las carpetas a partir del directorio raíz.