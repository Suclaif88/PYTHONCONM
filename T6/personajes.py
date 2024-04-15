PF = []
N = int(input())

for i in range(N):
    NP = input()
    if not NP.startswith("L"):
        PF.append(NP)

print(PF)
