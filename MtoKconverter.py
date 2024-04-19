from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=100, pady=100)

entry = Entry(width=5)
# Add some text to begin with
entry.insert(END, string="0")
entry.grid(column=2, row=1)

label1 = Label(text="Miles")
label1.grid(column=3, row=1)

label2 = Label(text="is equal to")
label2.grid(column=1, row=2)

label3 = Label(text="0")
label3.grid(column=2, row=2)

label4 = Label(text="Km")
label4.grid(column=3, row=2)


def do():
    #print("You clicked the button")
    label3["text"] = float(entry.get())*1.609


button = Button(command=do)
button["text"] = "Calculate"
button.grid(column=2, row=3)

window.mainloop()
