#orden acendente y desendente 
x=int(input("Por favor escriba un numero:"))
y=int(input("Por favor escriba otro numero:"))
z=int(input("Por favor escriba un tercer número"))
if x>y and x>z and y>z:
    print("mayor",x,"medio",y,"menor",z)
if y>x and y>z and z>x:
    print("mayor",y,"medio",z,"menor",x)