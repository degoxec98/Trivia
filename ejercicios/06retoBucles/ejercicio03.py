numero = int(input("Ingresa un número: "))
factorial = 1
for i in range(numero-1, 0, -1):
  numero = numero * i
print(numero)