U1 = str(input()).lower()
U2 = str(input()).lower()

if U1 == U2:
    print("Empate")
else:
 if U1 == "piedra":
  if U2 == "tijeras":
   print("El ganador es el usuario1")
  else:
   print("El ganador es el usuario2")
 elif U1 == "papel":
  if U2 == "piedra":
   print("El ganador es el usuario1")
  else:
   print("El ganador es el usuario2")
 elif U1 == "tijeras":
  if U2 == "papel":
   print("El ganador es el usuario1")
  else:
   print("El ganador es el usuario2")