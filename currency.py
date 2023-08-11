# currency convertor

from tkinter import*
from tkinter import ttk

def convert():
 try:
  n=int(input1.get())
  first =str(input2.get())
  second =str(input3.get())
 
  if first=="Rupees" and second=="Dollar" :
   res = n*0.012
   output.config(text=str(n) + " Rs. " + " = " + str(res) + " $ " )

  elif first=="Dollar" and second=="Rupees" :
   res = n*82
   output.config(text=str(n) + " $ " + " = " + str(res) + " Rs. " )
 
  elif first==second :
   output.config(text=str("No change"))

 except ValueError:
   output.config(text="Enter number")

 
 

root = Tk()

root.geometry("500x280+200+200")
root.title("Currency Convertor")
root.resizable(False,False)
root.configure(bg="black")
photo = PhotoImage(file = "cur.png")
root.iconphoto(False, photo)


lbl1 = Label(root,text="Currency Convertor" , fg="green2" ,bg="black" ,font=("Arial 25 bold"))
lbl1.place(x=100,y=20)

input1=Entry(root,fg="black",font=("Arial 15"),width=10)
input1.place(x=40,y=100)

input2 = ttk.Combobox(root,width=7)
input2.place(x=160,y=100)
input2["values"]=("Rupees" , "Dollar")
input2["state"]="readonly"
input2.current(0)

input3 = ttk.Combobox(root,width=28)
input3.place(x=40,y=150)
input3["values"]=("Rupees" , "Dollar")
input3["state"]="readonly"
input3.current(1)


submit = Button(root,text="Convert" , bg="green2" , fg="black",font=("Arial 15 bold"),command=convert)
submit.place(x=80,y=200)


result =  Label(root,text="Result" , fg="green2" ,bg="black" ,font=("Arial 15 italic"))
result.place(x=350,y=110)

output =  Label(root,fg="white" ,bg="black" ,font=("Arial 20 bold"))
output.place(x=280,y=160)

end=Label(root,text="Designed and Developed by - Raj chaudhary",fg="white",bg='black',font=("Arial 10 italic")).place(x=210,y=250)




root.mainloop()