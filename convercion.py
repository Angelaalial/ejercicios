def pulgadas(lon1):
    resultado_f= lon1 / 12
    print("pulgadas a pies: ",round(resultado_f,2)) 
    resultado_y= lon1 / 36
    print("pulgadas a yardas: ",round(resultado_y,2))
    resultado_c= lon1 * 2.54
    print("pulgadas a centimetros: ",round(resultado_c,2))
    resultado_m= lon1 /39.37
    print("pulgadas a metros: ",round(resultado_m,2))

def pies(lon1):
    resultado_p= lon1 * 12
    print("pies a pulgadas: ",round(resultado_p,2)) 
    resultado_y= lon1 / 3
    print("pies a yardas: ",round(resultado_y,2)) 
    resultado_c= lon1 * 30.48
    print("pies a centimetros: ",round(resultado_c,2)) 
    resultado_m= lon1 / 3.281
    print("pies a metros: ",round(resultado_m,2)) 

def yardas(lon1):
    resultado_f= lon1 /30.48
    print("yardas a pies: ",round(resultado_f,2)) 
    resultado_p= lon1 * 36
    print("yardas a pulgadas: ",round(resultado_p,2)) 
    resultado_c= lon1 * 91.44
    print("yardas a centimetros: ",round(resultado_c,2)) 
    resultado_m= lon1 / 1.094
    print("yardas a metros: ",round(resultado_m,2)) 
   
def centimetros (lon1):
    resultado_f= lon1 * 3
    print("centimetros a pies: ",round(resultado_f,2)) 
    resultado_p= lon1 /2.54
    print("centimetros a pulgadas: ",round(resultado_p,2)) 
    resultado_y= lon1 / 91.44
    print("centimetros a yardas: ",round(resultado_y,2)) 
    resultado_m= lon1 / 100
    print("centimetros a metros: ",round(resultado_m,2)) 

def metros (lon1):
    resultado_f= lon1 * 3.281
    print("metros a pies: ",round(resultado_f,2)) 
    resultado_p= lon1 *39.37
    print("metros a pulgadas: ",round(resultado_p,2)) 
    resultado_y= lon1 * 1.094
    print("metros a yardas: ",round(resultado_y,2)) 
    resultado_c= lon1 * 100
    print("metros a centimetros : ",round(resultado_c,2)) 

n=int(input("Ingrese un numero:"))
me=(input("ingrese la medida:"))

if me == "p":
    pulgadas(n)

if me == "f":
    pies(n) 

if me == "y":
    yardas(n)

if me == "c":
    centimetros(n)

if me == "m":
    metros(n) 
    