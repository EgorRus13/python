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
n=int(input("Секунд с начала дня: "))
h=n//3600
m=n//60
s=n%60
print(f"Прошло {h} часов и {m} минут и {s} секунд")