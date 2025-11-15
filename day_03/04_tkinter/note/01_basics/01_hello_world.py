import tkinter

root = tkinter.Tk()
root.title("Shirley Sample GUI Application")
root.geometry("1200x400")

label = tkinter.Label(root, text="Good Day")
label.pack()

next_label = tkinter.Label(root, text="Shirley")
next_label.pack()

root.mainloop()
