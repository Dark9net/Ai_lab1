from tkinter import *
from collections import Counter
root=Tk()
root.geometry('300x300')
def calculate_frequency():
    sentence = entry.get()
    character_frequency = Counter(sentence)
    display_frequency(character_frequency)

def display_frequency(freq_dict):
    result = "\n".join(f"{char}: {count}" for char, count in freq_dict.items())
    rel_label.config(text=result)

label=Label(root,text="Enter a sentence")
label.pack()
entry=Entry(root,width=30)
entry.pack()
button=Button(root,text="Count words",command=calculate_frequency)
button.pack()
rel_label=Label(root,text="Count result")
rel_label.pack()
root.mainloop()