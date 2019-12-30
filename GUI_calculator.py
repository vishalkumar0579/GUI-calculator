#
# from tkinter import *
# root=Tk()
#
# root.geometry("200x290")
#
# envalue=StringVar()
# en=Frame(root,relief=SUNKEN,borderwidth=4)
# en.pack(fill=X,pady=3)
# Entry(en,textvariable=envalue,font="lucida 9 bold").pack(fill=X)
#
# f1=Frame(root,relief=GROOVE,borderwidth=2,width=43,bg='#333')
# f1.pack(side=LEFT,fill=Y,padx=3)
# f1.config(width=150)
#
# def click(event):
#         global envalue
#         value=str(event.widget.cget("text"))
#         if value=='=':
#                 try:
#                         if envalue.get().isdigit():
#                                 envalue.set(envalue.get())
#                         else:
#                                 x=eval(envalue.get())
#                                 envalue.set(x)
#                 except:
#                         envalue.set('Bewakuf h two dekhe tune plus hote hue')
#         elif value=="c":
#                 envalue.set("")
#         else:
#                 envalue.set(envalue.get()+value)
# k=0
# l=0
# c=0
# for j in range(1,10)[::-1]:
#     b1=Button(f1,text=j,padx=16,pady=19)
#     b1.place(x=k,y=l)
#     b1.bind('<Button-1>',click)
#     k+=50
#     c+=1
#     if c==3:
#         l+=65
#         c=0
#         k=0
#
# b1=Button(f1,text="0",padx=15,pady=15)
# b1.place(x=k+50,y=l)
# b1.bind('<Button-1>',click)
# b1=Button(f1,text=".",padx=15,pady=15)
# b1.place(x=k+2,y=l)
# b1.bind('<Button-1>',click)
# b1=Button(f1,text="00",padx=15,pady=15)
# b1.place(x=k+98,y=l)
# b1.bind('<Button-1>',click)
#
#
# f2=Frame(root,relief=GROOVE,borderwidth=2,bg="#333")
# f2.pack(side=RIGHT,fill=Y,padx=3)
# f2.config(width=150)
#
# x1=0
# y1=0
# sign=['c','=','+','-','*','/']
# for j in sign:
#         if j!='-' or j!='c' or j!='*' or j!='/':
#                 b1=Button(f2,text=j,padx=8,pady=6)
#                 b1.place(x=x1,y=y1)
#                 b1.bind('<Button-1>',click)
#         if j=='c' or j=='*' or j=='/' or j=='-':
#                 b1=Button(f2,text=j,padx=9,pady=6,width='1')
#                 b1.place(x=x1,y=y1)
#                 b1.bind('<Button-1>',click)
#         y1+=43
# root.mainloop()
#
#
# # ////////////////////////////////////////////////////////////////////////////////////////////////////////
#
#
# exit()

#////////////////////////////MY PROGRAM///////////////////////////////////////////////////////////////////
from tkinter import *
root = Tk()
root.geometry("380x680")
root.title("Calculator By VISHAL")
root.wm_iconbitmap("download8.ico")


scvalue = StringVar()
scvalue.set("")
screen = Entry(root, text=scvalue, font="lucida 40 bold",relief=SUNKEN,borderwidth=4)
screen.pack(fill=X, ipadx=8, padx=10, pady=10)

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error"


        scvalue.set(value)
        screen.update()
    elif text == "c":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

#frame
# ////////////C,<,%,/,/////////////////////////////
f1= Frame(root,bg="grey",relief=GROOVE,borderwidth=2)
b = Button(f1, text="C", font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=9, pady=8)
f1.pack()

b = Button(f1, text="<", font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=9, pady=8)

b = Button(f1, text="%", font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=9, pady=8)

b = Button(f1, text="/", font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=9, pady=8)



# //////////////7,8,9,X////////////////////

f1= Frame(root, bg="grey",relief=GROOVE,borderwidth=2)
b = Button(f1, text="7", font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=12, pady=10)
f1.pack()

b = Button(f1, text="8", font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=10, pady=10)

b = Button(f1, text="9", font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=10, pady=10)

b = Button(f1, text="*", font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=12, pady=10)


# ////////////////4,5,6,-////////////////////////////////
f1= Frame(root, bg="grey",relief=GROOVE,borderwidth=2 )
b = Button(f1, text="4", font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=12, pady=10)
f1.pack()

b = Button(f1, text="5", font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=12, pady=10)

b = Button(f1, text="6", font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=12, pady=10)

b = Button(f1, text="-", font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=12, pady=10)


# /////////////////////////////////////////
f1= Frame(root, bg="grey",relief=GROOVE,borderwidth=2)
b = Button(f1, text="1", font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=11, pady=10)
f1.pack()

b = Button(f1, text="2", font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=10, pady=10)

b = Button(f1, text="3", font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=10, pady=10)

b = Button(f1, text="+", font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=11, pady=10)

# ////////////////////////////////////////
f1= Frame(root, bg="grey",relief=GROOVE,borderwidth=2)
b = Button(f1,  text="fc", font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=10, pady=9)
f1.pack()

b = Button(f1, text="0", font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=10, pady=10)

b = Button(f1, text=".", font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=10, pady=10)

b = Button(f1,text="=", font="lucida 35 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=10, pady=10)

# ///////////////////////////////////

root.mainloop()