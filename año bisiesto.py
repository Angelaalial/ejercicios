bisiesto = int(input("ingrese un año:"))

if (bisiesto % 4==0)and(bisiesto%100!=0) or (bisiesto % 400==0):
    print("el año:",bisiesto,"es un año bisiesto")

else:
    print("No es bisieto")