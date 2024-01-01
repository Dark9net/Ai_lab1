from tkinter import *
root=Tk()
root.geometry('300x300')

def factorial():
    num = int(entry.get())
    fact = 1
    for i in range(1,num+1):
        fact *= i
    disp_label.config(text=fact)

label = Label(root, text="Enter Number to find factorial")
label.pack()
entry = Entry(root)
entry.pack()
button = Button(root, command=factorial, text="Calculate")
button.pack()
disp_label = Label(root, text="Results")
disp_label.pack()
root.mainloop()