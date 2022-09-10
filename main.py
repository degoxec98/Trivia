
def logo(nombreTrivia): 
  print("_____________________________________________________")
  print("_____________________________________________________\n")
  print("************** ",nombreTrivia," **************")
  print("_____________________________________________________")
  print("_____________________________________________________")


def menuTrivia():
  print("\n")
  print("********* Elige un Trivia *********\n")
  print("a. Trivia 01")
  print("b. Trivia 02")
  print("c. Trivia 03")
  print("d. Trivia 04")
  print("e. Trivia RANDOM")
  option = input("Escoga una opción: ")
  return option

def pregunta(number, question):
  print(number, question[0])
  print("a)", question[1])
  print("b)", question[2])
  print("c)", question[3])
  print("d)", question[4])
  respuesta = input("La respuesta es: " )
  print(respuesta)

def triviaSeleccionPeru():
  name = "Trivia de la Selección Peruana"
  question01 = ["¿Cuántas veces La Blanquirroja ganó la Copa América?", "1", "3", "0", "2"]
  question02 = ["¿En qué torneo se estrenó la clásica camiseta blanca con franja roja?", "Copa América 1929", "Mundial 1930", "Juegos Olímpicos 1936", "Bolivarianos 1938"]
  question03 = ["¿Qué número de camiseta pidió Perú a la FIFA no usar en el Mundial de 1978?", "7", "13", "22", "23"]
  question04 = ["¿Qué número de camiseta ha vestido Paolo Guerrero en sus partidos por la bicolor?", "9 y 18", "Solo la 9", "9, 18 y 22", "8, 9 y 18"]
  question05 = ["¿Cuántos mundiales jugó Perú?", "5", "6", "4", "3"]
  question06 = ["¿Quién es el máximo goleador de la selección Peruana?", "Raúl Ruidíaz", "Jefferson Farfán", "Paolo Guerrero", "Teófilo Cubillas"]
  question07 = ["¿Ante qué rival Perú usó los colores del escudo invertidos en la Eliminatoria a México 1986?", "Chile", "Argentina", "Colombia", "Venezuela"]
  question08 = ["Antes de Ricardo Gareca, ¿Cuántos entrenadores argentinos dirigieron a Perú?", "0", "1", "2", "Más de 3"]
  question09 = ["¿Cuántos partidos ha dirigido Ricardo Gareca con Perú?", "100", "90", "95", "98"]
  question10 = ["¿Quién es el arquero australiano que atajó en los penales del repechaje al mundial Catar 2022?", "Yussuf Poulsen", "Matthew Ryan", "Mitchell Duke", "Andrew Redmayne"]
  pregunta("01)", question01)
  

def iniciarApp():
  logo("BIENVENIDO A LA TRIVIA")
  op = menuTrivia()
  print("Escogiste la opción:", op)
  triviaSeleccionPeru()

iniciarApp();