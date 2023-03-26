# class Human:
#     location="Novosibirsk"
#     __priv="Chto-to"
#     def __init__(self,rost=1, ves=100):
#         self.h =rost
#         self.j =ves
#
#     def public(self):
#         pass
#
#     def __private(self):
#         pass
#
# peson=Human(47)
# peson2=Human(48)
# peson3=Human(49)
# peson4=Human(50)
# print(peson.h)
# print(peson.j)
from random import randint
class Human:

    default_name="human"
    default_age=30

    def __init__(self,age=default_age,name=default_name):
        self.age= age
        self.name= name
        self.__money=850000
        self.__house=None

    def info(self):
        return(self.name,self.age,self.__money,self.__house)

    def earn_money(self):
        self.__money += 250000

    def default_info(self):
        return(self.default_age,self.default_name)

    def __make_deal(self,dom):
        if self.__money >= dom.final_price():
            self.__money -= dom.final_price()
            return True

    def buy_house(self,dom):
        if self.__make_deal(dom):
            dom.owner=self.name
            self.__house=dom
            return "Dom kyplen"
        else:
            return f"Ne hvataet.Nado{self.__money >= dom.final_price()}"

class House:
    def __init__(self,ar="Novosibirsk",pr=1000000):
        self.__area= ar
        self.__price= pr
        self.skidka=randint(5,25) / 100

    def final_price(self):
        return  self.__price - (self.__price * self.skidka)

artem=Human()
dom1=House()
print(dom1.final_price())
print(artem.buy_house(dom1))






