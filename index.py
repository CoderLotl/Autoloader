from autoloader import autoloader

autoloader(['Person'], globals()) # la clase Person es cargada dinámicamente

a = Person(['John', 30]) # la clase Person es instanciada. No se requirió escribir el import.

print(a.name)