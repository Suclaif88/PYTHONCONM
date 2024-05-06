caninos = []

def contarCaninos(caninos):
    contador = 0
    for i in caninos:
        if i["edad"] >= 6:
            contador += 1
    return contador