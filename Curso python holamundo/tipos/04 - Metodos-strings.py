# nombrando una variable
animal = "  ChanCHito Feliz  "

# los metodos se pueden encadenar
print(animal.upper())  # Todo mayusculas
print(animal.lower())  # Todo minusculas
# .captalize() = la primera palabra en mayusculas
print(animal.strip().capitalize())
print(animal.title())  # Todas las primeras letras de las palabras en mayusculas
print(animal.strip())  # Sin espacios iniciales o finales
print(animal.rstrip())  # Sin espacios finales
print(animal.lstrip())  # Sin espacios iniciales
# .find(argumento) = buscarlo -> Si no lo encuentra devuelve -1
print(animal.find("cH"))
# .find(argumento) = buscarlo -> Si lo encuentra devuelve el _indice_
print(animal.find("CH"))
print(animal.replace("nCH", "k"))  # se enecesitan si o si los dos argumentos
print("nCH" in animal)  # boolean True
print("nCH" not in animal)  # boolean
