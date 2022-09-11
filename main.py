nombre = ""


def logo(nombreTrivia): 
  print("______________________________________________________")
  print("______________________________________________________\n")
  print("***************",nombreTrivia,"***************")
  print("______________________________________________________")
  print("______________________________________________________")

def validarInput():
  opcion = input("Elige una respuesta: ").lower()
  while opcion not in ("a", "b", "c", "d","x"):
    opcion = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ").lower()
  opcion = opcion+"."
  if opcion == "x.":
    print("Vamos",nombre, "tú puedes!")
    return validarInput()
  return opcion


def validarEleccion(opcion, respuesta):
  correcto = False
  print(opcion)
  
  if len(respuesta)>1:
    for res in respuesta:
      if opcion in res:
        print("Incorrecto!(2)", res)
  else:
    for res in respuesta:
      if opcion == res:
        print("Correcto!!!!")
        correcto = True
      else:
        print("Incorrecto!(1)")  
    

def validarRespuesta(preguntaConIndice, respuesta):
  opcion = validarInput()
  for alternativa in preguntaConIndice:
    if opcion in alternativa:
      opcion = alternativa[2:]
  validarEleccion(opcion, respuesta)
  
  return opcion

def menuTrivia():
  nombre = input("\n¡Hola! Por favor ingresa tu nombre: ")
  print("\nBienvenido "+nombre+", por favor elige una de las siguientes trivias escribiendo la letra de la trivia y presionando 'Enter' para enviar tu opción:\n")
  print("a. Trivia Seleccion Peruana")
  print("b. Trivia 02")
  print("c. Trivia 03")
  print("d. Trivia RANDOM")
  respuesta = validarInput()
  return respuesta

def preguntaPrint(number, pregunta, respuesta):
  indice = [str(number)+".", "a.","b.","c.","d."]
  preguntaConIndice = []
  i = 0
  while i < len(indice):
    print(indice[i], pregunta[i])
    preguntaConIndice.append((indice[i]+pregunta[i]))
    i+=1
  respuesta = validarRespuesta(preguntaConIndice, respuesta)
  print("\n")

def triviaSeleccionPeru():
  name = "Trivia de la Selección Peruana"
  preguntas = []
  respuestas = []
  preguntas.append((["¿Cuántas veces La Blanquirroja ganó la Copa América?", "1", "3", "0", "2"],["2"]))
  preguntas.append((["¿En qué torneo se estrenó la clásica camiseta blanca con franja roja?", "Copa América 1929", "Mundial 1930", "Juegos Olímpicos 1936", "Bolivarianos 1938"],["Juegos Olímpicos 1936"]))
  preguntas.append((["¿Qué número de camiseta pidió Perú a la FIFA no usar en el Mundial de 1978?", "7", "13", "22", "23"],["13"]))
  preguntas.append((["¿Qué número de camiseta ha vestido Paolo Guerrero en sus partidos por la bicolor?", "9 y 18", "Solo la 9", "9, 18 y 22", "8, 9 y 18"],["Solo la 9"]))
  preguntas.append((["¿Cuántos mundiales jugó Perú?", "5", "6", "4", "3"],["5"]))
  preguntas.append((["¿Quién es el máximo goleador de la selección Peruana?", "Raúl Ruidíaz", "Jefferson Farfán", "Paolo Guerrero", "Teófilo Cubillas"],["Paolo Guerrero"]))
  preguntas.append((["¿Ante qué rival Perú usó los colores del escudo invertidos en la Eliminatoria a México 1986?", "Chile", "Argentina", "Colombia", "Venezuela"],["Chile"]))
  preguntas.append((["Antes de Ricardo Gareca, ¿Cuántos entrenadores argentinos dirigieron a Perú?", "0", "1", "2", "Más de 3"],["1"]))
  preguntas.append((["¿Cuántos partidos ha dirigido Ricardo Gareca con Perú?", "100", "90", "95", "98"],["95"]))
  preguntas.append((["¿Quién es el arquero australiano que atajó en los penales del repechaje al mundial Catar 2022?", "Yussuf Poulsen", "Mathew Ryan", "Mitchell Duke", "Andrew Redmayne"],["Andrew Redmayne", "Yussuf Poulsen juega en la selección de Dinamarca", "Mathew Ryan fue el arquero titular del partido pero fue sustituido para los penales", "Mitchell Duke juega en la posición de delantero"]))
  i = 1
  for pregunta in preguntas:
    preguntaPrint(i, pregunta[0], pregunta[1])
    i+=1
  

def iniciarApp():
  logo("BIENVENIDO A LA TRIVIA")
  op = menuTrivia()
  triviaSeleccionPeru()

iniciarApp();