from tkinter import *
from tkinter import messagebox
win = Tk()
win.geometry("500x500")
#==============================================================
# def get_lst(e):
#     indxs=lstbox.curselection()
#     for ind in indxs:
#         print(lst[ind])
#
# lst=["One", "Two", "Three"]
# lstbox = Listbox(win, selectmode=EXTENDED,
#                  bg="pink",
#                  fg="red",
#                  selectbackground="black",
#                  selectforeground="lightblue",
#                  selectborderwidth=10)
# lstbox.pack()
# # Button(win, text="button", command=get_lst).pack()
#
# lstbox.bind("<<ListboxSelect>>", get_lst)
#
# #через вставку циклом
# # for elem in lst:
# #     lstbox.insert(END, elem)
#
# #через переменную
# lst_tk=StringVar(value=lst)
# print(lst_tk.get())
# lstbox['listvariable']=lst_tk
# =======================================================================






# messagebox.showinfo("Information","You stupid")
# messagebox.showerror()
# messagebox.showwarning()

#==============================================================================
# Button(win, text="Baldej").pack(side=LEFT)
# Button(win, text="Baldej").pack(side=RIGHT)
# Button(win, text="Baldej").pack(side=BOTTOM)
# Button(win, text="Baldej").pack(fill=BOTH, expand=True)

# Button(win, text="Baldej").pack(pady=50, ipadx=20)
# Button(win, text="Baldej").pack(pady=50)



# Button(win, text="button1").grid(column=0, row=0)
# Button(win, text="button2").grid(column=1, row=0)
# Button(win, text="button3").grid(column=2, row=0, rowspan=2, sticky=NS)
# Button(win, text="button4").grid(column=0, row=1, columnspan=2, sticky=EW)




# Button(win,text="button").place(x=10, y=10)

# def hello(e):
#     print("hello")
#     win.after(1, hello)
#
# win.after(2000, hello)

# def hello(e):
#     print("hello")
#
# btn=Button(win, text="button")
# btn.pack()
# btn.focus_set()
# # btn.bind("<Enter>", hello)
# # btn.bind("<MouseWill>", hello)
# btn.bind("<Return>", hello)






























win.mainloop()


