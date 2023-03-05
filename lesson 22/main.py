import json

# open("я геннадий.txt", "w", encoding="utf-8").write("Приффки Я геннадий")  # .TXT
# open("я геннадий.json", "w").write("H")


# JSON. ЗАПИСЬ.
# text = [1, 5.3, True, None, [1, 2], (5, 7), "ENG", "РУС"]
# f = open("я геннадий.json", "w", encoding="utf-8")
# json.dump(text, f, ensure_ascii=False)  # в json + запись
# b = json.dumps(text, ensure_ascii=False)  # в json
# print(b)
# f.close()


# JSON. ЧТЕНИЕ
# f = open("я геннадий.json", "r", encoding="utf-8")
# # content = f.read()
# content = json.load(f)
# print(content)
# print(type(content))
# f.close()


# f = open("Ягеннадий2.txt", "r", encoding="utf-8")
#
# con = f.readlines()
# f.close()
# slovarishe = {}
#
# for elementiki in con:
#     print(elementiki)
#     lomka = elementiki.split(": ")
#     print(lomka[0])
#     print(lomka[1])
#     slovarishe[lomka[0]] = lomka[1].rstrip("\n")
#
#
# print(slovarishe)
# ff = open("Ягеннадий2.json", "w", encoding="utf-8")
# json.dump(slovarishe, ff,ensure_ascii=False)
# ff.close()


# Zadacha2-------------------------------------------------------------
f = open("я геннадий.json", "r", encoding="utf-8")
content = json.load(f)
f.close()
print(content)
for i, em in enumerate(content):
    if type(em) == str:
        content[i] += "!"
print(content)


