#

# def hello_world():   #обьявление функции
#     print("hello_world")
#
# hello_world()   #вызов функции

# def plus(chislo1:int,chislo2:str) ->  int:
#     """
#
#     :param chislo1:
#     :param chislo2:
#     :return:
#     """
#     answer=chislo1+chislo2
#     return answer
#
# x=plus(54,88)
# print(x+2)




# def is_sorted(list_one,):
#     clone_l=sorted(list_one)
#     if list_one==clone_l:
#         return True
#
# l=[1,2,3,4,5]
# if is_sorted(l):
#     print("print")
# else:
#     print("not print")
def min_max(qwe):
    mini=qwe[0]
    maxi=qwe[0]
    for i in qwe:
        if i > maxi:
            maxi=i
        elif i < mini:
            mini=i
    return mini,maxi
qwe=[4,5,3,6,7,1,3,5,76,7,5,7,4,6,4,1000-7,56,6,3,2,56,3,5,7,6,5]
print(min_max(qwe))