filas = int(input("Filas: "))
for i in range(0, filas):
  #print("+"*i) #OTRA MANERA DE HACERLO 
  for j in range(-1, i):
    print("+", end = " ")
  print(" ")