dia = int (input("Ingrese un día:"))

if dia<1 or dia>31:
    print("Día invalido")
else:
    print("Día valido")
mes = int (input("Ingrese un mes:"))

if mes<1 or mes>12:
    print("Mes invalido")
else:
    print("Mes valido")

año = int (input("Ingrese un año:"))
if (año % 4==0)and(año%100!=0) or (año %100==0)and(año % 400==0):
    print("El año",año,"es un año bisiesto")
else:
    print("No es un año bisiesto")