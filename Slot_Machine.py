import tkinter as tk
import ttkbootstrap as ttk
import random



window = ttk.Window(themename='darkly')
window.geometry('500x650')
    
num1 = tk.IntVar()
num2 = tk.IntVar()
num3 = tk.IntVar()
balance = tk.IntVar(value=500)


def SPIN():
     

    num1.set(random.randint(1,9))
    num2.set(random.randint(1,9))
    num3.set(random.randint(1,9))

    

    if  num1.get() == num2.get() and num1.get() == num3.get():
         postBalance = balance.get() + 800
         balance.set(postBalance)

    elif  num1.get() == num2.get() or num1.get() == num3.get() or num2.get() == num3.get():
         postBalance = balance.get() + 25
         balance.set(postBalance)

    else:
         postBalance = balance.get() - 10 
         balance.set(postBalance)
   






frame = ttk.Frame(master = window)
bframe = ttk.Frame(master = window)

money = ttk.Label(master = bframe, text = 'Balance: 0000', font = 'calibri 20 bold', textvariable = balance)


slot1 = ttk.Label(master = frame, text = '0', font = 'calibri 30 bold', textvariable = num1)


slot2 = ttk.Label(master = frame, text = '0', font = 'calibri 30 bold', textvariable = num2)


slot3 = ttk.Label(master = frame, text = '0', font = 'calibri 30 bold', textvariable = num3)

button = ttk.Button(master = bframe, text = 'Press to Roll', command = SPIN)

frame.grid(row = 0, column = 0 , pady = 100, padx = 200)
bframe.grid(row = 1, column = 0)


slot1.pack(side = 'left', padx = 5)
slot2.pack(side = 'left', padx = 5)
slot3.pack(side = 'left', padx = 5)
button.pack(side = 'bottom', pady = 10)
money.pack(side = 'top')

tk.mainloop()