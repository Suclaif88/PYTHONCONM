nombreUsuario = input("Bienvenido al cajero reciclador, ingrese su nombre: ")
saldoPuntos = int(input("Ingrese sus puntos:"))
print(f"Hola {nombreUsuario}, Tu saldo de puntos es: {saldoPuntos}")

print("Seleccione una opción: ")
print("1.Ver saldo")
print("2.Reciclar tapas")
print("3.Promo del mes")
print("4.Lotería")
print("5.Salir")

opcion = int(input("Ingrese el numero de la opcion que quiera seleccionar: "))
if opcion == 1 :
    print("Tu saldo de puntos es:",saldoPuntos*2)
elif opcion == 2:
    cantidadTapas=int(input("Ingrese la cantidad de tapas a reciclar: "))
    print("Sus puntos son: ",cantidadTapas * 6)
elif opcion == 3:
    print("Añadiendo fondos clandestinos a tu cuenta...")
    print("Autodestruyendo...")
    print("3")
    print("2")
    print("1")
    print("...")
    saldoPuntos + 1000000
elif opcion == 4:
    print("Adivina un numero del 1 al 10: ")
    numero = int(input())
    if numero == 7:
        print("¡GANADOR!")
        saldoPuntos = saldoPuntos + 20000
    else:
        print("Lo siento",nombreUsuario,"no eres ganador :'(")
else:
    print("Saliendo...")
    
print("...................")
print(nombreUsuario,"el saldo final es de:",saldoPuntos,"puntos.")
print("Gracias por usar el cajero loco vuelva pronto... \U0001F92A")
print("Fin del programa")