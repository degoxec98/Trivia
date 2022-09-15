import random #IMPORTA LA LIBRERIA RANDOM
import time #IMPORTA LA LIBRERIA TIME

# DEFINE LOS COLORES
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
# DEFINE DONDE FINALIZA CADA COLOR
RESET = '\033[39m'

# INICIALIZACIÓN DE VARIALBES GLOBALES
iniciarTrivia = True
intentos = 0
nombre = ""
respuestaSecreta = True
aleatorioActual = 0

def logo(): # FUNCION PARA IMPRIMIR EL LOGO
  # PINTA EL LOGO DE ROJO Y BLANCO COMO LA BANDERA PERUANA
  print(RED+"______________________"+RESET+WHITE+"________________________________"+RESET+RED+"______________________"+RESET)
  print(RED+"______________________"+RESET+WHITE+"________________________________"+RESET+RED+"______________________\n"+RESET)
  print(RED+"**********************"+RESET+WHITE+" TRIVIA DE LA SELECCIÓN PERUANA "+RESET+RED+"**********************"+RESET)
  print(RED+"______________________"+RESET+WHITE+"________________________________"+RESET+RED+"______________________"+RESET)
  print(RED+"______________________"+RESET+WHITE+"________________________________"+RESET+RED+"______________________\n"+RESET)
  time.sleep(1) # ESPERA 1 SEGUNDO
  # MENSAJE DE BIENVENIDA A LA TRIVIA
  print(MAGENTA+"Bienvenido a mi trivia sobre la selección peruana!")
  print("Pondremos a prueba que tan hincha eres la selección peruana!"+RESET)
  print(YELLOW+"Por favor sigue las indicaciones!"+RESET)
  # SE DEFINE GLOBAL PARA PODER MODIFICAR LA VARIALBE GLOBAL "nombre"
  global nombre
  time.sleep(1) #ESPERA 1 SEGUNDO
  # INGRESA EL NOMBRE DEL USUARIO
  nombre = input("\n¡Hola! Por favor ingresa tu nombre y presiona 'Enter' al finalizar: ")
  time.sleep(2) #ESPERA 2 SEGUNDOS
  # BIENVENIDA PERSONALIZADA E INSTRUCCIONES A SEGUIR
  print("\nBienvenido "+nombre+", por favor responde a las siguientes preguntas, escribiendo la letra de la alternativa elegida y presionando 'Enter' para enviar tu respuesta:\n")

# FUNCION PARA MOSTRAR EL PUNTAJE ACTUAL
def mostrarPuntaje():
  print(YELLOW+nombre, "tu puntaje actual es: ", puntaje,RESET)

# FUNCION PARA ASIGNAR PUNTAJE ALEATORIO CON LOS PARAMETROS DE CORRECTO
def puntajeRandom(correcto):
  # SE INDICA QUE LAS VARIABLES SON GLOBALES
  global puntaje
  global aleatorioActual
  # SI LA RESPUESTA ES CORRECTA INGRESA
  if correcto:
    aleatorioActual = random.randint(5, 10) # ASIGNA PUNTAJE ALEATORIO ENTRE 5 Y 10
    puntaje += aleatorioActual #SUMA EL PUNTAJE ACTUAL CON EL ALEATORIO OBTENIDO
  else: # SI LA RESPUESTA ES INCORRECTA INGRESA
    aleatorioActual = random.randint(2, 5) # ASIGNA PUNTAJE ALEATORIO ENTRE 2 Y 5
    puntaje -= aleatorioActual #RESTA EL PUNTAJE ACTUAL CON EL ALEATORIO OBTENIDO
  
