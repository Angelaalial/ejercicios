n1= int(input("Ingrese el numero donde desee que empiece:)"))
n2= int(input("Ingrese el numero de tablas que desea:)"))
m= int(input("Ingrese un numero :)"))


for i in range(1,m+1):
   for j in range(n1,n2+1):
      print (i*j, end="\t")
   print("")
