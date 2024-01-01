from tkinter import *
root=Tk()
root.geometry('200x200')
def division():
    percent=int(entry.get())
    if (percent >= 80):
        result_label.config(text="You got Distinction")
    elif 65 <= percent < 80:
        result_label.config(text="You got First Division")
    elif 55 <= percent < 65:
        result_label.config(text="You got Second division")
    elif 40 <= percent < 55:
        result_label.config(text="You got Third division")
    else:
        result_label.config(text="Sorry, You Failed")

text_label=Label(root,text="Enter the percentage")
text_label.pack(anchor="center")

entry=Entry(root,text="Percentage",width=30)
entry.pack()
check_button=Button(root,command=division,text="Check",width=30)
check_button.pack(anchor="center")
result_label=Label(root,text="Result")
result_label.pack(anchor="center")
root.mainloop()