# FUNCION PARA IMPRIMIR SI LA RESPUESTA ES CORRECTA O INCORRECTA
def verificarRespuesta(correcto, tip=""): # SE OBTIENE LOS PARAMETROS CORRECTO Y TIP = "" PORQUE SE INICIALIZA EN CASO NO SE ENVIE DICHO PARAMETRO
  if correcto: #VERIFICA SI ES CORRECTO 
    puntajeRandom(correcto) #SE SUMA UN PUNTAJE ALEATORIO
    print("Es correcto!",nombre,GREEN+"sumaste",aleatorioActual,"puntos"+RESET) # IMPRIME QUE ES CORRECTO Y EL PUNTAJE ALEATORIO SUMADO
  else: #EN CASO SEA INCORRECTO
    puntajeRandom(correcto) #SE RESTA UN PUNTAJE ALEATORIO
    if tip != "": #SI ES INCORRECTO PERO TIENE TIP INGRESA 
      print(nombre,"la respuesta es incorrecta."+RED+" Perdiste",aleatorioActual,"puntos!"+RESET+" Te dejo un pequeño tip para que lo tomes en cuenta\n"+CYAN+tip+RESET) #IMPRIME EL TIP 
    else: #EN CASO NO TENGA TIP
      print("La respuesta es incorrecta!",nombre,RED+"perdiste",aleatorioActual,"puntos!"+RESET)
  mostrarPuntaje() # LLAMA A LA FUNCION PARA MOSTRAR EL PUNTAJE ACTUAL

#FUNCION PARA VALIDAR LA ALTERNATIVA ELEGIDA
def validarInput():
  opcion = input("Elige una respuesta: ").lower() # TRANSFORMA EL INPUTA EN MINÚSCULAS
  while opcion not in ("a", "b", "c", "d","x"): # SE EJECUTA MIENTRAS NO SEA UNA DE LAS LETRAS ESTABLECIDAS
    opcion = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ").lower() #VUELVE A PEDIR QUE INGRESE UNA ALTERNATIVA VÁLIDA
  opcion = opcion+"." # CONCATENA UN PUNTO DESPUES DE LA ALTERNATIVA
  if opcion == "x.": # SI LA ALTERNATIVA ES UNA RESPUESTA SECRETA
    global respuestaSecreta
    global puntaje
    if respuestaSecreta: # VERIFICA SI YA SE UTILIZO LA RESPUESTA SECRETA
      print(GREEN+nombre, "acabas de ganar 33 puntos por descubrir la respuesta secreta!!!"+RESET) 
      respuestaSecreta = False # INDICA QUE LA RESPUESTA SECRETA YA SE HA UTILIZADO
      puntaje += 33 # SUMA SOLO UNA VEZ 33 PUNTOS AL PUNTAJE ACTUAL
    else: # EN CASO LA RESPUESTA SECRETA YA SE HAYA UTILIZADO
      print(BLUE+nombre,"Ya usaste la respuesta secreta una vez, ya no puedes volver a ganar puntos por eso, continua con la trivia!"+RESET)
    return validarInput() # VUELVE A LLAMAR LA FUNCION HASTA QUE ELIJA OTRA ALTERNATIVA DISTINA A LA RESPUESTA SECRETA
  return opcion #RETORNA LA OPCION ELEGIDA

# FUNCION PARA VALIDAR LA ALTERNATIVA ELEGIDA
def validarEleccion(opcion, respuesta): # TIENE COMO PARAMETROS LA OPCION ELEGIDA Y LA RESPUESTA A LA PREGUNTA
  correcto = False # SE INICIA LA VARIALBE CORRECTO CON FALSE
  # RECORRE EL ARRAY RESPUESTA EN CASO ESTE CONTENGA TIPS
  # EN CASO QUE SOLO OBTENGA LA RESPUESTA VA A RECORRER UNA SOLA VEZ
  # LO CUAL ES LA RESPUESTA A LA PREGUNTA
  for res in respuesta:
    if opcion == res: # SI LA OPCION ELEGIDA ES LA CORRECTA
      correcto = True # ENTONCES SE DICE QUE LA RESPUESTA ES CORRECTA
  if len(respuesta)>1 and not correcto: # SI LA RESPUESTA TIENE TIPS Y LA RESPUESTA SEA INCORRECTA
    for tip in respuesta: # RECORRE EL ARRAY DE LA RESPUESTA PARA OBTENER LOS TIPS DE LAS RESPUESTAS INCORRECTAS
      if opcion in tip: # SI ENCUENTRA LA RESPUESTA INCORRECTA EN EL TIP 
        verificarRespuesta(correcto,tip) # ENTONCES LLAMA A LA FUNCION VERIFICAR RESPUESTA CON LOS PARAMETROS CORRECTO Y EL TIP
  else: # CASO CONTRARIO
    verificarRespuesta(correcto) #LLAMA A LA FUNCION VERIFICAR RESPUESTA CON EL PARAMETRO CORRECTO 

