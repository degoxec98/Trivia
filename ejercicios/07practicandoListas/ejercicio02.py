vocales = ["a","e","i","o","u"]
palabra = input("Ingresa una palabra: ")

while palabra[0] in vocales:
  print("La palabra empieza con una vocal!")
  palabra = input("Ingresa una palabra: ")

print("La palabra empieza con una consonante!")