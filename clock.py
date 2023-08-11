from tkinter import*
import time

def clock():
	output =time.strftime("%I:%M:%S %p")
	lbl2.config(text=output)
	lbl2.after(200,clock)
root=Tk()
root.title("digital clock")
root.geometry("500x180+400+100")   #width and height of the the box
root.configure(bg='black')

root.resizable(False,False)
lbl=Label(root,text="Digital Clock",fg="green",font=("Arial 30 bold"),bg="black")
lbl.place(x=130,y=20)

lbl2=Label(root,font=("Arial 40 bold"),fg="white",bg="black")
lbl2.place(x=95,y=80)

end=Label(root,text="Designed and Developed by - Raj chaudhary",fg="green",bg='black',font=("Arial 10 italic")).place(x=210,y=150)

clock()
root.mainloop()