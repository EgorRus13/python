input()
kamu=input()
perepeskamu=list(kamu)
perehod=0
s=0
while perehod < len(perepeskamu) - 1:
    if perepeskamu[perehod] == perepeskamu[perehod + 1]:
        perepeskamu.pop(perehod)
        s += 1
    else:
        perehod += 1
print(s)
