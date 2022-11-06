# lst=["Биба","Боба","Олег","Бебра","Андрей"]
# for element in lst:
#     print(element)
# for i in range(0,10):
#     print(i)

# is_game=True
# while is_game==True:
#     if  input("да/нет:") =="нет":
#         is_game=False
#     print("sue")


# word=input("Введи слово: ")
# while word:
#     print(word,end=" ")
#     word=word[:-1]
# z=int(input("Введи число: "))
# while z:
#     z-=1
#     if z % 2==0:
#       print(z)

x=int(input("Введи число: "))
step=0
while x !=1:
    step+=1
    if x % 2==0:
        x=x//2
        print(f"{step})",end=" ")
        print(x,"/2",end="= ")
        print(x)
    else:
        print(f"{step})", end=" ")
        print(x, "*3", end=" ")
        x=3*x+1
        print(x)
print("Шагов: ",step)