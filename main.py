from tkinter import *
from tkinter.ttk import Entry
from tkinter.ttk import Button
import random

win = Tk()
win.title("Randomize")
win.geometry("500x500")

label1 = Label(win, text="Введите начальное число", font=("Arial Bold", 20))
label1.grid(column=0, row=1)

enter1 = Entry(win, width=70)
enter1.grid(column=0, row=2)

label2 = Label(win, text="Введите конечное число", font=("Arial Bold", 20))
label2.grid(column=0, row=3)

enter2 = Entry(win, width=70)
enter2.grid(column=0, row=4)

def bt():
    num1 = int(enter1.get())
    num2 = int(enter2.get())
    num = random.randint(num1, num2)
    number.configure(text=num)



bt = Button(win, text="Вывести рандомное число", width=70, command=bt)
bt.grid(column=0, row=5)

number = Label(win, text="", font=("Arial Bold", 50))
number.grid(column=0, row=6)

win.mainloop()