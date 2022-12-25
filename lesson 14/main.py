# множества.
# 1)Повторения исключены.
# 2)Внутри только неизменяемые типы данных.
# 3)Неупорядоченное содержимое.
# 4)Пустое множество - только set().

# словари
# 1)Пустой словарь - либо dict(), либо {}.
# 2){Ключ: значение} в качестве ключа допускаются любые типы данных.


# phrase="Я всегда я, когда я есть я.".lower()
# symbols=list("!.,?")
# ph_cleared=""
#
# for i in phrase:
#     if i not in symbols:
#         ph_cleared+=i
# l=ph_cleared.split(" ")
# d={}
# for element in l:
#     if element not in d:
#         d[element]=1
#     else:
#         d[element]+=1
# print(d)


# pok={"Чиспы":78,
#      "Кириешки":13,
#      "Яйца":70,
#      "МегаЯйцы":999}
# s=0
# # for i in pok:
# for i in pok.values():
#     s+=i
# print(s)




phrase="Я всегда я, когда я есть я.".lower()
symbols=list("!.,?")
ph_cleared=""

for i in phrase:
    if i not in symbols:
        ph_cleared+=i
l=ph_cleared.split(" ")
d={}
for element in l:
    if element not in d:
        d[element]=1
    else:
        d[element]+=1
print(d)
maxi=max(d.values())
print(maxi)
for(key, value) in d.items():
    if value==maxi:
        print(f"Максимальное значение_____{key},:{value}")