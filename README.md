# README
---
**Autor:** *CoderLotl - 30/10/2023*

## Intro

Sencilla función que tiene por finalidad la importación automática de clases en una sola línea, evitando múltiples líneas y pathing a través de diversas carpetas.
Esta función tiene 2 requerimientos:
1. Que cada archivo tenga 1 clase, y solo 1 clase.
2. Que tanto el nombre del archivo como de la clase sean exactamente el mismo.

Como comentario extra, el **autoloader** funciona mejor si es utilizado junto a un archivo de config en donde se seteen los paths con las rutas a las carpetas en donde se buscarán las clases.

## 1- Código
    def autoloader(args: list, global_vars):        
        for arg in args:
            try:
                module = importlib.import_module(arg)            
                global_vars[arg] = getattr(module, arg)
            except ImportError as e:
                print(f"Failed to import {arg}: {e}")

El código es autoexplicativo:

Recibe un array de str con los nombres de los archivos/clases a cargar, y la variable *globals()* del script en donde se ejecutará la función **autoloader**.
La función hará la búsqueda de las clases y las importará, añadiéndolas a la variable *globals()* para que posteriormente puedan utilizarse dichas clases de una manera más cómoda.

Esta idea fue concebida para emular un poco la utilidad del autoloader de PHP.

## 2- Estructura del repositorio

    [ROOT]
    ├── autoloader.py
    ├── index.py
    └── Person.py