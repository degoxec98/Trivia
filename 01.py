Nombre = ''
Turn = ''
SBruto = 0
SNeto = 0
TpH = 37
HoraTrabajo = 0
#TpH se define como la Tarifa por hora de trabajo en tanto SBruto y SNeto definen el salario bruto y neto del trabajador respectivamente

Nombre = str(input("Buenos dias Puede darme su nomre por favor:"))
Turn = int(input("Buenos dias tenga usted por favor ingrese el numero que coindica con su turno \n1. Morning \n2. Afternoon \n3. Nigth\n"))
HoraTrabajo = int(input("Hola por favor necesito saber sus horas de trabajo mensual: \n"))

if Turn == 1:
    TpH = TpH
    SBruto = (TpH*HoraTrabajo)
    SNeto = SBruto
    print ("señor ",Nombre,"su salario es: ",SNeto,"soles")
elif Turn == 2:
    TpH = (TpH+1.20)
    SBruto = (TpH*HoraTrabajo)
    SNeto = SBruto
    print ("señor ",Nombre,"su salario es: ",SNeto,"soles")
elif Turn == 3:
    TpH = (TpH+1.50)
    SBruto = (TpH*HoraTrabajo)
    #here la Funcion (if, elif, else) hacen return automatico
    if SBruto >=2000 and SBruto <= 5000:
        SNeto =(SBruto*85/100)
    elif SBruto >=5000 and SBruto <= 15000:
        SNeto =(SBruto*83/100)
    else :
        SNeto = SBruto
    print ("señor",Nombre,"su salario es:",SNeto,"soles")
else :
    print ("\nError no se ha selecionado un turno de trabajo correcto")