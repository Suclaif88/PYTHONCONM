P = str(input())

V = ['a','e','i','o','u']

for Vo in V:
    R = 'SI' if Vo in P else 'NO'
    print(Vo+ ": " + R)
    
    # funcionalidad de Python 3.6 y versiones posteriores la f-string no será reconocida y causará un error