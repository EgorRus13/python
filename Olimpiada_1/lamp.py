n = int(input())
c=0
for i in range(n):
    op=input()
    if op == "X++" or op == "++X":
        c += 1
    elif op == "X--" or op == "--X":
        c -= 1

print(c)