# FUNCION PARA VALIDAR LA RESPUESTA QUE TIENE LOS PARAMETROS DE PREGUNTA CON LOS INDICES Y LA RESPUESTA
def validarRespuesta(preguntaConIndice, respuesta):
  opcion = validarInput() # LLAMA A LA FUNCION VALIDAD INPUT Y GUARDA LA OPCION ELEGIDA
  for alternativa in preguntaConIndice: # RECORRE EL ARRAY PREGUNTA CON INDICE Y OBTIENE CADA ALTERNATIVA
    if opcion in alternativa: # SI LA OPCION ESTÁ EN LA ALTERNATIVA 
      opcion = alternativa[2:] # ENTONCES OBTIENE LA OPCION QUE SE HA ELEGIDO
  validarEleccion(opcion, respuesta) # LLAMA LA FUNCION VALIDAD ELECCION CON LOS PARAMETROS OPCION Y RESPUESTA
  return opcion #RETORNA LA OPCION ELEGIDA

# FUNCION PARA IMPRIMIR CADA PREGUNTA
def preguntaPrint(number, pregunta, respuesta): # RECIBE EL NÚMERO DE PREGUNTA (CON IDEA DE ALEATORIEDAD), LA PREGUNTA(y alternativas) Y LA RESPUESTA
  time.sleep(1)
  # SE CREA UN ARRAY CON LOS INDICES DE NUMERO (número de pregunta) concatenado con el "."
  # Y LAS ALTERNATIVAS (que van del a al d)
  indice = [str(number)+".", "a.","b.","c.","d."]
  preguntaConIndice = [] #SE CREA UN ARRAY AUXILIAR PARA CONCATENAR LOS INDICES DE LA LINEA ANTERIOR CON LAS PREGUNTAS(y alternativas)
  i = 0 # SE INICIALIZA i
  while i < len(indice): #MIENTRAS HAYA INDICES POR RECORRER ENTONCES:
    print(indice[i], pregunta[i]) # CONCATENA EL INDICE CON LA PREGUNTA (y alternativas)
    preguntaConIndice.append((indice[i]+pregunta[i])) # SE AGREGA LA CONCATENACION ANTERIOR AL ARRAY AUXILIAR
    i+=1
  respuesta = validarRespuesta(preguntaConIndice, respuesta) # SE LLAMA A LA FUNCION validarRespuesta
  print("\n")

# FUNCION PARA DEFINIR LA TRIVIA DE LA SELECCION PERUANA DE FÚTBOL
def triviaSeleccionPeru():
  preguntas = [] # ARRAY CON LAS PREGUNTAS, ALTERNATIVAS Y RESPUESTAS (algunas con TIP)
  # SE AGREGA UN ARRAY CON DOS ELEMENTOS: LA RESPUESTA CON LAS ALTERNATIVAS Y LA RESPUESTA
  preguntas.append((["¿Cuántas veces La Blanquirroja ganó la Copa América?", "1", "3", "0", "2"],["2"]))
  preguntas.append((["¿En qué torneo se estrenó la clásica camiseta blanca con franja roja?", "Copa América 1929", "Mundial 1930", "Juegos Olímpicos 1936", "Bolivarianos 1938"],["Juegos Olímpicos 1936"]))
  preguntas.append((["¿Qué número de camiseta pidió Perú a la FIFA no usar en el Mundial de 1978?", "7", "13", "22", "23"],["13"]))
  preguntas.append((["¿Qué número de camiseta ha vestido Paolo Guerrero en sus partidos por la bicolor?", "9 y 18", "Solo la 9", "9, 18 y 22", "8, 9 y 18"],["Solo la 9"]))
  preguntas.append((["¿Cuántos mundiales jugó Perú?", "5", "6", "4", "3"],["5"]))
  preguntas.append((["¿Quién es el máximo goleador de la selección Peruana?", "Raúl Ruidíaz", "Jefferson Farfán", "Paolo Guerrero", "Teófilo Cubillas"],["Paolo Guerrero"]))
  preguntas.append((["¿Ante qué rival Perú usó los colores del escudo invertidos en la Eliminatoria a México 1986?", "Chile", "Argentina", "Colombia", "Venezuela"],["Chile"]))
  preguntas.append((["Antes de Ricardo Gareca, ¿Cuántos entrenadores argentinos dirigieron a Perú?", "0", "1", "2", "Más de 3"],["1"]))
  preguntas.append((["¿Cuántos partidos ha dirigido Ricardo Gareca con Perú?", "100", "90", "95", "98"],["95"]))
  #
  # EN ESTE CASO SE AGREGA UN ARRAY CON DOS ELEMENTOS: LA PREGUNTA CON LAS ALTERNATIVAS Y LA RESPUESTA CON LOS TIPS
  # EN EL CASO DEL SEGUNDO ARRAY, SE TIENE QUE EL PRIMER ELEMENTO ES LA RESPUESTA
  # LOS DEMÁS ELEMENTOS SON LOS TIPS A LAS ALTERNATIVAS
  # POR EJEMPLO SI EN ESTA PREGUNTA SE ELIGE LA ALTERNATIVA "Yussuf Poulsen" LA CUAL ES INCORRECTA
  # SE DEBE IMPRIMIR EL TIP ACORDE A LA ALTERNATIVA ELEGIDA ANTERIORMENTE LA CUAL ES:
  # "Yussuf Poulsen juega en la selección de Dinamarca"
  preguntas.append((["¿Quién es el arquero australiano que atajó en los penales del repechaje al mundial Catar 2022?", "Yussuf Poulsen", "Mathew Ryan", "Mitchell Duke", "Andrew Redmayne"],["Andrew Redmayne", "Yussuf Poulsen juega en la selección de Dinamarca", "Mathew Ryan fue el arquero titular del partido pero fue sustituido para los penales", "Mitchell Duke juega en la posición de delantero"]))
  return preguntas # RETORNA LA PREGUNTAS CON LAS ALTERNATIVAS Y LAS RESPUESTAS CON LOS TIPS EN CASO TENGAN

