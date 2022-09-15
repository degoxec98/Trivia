num01 = int(input("Ingrese un número: "))
num02 = int(input("Ingrese otro número: "))
operador = input("Ingrese la operación: ")

while operador not in ("+","-","*","/"):
  print("Resultado: Operador inválido")
  print("Por favor ingrese +, -, *, /.")
  operador = input("Ingrese nuevamente la operación: ")
  if operador == '+':
    print(num01 + num02)
  elif operador == '-':
    print(num01 - num02)
  elif operador == '*':
    print(num01 * num02)
  elif operador == '/':
    print(num01 / num02)