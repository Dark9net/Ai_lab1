from tkinter import *
root=Tk()
root.geometry('300x300')
def sum1():
    num = entry.get()
    num_list = num.split(',')
    numbers.extend(map(int, num_list))
    total = sum(numbers)
    rel_label.config(text=total)

numbers = []

label=Label(root,text="Enter numbers in List")
label.pack()
entry=Entry(root,width=30)
entry.pack()
button=Button(root,text="Find Sum",command=sum1)
button.pack()
rel_label=Label(root,text="Total Sum")
rel_label.pack()
root.mainloop()