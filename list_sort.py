from tkinter import *
root=Tk()
root.geometry('300x300')
def sort():
    num = entry.get()
    numbers.extend(num.split(','))
    numbers.sort()
    insert()
def insert():
    rel_label.config(text=numbers)

numbers = []

label=Label(root,text="Enter numbers in List")
label.pack()
entry=Entry(root,width=30)
entry.pack()
button=Button(root,text="Sort numbers",command=sort)
button.pack()
rel_label=Label(root,text="Sorted List")
rel_label.pack()
root.mainloop()