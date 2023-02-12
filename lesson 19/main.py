def abvgedeika(s):
    return s[::-1]
alphabetmaxi = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
alphabetmini = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
reversebig=abvgedeika(alphabetmaxi)
reversesmall=abvgedeika(alphabetmini)

sms = input("Введи слово для шифрования:")
word = ''
for i in sms:
    if i not in alphabetmaxi and i not in alphabetmini:
        word=word+i
        continue
    if i .isupper():
        ind = alphabetmaxi.index(i)
        letter = reversebig[ind]
    else:
        ind = alphabetmini.index(i)
        letter = reversesmall[ind]
    word = word + letter
print(word)
