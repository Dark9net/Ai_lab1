from tkinter import *
root=Tk()
root.geometry('300x300')

def update_dictionary():
    input_values = key_entry.get()
    separation = input_values.split(',')
    for pair in separation:
        key, value = pair.split(':') if ':' in pair else (pair, None)
        if key.strip():
            my_dict[key.strip()] = value.strip() if value else None
    calculate_total()

def calculate_total():
    net_value = sum(my_dict.values())
    rel_label.config(text=f"Total: {net_value}")

my_dict = {}
label=Label(root,text="Enter Key:value separated by comma")
label.pack()
key_entry=Entry(root,width=30)
key_entry.pack()

button=Button(root,text="Count words",command=update_dictionary)
button.pack()
rel_label=Label(root,text="Count result")
rel_label.pack()
root.mainloop()