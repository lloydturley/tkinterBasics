from tkinter import *

def add(*args):
    result=0
    for n in args:
        result+=n
    return result

res = add(2,4,2,4,3,2,4)

window = Tk()
window.title("First GUI")
window.minsize(width=500, height=500)
window.config(padx=100, pady=100)

my_label = Label(text=res, font=("Arial", 24, "bold"))
my_label.grid(column=1, row=1)



def button_click():
    my_label["text"] = input.get().upper()
    #button.config(padx=300, pady=300)

button = Button(text="Push Me", command=button_click)
button.grid(column=2, row=2)

button = Button(text="Push Me", command=button_click)
button.grid(column=3, row=1)

#Entry
input = Entry()
input["width"] = 30
#input.pack(side="left")
#input.place(x=0, y=250)
input.grid(column=4,row=3)


window.mainloop()