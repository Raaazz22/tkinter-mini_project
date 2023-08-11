# Temperature convertor

from tkinter import*
from tkinter import ttk

def convert():
 try:
  n=eval(input1.get())
  first =str(input2.get())
  second =str(input3.get())
 
  if first=="Celsius" and second=="Fahrenheit" :
   res = (n*1.8)+32
   output.config(text=str(n) + " C " + " = " + str(res) + " F " )

  elif first=="Fahrenheit" and second=="Celsius" :
   res = (n-32)/1.8
   output.config(text=str(n) + " F " + " = " + str(res) + " C " )
 
  elif first==second :
   output.config(text=str("No Change"))

 except ValueError:
   output.config(text="Enter Number")

 
 

root = Tk()

root.geometry("500x280+200+200")
root.title("Temperature Convertor")
root.resizable(False,False)
root.configure(bg="purple1")
photo = PhotoImage(file = "temp.png")
root.iconphoto(False, photo)


lbl1 = Label(root,text="Temperature Convertor" , fg="black" ,bg="purple1" ,font=("Arial 25 bold"))
lbl1.place(x=70,y=20)

input1=Entry(root,fg="black",font=("Arial 15"),width=10)
input1.place(x=40,y=100)

input2 = ttk.Combobox(root,width=7)
input2.place(x=160,y=100)
input2["values"]=("Celsius" , "Fahrenheit")
input2["state"]="readonly"
input2.current(0)

input3 = ttk.Combobox(root,width=28)
input3.place(x=40,y=150)
input3["values"]=("Celsius" , "Fahrenheit")
input3["state"]="readonly"
input3.current(1)


submit = Button(root,text="Convert" , bg="black" , fg="white",font=("Arial 15 bold"),command=convert)
submit.place(x=80,y=200)


result =  Label(root,text="Result" , fg="black" ,bg="purple1" ,font=("Arial 15 italic"))
result.place(x=350,y=110)

output =  Label(root,fg="white" ,bg="purple1" ,font=("Arial 20 bold"))
output.place(x=280,y=160)

end=Label(root,text="Designed and Developed by - Raj chaudhary",fg="black",bg='purple1',font=("Arial 10 italic")).place(x=210,y=250)




root.mainloop()