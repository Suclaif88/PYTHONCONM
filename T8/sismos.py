sismos= [8.0, 4.0, 6.9]
contador = 0
def contarSismos(sismos, contador):
    for i in sismos:
        if(i >= 6.0):
            contador += 1
    print (contador) 
contarSismos(sismos, contador)