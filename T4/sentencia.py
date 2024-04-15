while True:
    nomJuzgado = str(input())
    D = int(input())
    
    if D > 10:
        print(nomJuzgado, "es culpable")
        break
    else:
        print(nomJuzgado, "es inocente")