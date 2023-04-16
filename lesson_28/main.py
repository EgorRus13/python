from tkinter import *
# def hell_o(event):
#     # print("Privet")
#     message=ent.get()
#     ent.delete(0, END)
#     print(message)
#
#     message2=txt.get(1.0, END)
#     txt.delete(0.0, END)
#     print(message2)
#
# root = Tk()
# root.title("С пасхой!")
# root.geometry("400x500")
# root["bg"]="lightblue"
#
# lab=Label(root, text="Христос воскрес!")
# lab["bg"] = "pink"
# lab["fg"] = "red"
# lab.pack()
# lab["font"] = 100
# lab["font"] = "TimesNewRoman 20 italic"
# lab["font"] = ("Times New Roman", 30,"bold","italic","underline")
#
# btn=Button(root, text="Najmi", font=20,width=30,height=10,borderwidth=15)
#            #command=hell_o
# btn.pack()
# btn.bind("<Button-1>", hell_o)
# ent =Entry(root,bd=10,font=20,width=15)
# ent.pack()
# txt=Text(root, width=20, height=5)
# txt.pack()

#root.mainloop()

def udalit(event):
    message=ent.get()
    ent.delete(0,END)
    print(message)
    message2=ent.get(1.0,END)
    ent.delete(0.0,END)
    print(message2)

root=Tk()
root.geometry("500x500")

lab=Label(root,text="Your adress:", bg="wheat")
lab.pack()

ent=Entry(root, width=30,bd=5)
ent.pack()

lab1= Label(root,text="Comment:")
lab1.pack()

ent1=Entry(root, width=30)
ent1.pack()




root.mainloop()

