import tkinter as tk
import ttkbootstrap as ttk
import random
import string

#basic python encrypion program to learn tKinter
baseString = string.ascii_letters + string.punctuation + string.digits + ' '

keyList = list(baseString)
random.shuffle(keyList)

window = ttk.Window(themename='darkly')
window.geometry('500x300')


input = tk.StringVar()
output = tk.StringVar()



def convert():     
    encryptedText = ''
    for char in input.get():
        index = baseString.index(char)
        encryptedText += keyList[index]
        output.set(encryptedText)

def reverse():
     rencryptedText = ''
     for char in input.get():
        index = keyList.index(char)
        rencryptedText += baseString[index]
        output.set(rencryptedText)



resultFrame = ttk.Frame(master = window)
frame = ttk.Frame(master = window)

button = ttk.Button(master = frame, text='Convert', command=convert)
reverseButton = ttk.Button(master=frame, text='reverse', command = reverse)
entry = ttk.Entry(master = frame, text='test', font='calibri 20 bold', textvariable=input)
resultLabel = ttk.Label(master=resultFrame, text='test', font='calibri 40 bold', textvariable=output)

resultFrame.pack()
frame.pack()
button.pack(pady=10)
reverseButton.pack()
entry.pack(pady=10)
resultLabel.pack()


print('input')
               
if  input == 'a':
    print(keyList)

tk.mainloop()