# FUNCION PARA CORRER LA TRIVA
def correrTrivia(preguntas): # RECIBE LAS PREGUNTAS
  i = 1
  for pregunta in preguntas: # RECORRE TODAS LAS PREGUNTAS, PREGUNTA POR PREGUNTA
    preguntaPrint(i, pregunta[0], pregunta[1]) # LLAMA A LA FUNCION PARA IMRPIMIR CADA PREGUNTA
    i+=1 # INDICE DE LA PREGUNTA (con idea de aleatoriedad)
  print ("Gracias", nombre, "por jugar mi trivia, alcanzaste", puntaje, "puntos") #IMPRIME UNA VEZ QUE HAYA RESPONDIDO TODAS LAS PREGUNTAS

# FUNCION PARA INICIAR LA APP (trivia)
def iniciarApp():
  # SE LLAMA A LAS VARIALBES GLOBALES A MODIFICAR
  global intentos
  global puntaje
  global iniciarTrivia
  
  logo() # LLAMA A LA FUNCION LOGO PARA IMPRIMIR EL LOGO
  preguntas = triviaSeleccionPeru() # SE TRAE LAS PREGUNTAS DE LA TRIVIA
  while iniciarTrivia: # MIENTRAS SE SIGA USANDO LA TRIVIA ENTONCES:
    intentos += 1 # CUENTA EL NÚMERO DE INTENTOS DEL USUARIO
    puntaje = random.randint(0, 10) # SE ASIGNA UN PUNTAJE INICIAL ALEATORIO ENTRE EL 0 Y EL 10
    print(MAGENTA+"Intento número:", intentos,RESET)
    input("Presiona Enter para continuar")
    print("\n")
    print(YELLOW+nombre+", comenzarás con:",puntaje,"puntos\n"+RESET)
    correrTrivia(preguntas) # SE LLAMA A LA FUNCION CORRERTRIVIA CON LAS PREGUNTAS 
    print(YELLOW+"\n¿Deseas intentar la trivia nuevamente?"+RESET) # PREGUNTA SI SE DESEA VOLVER A INTENTARLO
    # OBTIENE LA RESPUESTA DEL USUARIO (en caso quiera repetir la trivia o no)
    repetirTrivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()
    if repetirTrivia != "si": # SI EL USUARIO NO QUIERE VOLVER A INTENTARLO ENTONCES:
     print(MAGENTA+nombre+" espero que lo hayas pasado bien, hasta pronto!"+RESET) #MENSAJE DE DESPEDIDA
     iniciarTrivia = False # CAMBIA EL ESTADO A FALSO PARA QUE EL WHILE PUEDA FINALIZAR

iniciarApp(); # LLAMA A LA FUNCION INICIARAPP PARA CORRER LA TRIVIA