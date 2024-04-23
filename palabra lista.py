
p=[]
palabra=input("Escriba una palabra o frase:")
a=0
e=0
i=0
o=0
u=0

for v in palabra:
    p.append(v)

print(p)

if "a" in p:
    print("La letra a se repite ",p.count("a"))
          
if "e" in p:
    print("La letra e se repite ",p.count("e"))
if "i" in p:
    print("La letra i se repite ",p.count("i"))
if "o" in p:
    print("La letra o se repite ",p.count("o"))
   
if "u" in p:
    print("La letra u se repite ",p.count("u"))
   