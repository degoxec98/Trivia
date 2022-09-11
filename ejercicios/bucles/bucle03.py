filas = int(input("Filas: "))
i = 1
while i <= filas:
  #print("+"*i)
  j = 0
  while j < i:
    print("+", end = "")
    j+=1
  print(" ")
  i+=1