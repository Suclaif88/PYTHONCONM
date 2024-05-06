import random

Gusanos = []

with open("gusanos.txt", "r") as texto:
    for linea in texto:
        valores = linea.strip().split(",")
        valores_enteros = [int(valor) for valor in valores]
        Gusanos.extend(valores_enteros)

print("--Creando los gusanos en las ubicaciones--")
print()


def mostrar(Gusanos):
    print("-------------")
    print(f"FB: {Gusanos[0]} | AR: {Gusanos[1]}")
    print("-------------")
    print(f"NA: {Gusanos[2]} | PP: {Gusanos[3]}")
    print("-------------")

def Disparar(Gusanos):
  posicionADisparar = int(input("Ingrese la ubicación a disparar (0, 1, 2 ó 3): "))
  Gusanos[posicionADisparar] = Gusanos[posicionADisparar] - 10
  if Gusanos[posicionADisparar] < 0:
    Gusanos[posicionADisparar] = 0
    print()
    
def Pesticida(Gusanos):
    Gusanos[0] = int(Gusanos[0] - Gusanos[0] / 2)
    Gusanos[1] = int(Gusanos[1] - Gusanos[1] / 2)
    Gusanos[2] = int(Gusanos[2] - Gusanos[2] / 2)
    Gusanos[3] = int(Gusanos[3] - Gusanos[3] / 2)
    print()

def Vientecito(Gusanos):
    Ubi = random.randint(0,3)
    print("Un viento mágico ha soplado en una ubicacion reviviendo 10 gusanos...")
    Gusanos[Ubi] += 10
    print()

def lluviaA(Gusanos):
    posicionN = int(input("Ingrese la ubicación de la nube (0, 1, 2 ó 3): "))
    Gusanos[posicionN] = 0
    print()

def La_tia(Gusanos):
    Frases = ["¡No olviden lavarse bien las manos después de jugar con los gusanos!",
              "¡Cuidado con esos gusanitos! Son criaturas de Dios",
              "¡¡No hagas a los demás lo que no quieres que te hagan a ti!!",
              "¡Qué lindo verlos jugar con los gusanos! Pero no le hagan daño a los gusanos"]
    print(random.choice(Frases))
    print()
    Gusanos[0] += 5
    Gusanos[1] += 5
    Gusanos[2] += 5
    Gusanos[3] += 5
    print("La tia agrego 5 gusanos a todas la ubicaciones ¡¡¡portate bien!!!")
    print()
    
def Misterio(Gusanos):
    Op = ["¡El unicornio de peluche te ayudo!",
          "Te resbalaste y presionaste por accidente un boton: "]
    Op_elegido = random.choice(Op)
    if Op_elegido == Op[0]:
        print(Op_elegido)
        Gusanos[0] = 0
        Gusanos[1] = 0
        Gusanos[2] = 0
        Gusanos[3] = 0
    else:
        print(Op_elegido)
        Accion = random.randint(1,5)
        if(Accion == 1):
            print("1.) Disparar a gusanos de una ubicación particular")
            Disparar(Gusanos)
        elif(Accion == 2):
            print("2.) Lanzar pesticida a todos los gusanos de todas las ubicaciónes")
            Pesticida(Gusanos)
        elif(Accion == 3):
            print("3.) Se desato el poder de la virgen")
            Vientecito(Gusanos)
        elif(Accion == 4):
            print("4.) Envia una lluvia acida")
            lluviaA(Gusanos)
        elif(Accion == 5):
            print("5.) Escuchar la cantaleta de la tia")
            La_tia(Gusanos)
            
def Terminar(Gusanos):
    if Gusanos[0] == 0 and Gusanos[1] == 0 and Gusanos[2] == 0 and Gusanos[3] == 0:
        print("¡Felicitaciones salvaste la Galaxia!")
        return True
    return False

def PromedioG(Gusanos):
    Acumulador = 0
    for i in Gusanos:
        Acumulador += i
    Prom = Acumulador / len(Gusanos)
    print("-----------------------------")
    print("El promedio de gusanos en total es:",Prom)
    print("-----------------------------")
        

while(True):
  mostrar(Gusanos)
  if Terminar(Gusanos):
        break
  print("--Ingrese--")
  print("1.) Para disparar a gusanos de una ubicación particular")
  print("2.) Para lanzar pesticida a todos los gusanos de todas las ubicaciónes")
  print("3.) Para desatar el poder de la virgen")
  print("4.) Para enviar una lluvia acida")
  print("5.) Para escuchar la cantaleta de la tia")
  print("6.) ???")
  print("7.) Calcular el promedio de gusanos")
  
  Accion = int(input())
  if(Accion == 1):
    Disparar(Gusanos)
  elif(Accion == 2):
    Pesticida(Gusanos)
  elif(Accion == 3):
    Vientecito(Gusanos)
  elif(Accion == 4):
    lluviaA(Gusanos)
  elif(Accion == 5):
    La_tia(Gusanos)
  elif(Accion == 6):
    Misterio(Gusanos)
  elif(Accion == 7):
    PromedioG(Gusanos)
  else:
    print("Opción inválida")
