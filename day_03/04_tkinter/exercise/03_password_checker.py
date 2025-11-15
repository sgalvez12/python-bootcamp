import tkinter

root = tkinter.Tk()


label_var = tkinter.StringVar(root, value="Enter your password:")
label = tkinter.Label(root, textvariable=label_var)
label.pack(side="top")

entry_var = tkinter.StringVar(root, value="")
entry = tkinter.Entry(root, textvariable=entry_var,show="*")
entry.pack()

label_var2 = tkinter.StringVar(root, value="Enter your password and press Enter: ")
label2 = tkinter.Label(root, textvariable=label_var2)
label2.pack()



def check_password(event=None):
    correct_password = "pass"
    if entry_var.get() == correct_password:
        label_var2.set("Password correct. Access Granted!")
    else:
        label_var2.set("Incorrect password. Try again!")



button = tkinter.Button(root, text="Submit", command=check_password, fg="red")
button.pack()
root.mainloop()
