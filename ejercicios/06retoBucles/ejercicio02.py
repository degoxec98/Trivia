numero = int(input("Ingrese un número entero positivo: "))
while numero < 0:
  print("Ingresa un número positivo!")
  numero = int(input("Ingrese un número entero positivo: "))

for i in range(1, numero, 2):
  print(i)