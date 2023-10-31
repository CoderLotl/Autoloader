from autoloader import autoloader

autoloader(['Person'], globals())

a = Person(['John', 30])

print(a.name)