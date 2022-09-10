
def logo(nombreTrivia): 
  print("_____________________________________________________");
  print("_____________________________________________________\n");
  print("************** ",nombreTrivia," **************");
  print("_____________________________________________________");
  print("_____________________________________________________");


def menu():
  print("\n");
  print("********* MENU DE OPCIONES *********\n");
  print("a. Trivia 01");
  print("b. Trivia 02");
  print("c. Trivia 03");
  print("d. Trivia 04");
  print("e. Trivia RANDOM");
  option = input("Escoga una opción: ");
  return option;

def pregunta(number, question):
  print(number, question[0]);
  print("a)", question[1]);
  print("b)", question[2]);
  print("c)", question[3]);
  print("d)", question[4]);

def trivia1():
  name = "Trivia de Programación";
  question01 = ["¿Que es Python?", "Un Juego", "Un Programa", "Un lenguaje de Programación", "Una Aplicación"];
  question02 = []
  pregunta("01)", question01);
  

def iniciarApp():
  logo("BIENVENIDO A LA TRIVIA");
  op = menu();
  print("Escogiste la opción:", op);
  trivia1();

iniciarApp();