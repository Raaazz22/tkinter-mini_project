# Dictionary

from tkinter import *
def sear():
 dict = {"php":"a server side language" , "python":"High level language ,\n developed by Guido vann Rosoum" , "html":"Hyper text \n markup language", "css":"cascading stylesheet", 
   "js":"Java script"}
 word=str(search.get().lower())
 res = dict[word]
 output.config(text=str(res))

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


img= PhotoImage(file='book2.png', master= root)
img_label= Label(root,image=img)
img_label.place(x=0, y=0)
  

search = Entry(root,font=("Arial 20"))
search.place(x=40,y=40)

find = Button(root,text="Search",bg="SkyBlue1",width=10,fg="white",font=("Arial 15"),command=sear)
find.place(x=50,y=100)

clear = Button(root,text="Clear",width=10,bg="SkyBlue1",fg="white",font=("Arial 15"),command=clear)
clear.place(x=210,y=100)

output=Label(root,fg="black",font=("Arial 15"),height=7,width=27)
output.place(x=40,y=170)

close = Button(root,text="Close",bg="red",width=5,fg="white",font=("Arial 10"),command=close)
close.place(x=150,y=350)



root.mainloop()
