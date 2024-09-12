import tkinter as tk
import ttkbootstrap as ttk

screen = ttk.Window()
screen.geometry('500x500')



def press():
    labelInt.set(123)


frame = ttk.Frame(master = screen)
button = ttk.Button(master = screen , text = 'hello', command = press)

labelInt = tk.IntVar()
labelInt.set(234)

label = ttk.Label(master = screen, text = 'hele', textvariable = labelInt)



button.pack()
label.pack()
frame.pack()




tk.mainloop()