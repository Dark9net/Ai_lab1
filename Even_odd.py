from tkinter import *
root=Tk()
root.geometry('200x200')
def even_or_odd():
    num=int(input_num.get())
    if (num % 2 == 0):
        label.config(text="The number is even")
    else:
        label.config(text="The number is odd")
text_label=Label(root,text="Enter the number to check Either it is Even or Odd")
text_label.pack()
input_num=Entry(root,text="Enter the number",width=60)
input_num.pack()
check_button = Button(root,command=even_or_odd,text="CHECK")
check_button.pack()
label=Label(root,text="result")
label.pack()

root.mainloop()