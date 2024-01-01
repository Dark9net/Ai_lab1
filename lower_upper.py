from tkinter import *
root=Tk()
root.geometry('300x300')
def convert():
    sentence1 = entry.get()
    sent_ref = ""
    for char in sentence1:
        if char.islower():
            sent_ref += char.upper()
        elif char.isupper():
            sent_ref += char.lower()
        else:
            sent_ref += char
    label_rel.config(text=sent_ref)

label=Label(root,text="Sentence to Swap alphabets")
label.pack()
entry=Entry(root,width=30)
entry.pack()
button=Button(root,text="Swap",command=convert)
button.pack()
label_rel=Label(root,text="Result")
label_rel.pack()
root.mainloop()