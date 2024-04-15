nombre_del_candidato1 = str(input())
v1 = int(input())

nombre_del_candidato2 = str(input())
v2 = int(input())

if v1 > v2:
    print("El presidente electo es",nombre_del_candidato1)
elif v2 > v1:
    print("El presidente electo es",nombre_del_candidato2)
elif v1 == v2:
    print("Hay empate")
else:
    pass