n = int(input())
a = 0

for i in range(n):
    zadachi=input()
    print(zadachi.split(" "))
    x=int(zadachi[0])
    y=int(zadachi[1])
    z=int(zadachi[2])
    if x+y+z>=2:
        a+=1