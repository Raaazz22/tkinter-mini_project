# Dictionary using PyDictionary Module

from tkinter import *
from PyDictionary import PyDictionary
dict = PyDictionary()

def sear():
 word=search.get()
 mean = dict.meaning(word)
 output.config(text=mean['Noun'][0])

def clear():
 search.delete(0, 'end')
 output.config(text=" ")

def close():
 root.destroy()


root = Tk()

root.geometry("600x400+300+300")
root.title("Dictionary")
root.resizable(False,False)

photo = PhotoImage(file = "dict.png")
root.iconphoto(False, photo)


img= PhotoImage(file='book3.png', master= root)
img_label= Label(root,image=img)
img_label.place(x=0, y=0)

search = Entry(root,font=("Arial 20"))
search.place(x=40,y=40)

find = Button(root,text="Search",bg="SkyBlue1",width=10,fg="white",font=("Arial 15"),command=sear)
find.place(x=50,y=100)

clear = Button(root,text="Clear",width=10,bg="SkyBlue1",fg="white",font=("Arial 15"),command=clear)
clear.place(x=210,y=100)

output=Label(root,fg="black",font=("Arial 10"),height=10,width=37,bg="white")
output.place(x=40,y=170)

close = Button(root,text="Close",bg="red",width=5,fg="white",font=("Arial 10"),command=close)
close.place(x=150,y=350)



root.mainloop()
