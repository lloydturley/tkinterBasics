import tkinter

window = tkinter.Tk()
window.title("First GUI")
window.minsize(width=500, height=500)

my_label = tkinter.Label(text="Label 1", font=("Arial", 24, "bold"))
my_label.pack()




window.mainloop()