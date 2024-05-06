import random

def generar_saludo():
    saludo = ['C', 'h', 'a', 'o']
    return saludo

def generar_despedida():
    despedida = ['t', 'a', 'l', 'l', 'e', 'r', 'e', 's']
    return despedida

def generar_institucion():
    institucion = ['E', 'A', 'F', 'I', 'T']
    institucion = [letra.upper() if random.random() > 0.5 else letra for letra in institucion]
    return institucion

def imprimir_mensaje():
    saludo = generar_saludo()
    despedida = generar_despedida()
    institucion = generar_institucion()

    mensaje = []
    for letra in saludo:
        mensaje.append(letra)
    mensaje.append(" ")
    for letra in despedida:
        mensaje.append(letra)
    mensaje.append(" ")
    for letra in institucion:
        mensaje.append(letra)

    for letra in mensaje:
        print(letra, end="")

imprimir_mensaje()
