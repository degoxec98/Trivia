numero = int(input("Ingresa un número del 1 al 12: "))

while numero<1 or numero>12:
  print("Número no válido, vuelve a ingresar!")
  numero = int(input("Ingresa un número del 1 al 12: "))

for i in range (1, 13):
  print(i*numero)

