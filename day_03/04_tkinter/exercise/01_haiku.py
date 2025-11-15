import tkinter


root = tkinter.Tk()
root.title("Shirley Sample GUI Application")
root.geometry("1200x400")


message = """
Loops within loops again
A silent function returns
The logic is clear
"""

label = tkinter.Label(root, text=message)
label.pack()

root.mainloop()

# TODO: Show message using a label
