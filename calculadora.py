from tkinter import *

def sumar():
    variable3.set(float(variable1.get()+ float (variable2)))
    limpar()

def limpar():
    variable1.set("")
    variable2.set("")

root = Tk()
root.config(bd=15)
root.config(cursor="heart")

variable1 = StringVar()
variable2 = StringVar()
variable3 = StringVar()

titulo1 = Label(root,text="numero 1")
titulo1.pack()
entrda1= Entry(root,justify="center", textvariable=variable1)

titulo2 = Label(root,text="numero 2")
titulo2.pack()
entrda2= Entry(root,justify="center", textvariable=variable2)

titulo2 = Label(root,text="numero 2")
titulo2.pack()
entrda2= Entry(root,justify="center", textvariable=variable2)

boton =Button(root, text= " sumar", command=sumar)
boton.pack