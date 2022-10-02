# x=637
# print("Последняя цифра:",x//100)
# x=123
# first=x//100
# second=(x//10)%10
# tretie=x%10
# print(first,second,tretie)
#
# print(f"Сумма чисел{x}:",first+second+tretie)
# print("Введи стоимость одного пирожка")
# rub=int(input("Рублей"))
# cop=int(input("Копеек"))
# price_pie=rub*100+cop
# count=int(input("Сколько пирожков"))
# need_to_pay=count*price_pie
# print(f"С вас {need_to_pay//100} рублей и {need_to_pay%100} копеек")
# moneti=int(input("Отдаешь бабок:"))
# money_cop=moneti*100
# final_cdacha=money_cop-need_to_pay
# print(f"Сдача:{final_cdacha//100} рублей и {final_cdacha%100} копеек")
# x=int(input("Число"))
# first=x//100
# second=(x//10)%10
# tretie=x%10
# print("Произведение числа=",first*second*tretie)
# x=int(input("Число: "))
# if x%2==1:
#     x+=1
# else:
#     x=x+2
# print(x)
# d=int(input("Диаметр окружности: "))
# print("Диаметр окружности=", 3.14*d)
# r=float(input("Радиус окружности: "))
# print("Площадь=", 3.14*r*r)
# n=int(input("Секунд с начала дня: "))
# h=n//3600
# m=n//60
# s=n%60
#  print(f"Прошло {h} часов и {m} минут и {s} секунд")
# lst=["A","Б","В","Г","Д","Е","Ё","Ж","З"]
# print(lst[0],lst[1],lst[2],lst[3],lst[4])
# print(lst[0:5])
# print(lst[0:5:2])
# x="Egor"
# print(x[0:3])
# x="Andrey"
# print=(x)
# x=input("Введи слово: ")
# temp=x[-1]
# print(temp)
# print(x.index(temp)+1)
# print(len(x))
# x="C:\Python3\python.exe"
# print("Имя файла: ", x[11:22])
# print("Расширение: ",x[-3:])
# print("Имя каталога: ",x[3:10])
# print("Полный путь к файлу: ",x[0:10])
# x1=x.split("\\")
# print(x1)
# print("Имя файла: ",x1[2])
# chapter1=input("Глава 1:")
# page1=input("Страница:")
# chapter2=input("Глава 2:")
# page2=input("Страница:")
# chapter3=input("Глава 3:")
# page3=input("Страница:")
# print(chapter1.ljust(15),page1.rjust(30))
# print(chapter2.ljust(15),page2.rjust(30))
# print(chapter3.ljust(15),page3.rjust(30))
# temp=text.split("'")
# print(temp)
# temp2=temp[0]+temp[1]+temp[2]
# print(temp2)
# number=int(temp2)
text="12'345'678"
# temp=text[:2]+text[3:6]+text[7:]
# number=int(temp)
# print(temp)
temp=text.replace("'","")
number=int(temp)
print(temp)