#simple calculator

from tkinter import *

def add():
 try:
  n1=int(input_n1.get())
  n2=int(input_n2.get())
  res=n1+n2
  lbl_res.config(text="result : " + str(n1)+" + "+str(n2)+"  =  "+str(res))
 except ValueError:
  res = "Incorrect input"
  lbl_res.config(text=str(res))
 except TypeError:
  res = "Only integer allowed"
  lbl_res.config(text=str(res))
 

def sub():
 try:
  n1=int(input_n1.get())
  n2=int(input_n2.get())
  res=n1-n2
  lbl_res.config(text="result : " + str(n1)+" - "+str(n2)+"  =  "+str(res))
 except ValueError:
  res = "Incorrect input"
  lbl_res.config(text=str(res))
 except TypeError:
  res = "Only integer allowed"
  lbl_res.config(text=str(res))
 

def mul():
 try:
  n1=int(input_n1.get())
  n2=int(input_n2.get())
  res=n1*n2
  lbl_res.config(text="result : " + str(n1)+" * "+str(n2)+"  =  "+str(res))
 except ValueError:
  res = "Incorrect input"
  lbl_res.config(text=str(res))
 except TypeError:
  res = "Only integer allowed"
  lbl_res.config(text=str(res))

def div():
 try:
  n1=int(input_n1.get())
  n2=int(input_n2.get())
  res=n1/n2
  lbl_res.config(text="result : " + str(n1)+" / "+str(n2)+"  =  "+str(res))
 except ValueError:
  res = "Incorrect input"
  lbl_res.config(text=str(res))
 except TypeError:
  res = "Only integer allowed"
  lbl_res.config(text=str(res))
 except ZeroDivisionError:
  res = "Zero Division Error"
  lbl_res.config(text=str(res))



def clear():
 input_n1.delete(0, 'end')
 input_n2.delete(0, 'end')
 lbl_res.config(text=" ")



root = Tk()
root.title("Simple Calculator")
root.geometry("500x400+200+200")
root.resizable(False,False)
root.configure(bg='black')
photo = PhotoImage(file = "calc.png")
root.iconphoto(False, photo)




lbl_title=Label(root,text="Simple Calculator",fg="green3",bg='black',font=("Arial 25 bold")).place(x=120,y=25)

first=Label(root,text="Enter First number : ",fg="green2",bg='black',font=("Arial 15 bold")).place(x=10,y=100)
input_n1 = Entry(root,font=("Arial 15"))
input_n1.place(x=250,y=100)

second = Label(root,text="Enter Second number :",fg="green2",bg='black',font=("Arial 15 bold")).place(x=10,y=150)
input_n2 = Entry(root,font=("Arial 15"))
input_n2.place(x=250,y=150)

lbl_res=Label(root,fg="white",bg='black',font=("Arial 20 bold"))
lbl_res.place(x=210,y=220)

btn_add= Button(root,text="ADD",font=("Arial 15 bold "),fg="white",bg ="green3" ,width=5,command=add).place(x=25,y=290)
btn_sub= Button(root,text="SUB",font=("Arial 15 bold "),fg="white",bg ="green3",width=5,command=sub).place(x=120,y=290)
btn_mul= Button(root,text="MUL",font=("Arial 15 bold "),fg="white",bg ="green3",width=5,command=mul).place(x=215,y=290)
btn_div= Button(root,text="DIV",font=("Arial 15 bold "),fg="white",bg ="green3",width=5,command=div).place(x=310,y=290)
btn_clr= Button(root,text="Clear",font=("Arial 15 bold "),fg="white",bg ="green3",command=clear).place(x=405,y=290)


end=Label(root,text="Designed and Developed by - Raj chaudhary",fg="white",bg='black',font=("Arial 10 italic")).place(x=210,y=360)

root.mainloop()
