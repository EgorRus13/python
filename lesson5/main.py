# x=10
# if x<=10 or x==15:
#     print("Икс не больше 10 или равен 15")
# else:
#     print("Икс больше 10")
# x=10
# print(x==10)
# print(x==5)
# x=int(input("Введите число: "))
# if x<0:
#     print("Отрицательное")
# elif x>0:
#     print("Положительное")
# else:
#     print("Нолик")
# year=int(input("Введи год: "))
# if year%4==0 and (year%400==0 or year%100!=0):
#     print("Високосненько")
# else:
#     print("Не викосненько:(")
# number1=int(input("Введи первое число"))
# operation=input("Введи операцию(+,-,*,/)")
# number2=int(input("Введи второе число"))
# lst=["+","-","*","/"]
# if operation in lst:
#     if operation=="+":
#         print(number1+number2)
#     if operation == "-":
#         print(number1 - number2)
#     if operation == "*":
#         print(number1 * number2)
#     if operation=="/":
#         print(number1/number2)
# number1=int(input("Введи первое число: "))
# number2=int(input("Введи второе число: "))
# number3=int(input("Введи третье число: "))
# counter_plus=0
# counter_minus=0
# if number1>0:
#     counter_plus+=1
# else:
#     counter_minus+=1
# if number2 > 0:
#     counter_plus += 1
# else:
#     counter_minus += 1
# if number3>0:
#     counter_plus+=1
# else:
#     counter_minus+=1
# print("Сколько положительных чисел:",counter_plus)
# print("Сколько отрицательных чисел:",counter_minus)
# number1=int(input("Введи первое число: "))
# number2=int(input("Введи второе число: "))
# number3=int(input("Введи третье число: "))
# lst=[number1,number2,number3]
# mini=min(lst)
# maxi=max(lst)
# print("Минимальное:",mini)
# print("Максимальное:",maxi)
ticket=input("Введи номер билета:")
if len(ticket)==6 and ticket.isdigit():
    one=ticket[:3]
    two=ticket[-3:]
    sum1=int(one[0])+int(one[1])+int(one[2])
    sum2 = int(two[0]) + int(two[1]) + int(two[2])
    if sum1==sum2:
        print("Твой билет счастливый!")
    else:
        print("Не повезло;)")
else:
    print("Не то ты ввел!")