from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5,)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10,)

def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))

def button_clean():
    e.delete(0,END)

def button_add():
    first_number = e.get()
    global f_num 
    global math
    math =  "addition"
    f_num = int(first_number)
    e.delete(0,END)

def button_equal():
    second_number = e.get()
    e.delete(0,END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))

def button_mult():
    first_number = e.get()
    global f_num 
    global math
    math =  "multiplication"
    f_num = int(first_number)
    e.delete(0,END)

def button_sub():
    first_number = e.get()
    global f_num 
    global math
    math =  "subtraction"
    f_num = int(first_number)
    e.delete(0,END)

def button_div():
    first_number = e.get()
    global f_num 
    global math
    math =  "division"
    f_num = int(first_number)
    e.delete(0,END)

button1 = Button(root,text="1",padx=40,pady=20,command=lambda: button_click(1),fg="blue",bg="white",activebackground="blue")
button2 = Button(root,text="2",padx=40,pady=20,command=lambda: button_click(2),fg="blue",bg="white",activebackground="blue")
button3 = Button(root,text="3",padx=40,pady=20,command=lambda: button_click(3),fg="blue",bg="white",activebackground="blue")
button4 = Button(root,text="4",padx=40,pady=20,command=lambda: button_click(4),fg="blue",bg="white",activebackground="blue")
button5 = Button(root,text="5",padx=40,pady=20,command=lambda: button_click(5),fg="blue",bg="white",activebackground="blue")
button6 = Button(root,text="6",padx=40,pady=20,command=lambda: button_click(6),fg="blue",bg="white",activebackground="blue")
button7 = Button(root,text="7",padx=40,pady=20,command=lambda: button_click(7),fg="blue",bg="white",activebackground="blue")
button8 = Button(root,text="8",padx=40,pady=20,command=lambda: button_click(8),fg="blue",bg="white",activebackground="blue")
button9 = Button(root,text="9",padx=40,pady=20,command=lambda: button_click(9),fg="blue",bg="white",activebackground="blue")
button0 = Button(root,text="0",padx=40,pady=20,command=lambda: button_click(0),fg="blue",bg="white",activebackground="blue")

button_plus = Button(root,text="+",padx=40,pady=20,command=lambda: button_add(),fg="blue",bg="white",activebackground="blue")
button_sum = Button(root,text="=",padx=90,pady=20,command=lambda: button_equal(),fg="blue",bg="white",activebackground="blue")
button_multiply = Button(root,text="*",padx=41,pady=20,command=lambda: button_mult(),fg="blue",bg="white",activebackground="blue")
button_subtract = Button(root,text="-",padx=41,pady=20,command=lambda: button_sub(),fg="blue",bg="white",activebackground="blue")
button_divide = Button(root,text="/",padx=41,pady=20,command=lambda: button_div(),fg="blue",bg="white",activebackground="blue")

button_clear = Button(root,text="Clear",padx=78,pady=20,command=lambda: button_clean(),fg="blue",bg="white",activebackground="blue")

#put button on the screen

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)

button_plus.grid(row=4,column=1)
button_subtract.grid(row=4,column=2)
button_multiply.grid(row=5,column=0)
button_divide.grid(row=6,column=0)


button_clear.grid(row=6,column=1,columnspan=2)
button_sum.grid(row=5,column=1,columnspan=2)

root.mainloop()