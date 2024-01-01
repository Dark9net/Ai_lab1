from tkinter import *
import math
root=Tk()
root.geometry('300x300')

def prime():
    results = ""
    for i in range(2,100):
        num = math.ceil(i/2)
        p_flag = True
        for j in (2,num):
            if i % j == 0:
                p_flag = False
                break
        if p_flag:
            results += str(i) + ","
    results_label.config(text=results)

results_label=Label(root,text="Results")
results_label.pack(anchor="center")
button=Button(root,command=prime,text="Check prime form 1-100")
button.pack()
root.mainloop()