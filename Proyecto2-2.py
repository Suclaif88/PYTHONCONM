import random

gusanos = []

with open("gusanos.txt", "r") as texto:
    for l in texto:
        va = l.strip().split(",")
        valoresinsertar = [int(valor) for valor in va]
        gusanos.extend(valoresinsertar)

def mostrar(gusanos):
    print("---------------")
    print("FB:", gusanos[0],"| AR:", gusanos[1])
    print("---------------")
    print("NA", gusanos[2], "| PP:", gusanos[3])
    print("---------------")

def disparar(gusanos):
    posicionADisparar = int(input("Ingrese la ubicación a disparar (0, 1, 2 ó 3): "))
    if gusanos[posicionADisparar] >= 10:
        gusanos[posicionADisparar] -= 10
    else:
        gusanos[posicionADisparar] = 0

def lanzar_pesticidas(gusanos):
    gusanos[0] //= 2
    gusanos[1] //= 2
    gusanos[2] //= 2
    gusanos[3] //= 2

def revivir_gusanos(gusanos):
    ubicacion = random.randint(0, 3)
    gusanos[ubicacion] += 10
    
def lluvia_acida_concentrada(gusanos):
    posicionADisparar = int(input("Ingrese la ubicación a disparar (0, 1, 2 ó 3): "))
    gusanos[posicionADisparar] = 0

def consejo_tia(gusanos):
    frases_tia = [
    "¡Ay, ay, ay! ¡No toquen esos gusanitos, pueden ensuciarse las manos!",
    "¡Dejen a los pobres gusanitos tranquilos, que están haciendo su trabajo en el jardín!",
    "¡Uy, qué asco! Mejor jueguen con las muñecas o los carritos, ¿no?",
    "¡Cuidado, cuidado! No vayan a lastimar a los animalitos, son seres vivos también.",
    "¡Bueno, pero si quieren jugar con bichitos, vamos a buscar mariposas o mariquitas, ¿les parece?"
]
    f = random.choice(frases_tia)
    print(f)
    gusanos[3] += 10
    print("¡Han llegado 10 nuevos gusanos a Pueblo Paleta!")
     
def migracion_gusanos(gusanos):
    print("Seleccione la ubicación de origen (0: Fondo de Bikini, 1: Arrakis, 2: Namekusei, 3: Pueblo Paleta):")
    origen = int(input())
    
    print("Seleccione la ubicación de destino (0: Fondo de Bikini, 1: Arrakis, 2: Namekusei, 3: Pueblo Paleta):")
    destino = int(input())

    print("Ingrese la cantidad de gusanos que desea migrar:")
    cantidad = int(input())

    if gusanos[origen] >= cantidad:
        gusanos[origen] -= cantidad
        gusanos[destino] += cantidad
        print("¡Migración exitosa!")
    else:
        print("No hay suficientes gusanos en la ubicación de origen para realizar la migración.")
        
def verificar_gusanos(gusanos):
    if gusanos.count(0) == len(gusanos):
        print("¡Felicitaciones! Salvaste la Galaxia.")
        return True
    return False

def prom_gusanos(gusanos):
    C = 0
    for i in gusanos:
        C += i
    promedio = C / len(gusanos)
    print("promedio de los gusanos es:"+promedio)

while True:
    mostrar(gusanos)
    if verificar_gusanos(gusanos):
        break
    print("--Ingrese--")
    print("1) para disparar a gusanos de una ubicación particular")
    print("2) para lanzar pesticidas a todos los gusanos")
    print("3) viento de la rosa de guadalupe")
    print("4) para lanzar lluvia acida")
    print("5) para escuchar un consejo de la tía")
    print("6) para realizar una migración de gusanos entre ubicaciones")
    print("7) para promedio de gusanos")


    accion = int(input())
    if accion == 1:
        disparar(gusanos)
    elif accion == 2:
        lanzar_pesticidas(gusanos)
    elif accion == 3:
        revivir_gusanos(gusanos)
    elif accion == 4:
        lluvia_acida_concentrada(gusanos)
    elif accion == 5:
        consejo_tia(gusanos)
    elif accion == 6:
        migracion_gusanos(gusanos)
    elif accion == 7:
        prom_gusanos(gusanos)
    else:
        print("Opcion no valida")
    
