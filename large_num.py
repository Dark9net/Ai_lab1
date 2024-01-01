from tkinter import *
root=Tk()
root.geometry('300x300')
def largest():
    num = entry.get()
    numbers.extend(num.split(','))
    numbers.sort()
    rel_label.config(text=numbers[-1])


numbers = []

label=Label(root,text="Enter numbers in List")
label.pack()
entry=Entry(root,width=30)
entry.pack()
button=Button(root,text="Find largest",command=largest)
button.pack()
rel_label=Label(root,text="largest Element")
rel_label.pack()
root.mainloop()