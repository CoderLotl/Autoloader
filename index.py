from autoloader import autoloader

autoloader(['Person', 'Animal'], globals()) # la clase Person es cargada dinámicamente

a = Person(['John', 30]) # la clase Person es instanciada. No se requirió escribir el import.
b = Animal(['Dog', 'GUAU GUAU!!'])

print(a.name)
b.emit_sound()