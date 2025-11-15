import tkinter
import json

root = tkinter.Tk()

name_frame = tkinter.Frame(root)
name_frame.pack()

name = tkinter.Label(name_frame,text="Name")
name.pack(side="left")

name_entry_var = tkinter.StringVar()
name_entry = tkinter.Entry(name_frame, textvariable=name_entry_var)
name_entry.pack(side="right")


age_frame = tkinter.Frame(root)
age_frame.pack()

age= tkinter.Label(age_frame, text="Age")
age.pack(side="left")

age_entry_var = tkinter.StringVar()
age_entry = tkinter.Entry(age_frame, textvariable=age_entry_var)
age_entry.pack(side="right")

# TODO: Create StringVar for theme
# TODO: Create StringVar for theme
theme_var = tkinter.StringVar(value="Preferred Theme:")
theme = tkinter.Label(root, textvariable=theme_var)
theme.pack(side="left")

theme_var = tkinter.StringVar(value="Light")
theme1 = tkinter.Radiobutton(
    root, text="Light", variable=theme_var, value="Light")
theme1.pack()

theme2 = tkinter.Radiobutton(
    root, text="Dark", variable=theme_var, value="Dark")
theme2.pack()

# TODO: Create BooleanVar for subscribe
# TODO: Create BooleanVar for subscribe
subscribe_value = tkinter.BooleanVar()
subscribe_checkbox = tkinter.Checkbutton(
    root,
    text="Subscribe",
    variable=subscribe_value)
subscribe_checkbox.pack()
# TODO: Create IntVar for rating
# TODO: Create IntVar for rating
rating_var = tkinter.StringVar(root, value="Rate us")
rating = tkinter.Label(root, textvariable=rating_var)
rating.pack(side="left")

rating_value = tkinter.IntVar(value=0)
rating = tkinter.Scale(
    root,
    from_=1,
    to=5,
    orient="horizontal",
    variable=rating_value)
rating.pack()
# TODO: Create function for saving values to JSON
# TODO: Create button for submit + save
def save_data(event=None):
    data = {

    }
    with open("data.json", "w") as file:
        json.dump(data, file)

button = tkinter.Button(root, text="Submit", command=save_data)
button.pack()

root.mainloop()
