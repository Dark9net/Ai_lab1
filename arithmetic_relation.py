from tkinter import *
root=Tk()
root.geometry('300x300')
def arithmetic_rel():
    num1=int(entry1.get())
    num2=int(entry2.get())
    sym=entry3.get()
    if sym == '+':
        result = num1 + num2
        result_label.config(text=result)
    elif sym == '-':
        result = num1 - num2
        result_label.config(text=result)
    elif sym == '*':
        result = num1 * num2
        result_label.config(text=result)
    elif sym == '/':
        result = num1 / num2
        result_label.config(text=result)
    else:
        result_label.config(text="you entered incorrect symbol")

text_label=Label(root,text="Enter Number1")
text_label.pack(anchor="center")

entry1=Entry(root,text="Number 1",width=30)
entry1.pack()
text_label2=Label(root,text="Enter Number2")
text_label2.pack(anchor="center")
entry2=Entry(root,text="Number 2",width=30)
entry2.pack()
text_label3=Label(root,text="Enter Symbol")
text_label3.pack(anchor="center")
entry3=Entry(root,text="Symbol",width=30)
entry3.pack()
check_button=Button(root,command=arithmetic_rel,text="Check",width=30)
check_button.pack(anchor="center")
result_label=Label(root,text="Result")
result_label.pack(anchor="center")
root.mainloop()