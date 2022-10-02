#x = "я строка, я карта, я антон"
#print(x[-5:])
#print(x[:8])

#x = input("введи слово:")
#temp = x[-1]
#index = x.index(temp)
#print(index + 1)

#print(len(x))

#path = "C:/Python3/python.exe"
#print("имя файла:", path[-10:])
#print("расширение:", path[-3:])
#print("имя каталога:", path[3:9])
#print("полный путь к каталогу:", path[0:10])

#path2 = path.split("/")
#print(path2)
#
#print("имя файла:", path2[-1])
#print("расширение:", path2[-1][-3:])
#print("имя каталога:", path2 [1])
#print(f"полный путь к каталогу: {path2[0]}/{path2[1]}")


#chapter_1 = input("глава 1:")
#page_1 = input("страница:")
#
#chapter_2 = input("глава 2:")
#page_2 = input("страница:")
#
#chapter_3 = input("глава 3:")
#page_3 = input("страница: ")
#
#print(chapter_1.rjust(15), page_1.rjust(15))
#print(chapter_2.rjust(15), page_2.rjust(15))
#print(chapter_3.rjust(15), page_3.rjust(15))

x = "12'345'678"
#temp = x.split("'")
#print(temp)
#number = int(temp[0] + temp[1] + temp[2])
#print(number)

#temp = x[0:2] + x[3:7] + x[-3:]
#number = int(temp)
#print(number)

temp = x.replace("'", "")
print(temp)