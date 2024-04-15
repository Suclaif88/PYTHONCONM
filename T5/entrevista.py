R1 = str(input())
R2 = str(input())

if len(R1) > len(R2):
    print("La respuesta de la primera presidenta es más larga")
elif len(R1) < len(R2):
    print("La respuesta de la segunda presidenta es más larga")
else:
    print("Las respuestas de ambas presidentas son igual de largas")