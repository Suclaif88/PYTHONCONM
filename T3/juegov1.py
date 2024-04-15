U1 = str(input()).lower()
U2 = str(input()).lower()

if U1 == U2:
    print("Empate")
elif (U1 == "piedra" and U2 == "tijeras") or (U1 == "papel" and U2 == "piedra") or (U1 == "tijeras" and U2 == "papel"):
    print("El ganador es el usuario1")
else:
    print("El ganador es el usuario2")