from tkinter import *
win=Tk()
# baton=Button(win, text="nigger")
# baton.pack()
# baton['text']="txt"
# baton['height']=3
# baton['width']=10
# baton['font']="Arial 15 bold italic overstrike underline"
# baton['bg']="orange"
# baton['fg']="darkred"
# baton['bd']=10






# def get_rb():
#     print(rb_val.get())
#
#
# rb_val = IntVar()
# rb1 = Radiobutton(win,
#                   text="click me",
#                variable=rb_val,
#                value=470,
#                command=get_rb)
# rb1.pack()
#
#
# rb2=Radiobutton(win,
#                 text="no click me",
#                variable=rb_val,
#                value=2,
#                command=get_rb)
# rb2.pack()


# def get_scala(val):
#     print(scala.get())
#
# scala=Scale(win, from_=80, to=1000, orient=HORIZONTAL, length=300, tickinterval=3, resolution=2, command=get_scala)
# scala.pack()





# img=PhotoImage(file="scala.png")
# img_big=img.subsample(2,2)
# img_small=img.zoom(1,1)
# lab=Label(win, image=img_big)
# lab.pack()


# Entry(win,bg="gold").pack()
# Entry(win,bg="magenta").pack(ipady=10,ipadx=50,pady=30)



# btn=Button(win, text="PEREKYS")
# btn.pack()
# btn['state']=DISABLED
#
# ent=Entry(win)
# ent.pack()
# ent.insert(0,"pi-pi py-py")
# ent['state']="readonly"
# def izmenenia():
#     if rb_val.get() == 1:
#         lab["text"]=start+" "+rb["text"]
#     else:
#         lab["text"]=start+" "+rb1["text"]
# rb_val=IntVar()
# start="Hello"
# lab=Label(win,text=start + " ...", font="Arial 15 normal")
# lab.pack()
# rb=Radiobutton(win, text="Arkasha", font="Arial 15 normal", variable=rb_val, value=1, command=izmenenia)
# rb.pack()
#
#
# rb1=Radiobutton(win, text="Vitalik", font="Arial 15 normal", variable=rb_val, value=2, command=izmenenia)
# rb1.pack()
from tkinter import *

win = Tk()
win.geometry("500x500")

# def click_rbm(event):
#     ent.get()
#     lab['text'] =ent.get()
#
#
# lab = Label(win, text="////")
# lab.pack()
#
#
# ent = Entry(win)
# ent.bind("<Button-3>", click_rbm)
# ent.pack()


# Задача №2
# def izmeneniya():
#     if rb_val.get() == 1:
#         lab["text"] = start + " " + rb["text"]
#     else:
#         lab["text"] = start + " " + rb1["text"]
#
# rb_val = IntVar()
# start = "Hello"
# lab = Label(win, text=start + " ...", font="Arial 15 normal")
# lab.pack()
# rb = Radiobutton(win, text="Arkasha",
#                  font="Arial 15 normal",
#                  variable=rb_val,
#                  value=1,
#                  command=izmeneniya)
# rb.pack()
# rb1 = Radiobutton(win, text="Vitalik",
#                   font="Arial 15 normal",
#                   variable=rb_val,
#                   value=2,
#                   command=izmeneniya)
# rb1.pack()
#


# Задача №3
# def get_cb():
#     print(cb_val.get())
#     if cb_val.get() == True:# cb актив
#         btn["state"] = "normal"
#     else:
#         btn["state"] = DISABLED
#
#
# cb_val = BooleanVar()
# cb = Checkbutton(win,
#                 text="Актевировать",
#                 variable=cb_val,
#                 onvalue=True,
#                 offvalue=False,
#                 command=get_cb)
# cb.pack()
# # cb.select()# активация cb
# # cb.deselect() # деактивация cb
#
#
# btn = Button(win, text="Не актив!", state=DISABLED)
# btn.pack()

# задача №5
colors = ('blue', 'red', 'black', 'orange', 'purple', 'yellow')


def get_scala(val):
    print(scala.get())  # значение либо так
    print(val)  # либо так

    win['bg'] = colors[scala.get()]


scala = Scale(win, from_=0, to=5,
              orient=HORIZONTAL,  # ориентация
              length=300,  # длина в пикселях
              command=get_scala
              )
scala.pack()











win.mainloop()