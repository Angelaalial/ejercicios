#piedra, papel o tijera
j1=(input("Jugador 1:"))
j2=(input("Jugador 2:"))

if j1=="piedra" and j2=="tijera":
    print("Ganador:Jugador 1")  

if j1=="papel" and j2=="piedra":
    print("Ganador:Jugador 1")  

if j1=="tijera" and j2=="papel":
    print("Ganador:Jugador 1")  

if j1=="papel" and j2=="tijera":
    print("Ganador:Jugador 2")

if j1=="piedra" and j2=="papel":
    print("Ganador:Jugador 2")    

if j1=="papel" and j2=="tijera":
    print("Ganador:Jugador 2")

if j1=="papel" and j2=="papel":
    print("Empate")

if j1=="tijera" and j2=="tijera":
    print("Empate")

if j1=="piedra" and j2=="piedra":
    print("Empate")
