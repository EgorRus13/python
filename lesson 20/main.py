# f=open("pivo.txt","w",encoding="utf-8")
#
# f.write("Hello world\n")
# f.write("Привет мир")
#
# f.close()

# f=open("pivo.txt","r",encoding="utf-8")
# content=f.readlines()
# # print(content[0])
# for line in content:
#     print(line)
# f.close()


# name=input("Введи имя файла:")
# content=input(">>>")
# f=open(name+".txt","w",encoding="utf-8")
# while content!="":
#     f.write(content+"\n")
#     content = input(">>>")
# f.close()

f0=open("data.txt","r",encoding="utf-8")
v=f0.readlines()
f0.close()
nf=0
while v!=[]:
    nf=nf+1
    fm=open(str(nf)+".txt","w",encoding="utf-8")
    ts=v[:3]
    for line in ts:
        fm.write(line)
    del v[:3]
