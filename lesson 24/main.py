# class Car:
#     def __init__(self, wheel, doors, pdk):
#         self.wheels=wheel
#         self.doors=doors
#         self.pdk=pdk
#         self.__probeg =10_000
#
#
#     def go_out(self):
#         if self.pdk==True:
#             self.pdk=False
#             return "izgnali"
#         else:
#             return "ypa"
#     def __obl(self):
#         self.__probeg=0
#     def selling(self):
#         self.__obl()
#
# nissan=Car(wheel=8,doors=8,pdk=False)
# print(nissan.pdk)
# nissan.pdk=True
# nissan.__probeg=500
# print(nissan.__probeg)


# import string
# class Alphabet:
#     def __init__(self):
#         self.__lang="eng"
#         self.__letters=string.ascii_lowercase
#     def print(self):
#         return self.__letters
#     def lenka_pomogi(self):
#         return len(self.__letters)
# alpha=Alphabet()
# print(alpha.print())
# print(alpha.lenka_pomogi())

# class Car:
#
#     def go(self):
#         return ("Поехал")
#
#     def stop(self):
#         return ("Остановился")
#
#     def ckok_let(self, year):
#         self.year = year
#         return self.year
#
#     def marka(self, type):
#         self.type = type
#         return self.type
#
#     def cvet(self, color):
#         self.color = color
#         return self.color
#
#
# opel = Car()
# print(opel.go())
# print(opel.stop())
# print(opel.ckok_let(1900))
# print(opel.marka("opel"))
# print(opel.cvet("grey"))
#




import datetime

class Chasi:
    def __init__(self):
        self.__h, self.__m, self.__s=datetime.datetime.now().strftime("%H:%M:%S").split(":")
        self.__h, self.__m, self.__s=int(self.__h),int(self.__m), int(self.__s)

    def addH(self):
        self.__h+=1
    def addM(self):
        self.__m += 1
    def addS(self):
        self.__s += 1

    def vivod(self):
        return f"{self.__h}:{self.__m}:{str(self.__s).ljust(2,'0')}"
luboe=Chasi()
luboe.addH()
print(luboe.vivod())

