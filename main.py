import tkinter

def add(*args):
    result=0
    for n in args:
        result+=n
    return result

res = add(2,4,2,4,3,2,4)

window = tkinter.Tk()
window.title("First GUI")

window.minsize(width=500, height=500)

my_label = tkinter.Label(text=res, font=("Arial", 24, "bold"))
my_label.pack()





window.mainloop()