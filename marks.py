from tkinter import *
root=Tk()
root.geometry('300x300')

def display():
    disp=entry.get()
    disp_label.config(text=disp)
label=Label(root,text="Enter marks")
label.pack()
entry=Entry(root)
entry.pack()
button=Button(root,command=display,text="Display Data")
button.pack()
disp_label=Label(root,text="Results")
disp_label.pack()
root.mainloop()