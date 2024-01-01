from tkinter import *
root=Tk()
root.geometry('300x300')
def sentence():
    sent = str(entry.get())
    count = len(sent.split())
    rel_label.config(text=count)

label=Label(root,text="Enter a sentence")
label.pack()
entry=Entry(root,width=30)
entry.pack()
button=Button(root,text="Count words",command=sentence)
button.pack()
rel_label=Label(root,text="Count result")
rel_label.pack()
root.mainloop()