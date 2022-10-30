# try:
#     x=5/0
#     int("x")
# except ZeroDivisionError:
#     print("Деление на ноль.")
# except Exception:
#     print("Я обработаю все!")


# try:
#     x=int(input("Введи число:"))
# except ValueError:
#     print("Э,давай цифру")
# else:
#     print("Ура, победа!")
# finally:
#     print("Кто я?")

# try:
#     name=input("Введите имя: ")
#     if name=="Антон":
#         raise Exception("Антона нельзя!")
# except Exception as error_message:
#     print("Ты ошибся😒")
#     print("Ошибка плохая😢:", error_message)

try:
    x = 5/0
except ZeroDivisionError:
    pass


if 5 > 3:
    pass

temperatura=50
print()
x // 5