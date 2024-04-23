#edads
es1=int(input("Ingrese edad 1:"))
es2=int(input("Ingrese edad 2:"))
es3=int(input("Ingrese edad 3:"))
es4=int(input("Ingrese edad 4:"))
es5=int(input("Ingrese edad 5:"))
es6=int(input("Ingrese edad 6:"))
es7=int(input("Ingrese edad 7:"))
es8=int(input("Ingrese edad 8:"))

pre=0 #contador de edades de 5 años
kin=0 #contador de edades de 4 años
pri=0 #contador de edades de 6 años

if(3<es1<=6) and (3<es2<=6) and (3<es3<=6) and (3<es4<=6) and (3<es5<=6) and (3<es6<=6) and (3<es7<=6) and (3<es8<=6):
    if es1==4:
       pre=pre+1
    if es2==4:
       pre=pre+1
    if es3==4:
       pre=pre+1
    if es4==4:
       pre=pre+1
    if es6==4:
       pre=pre+1
    if es7==4:
       pre=pre+1
    if es8==4:
       pre=pre+1
    print(pre,"Niño de prekinder")
    if es1==5:
       kin=kin+1
    if es2==5:
       kin=kin+1
    if es3==5:
       kin=kin+1
    if es4==5:
       kin=kin+1
    if es5==5:
       kin=kin+1
    if es6==5:
       kin=kin+1
    if es7==5:
       kin=kin+1
    if es8==5:
       kin=kin+1
    print(kin,"Niño de kinder")
    if es1==6:
       pri=pri+1
    if es2==6:
       pri=pri+1
    if es3==6:
       pri=pri+1
    if es4==6:
       pri=pri+1
    if es5==6:
       pri=pri+1
    if es6==6:
       pri=pri+1
    if es7==6:
       pri=pri+1
    if es8==6:
       pri=pri+1
    print(pri,"Niño de primaria")
    
else:
   print("numero invalido")



