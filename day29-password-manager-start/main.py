from tkinter import *
from tkinter import messagebox
from password import Password
import pyperclip
import json
import os

# ---------------------------- SEARCH ------------------------------- #
def search():
    with open("data.json", 'r') as data_file:
        data = json.load(data_file)
        try:
            d = data[web.get()]
            messagebox.showinfo(title=f"{web.get()}", message=f'mail: {d["mail"]}\npassword: {d["password"]}')
        except:
            messagebox.showerror(title=web.get(), message="Password is not yet saved for this website. Create a new one.")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    if web.get()=="":
        messagebox.showerror(title="Oops!!!", message="Please don't leave any fields empty.")
    else:
        gen = Password()
        pw.insert(0, gen.password)
        pyperclip.copy(gen.password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_data = {
        web.get():
            {
                "mail": mail.get(),
                "password": pw.get(),
            }
    }
    if pw.get() == "" or web.get() == "":
        messagebox.showerror(title="Oops!!!", message="Please don't leave any fields empty.")

    else:
        isOk = messagebox.askokcancel(title=web.get(),
                                      message=f"These are the details entered: \n{mail.get()}\n{pw.get()}\nIs it Ok to save?")
        if isOk:
            try:
                with open("data.json", 'r') as data_file:
                    try:
                        data = json.load(data_file)
                    except:
                        data_file.close()
                        os.remove("data.json")
                        with open("data.json", 'w') as data_file:
                            json.dump(new_data, data_file, indent=4)
            except FileNotFoundError:
                with open("data.json", 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                web.delete(0, END)
                pw.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

screen = Tk()
screen.config(padx=40, pady=40)
screen.title("Password Manager")
canvas = Canvas(height=200, width=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# Website label
website = Label(text="Website:")
website.grid(column=0, row=1)
web = Entry(width=32)
web.focus()
web.grid(column=1, row=1)

# search button
search = Button(text="Search", width=15, command=search)
search.grid(column=2, row=1)

# email label
email = Label(text="Email/Username:")
email.grid(column=0, row=2)
mail = Entry(width=50)
mail.insert(0, "hvandrangi@gmail.com")
mail.grid(column=1, row=2, columnspan=2)

# password label
password = Label(text="Password:")
password.grid(column=0, row=3)
pw = Entry(width=32)
pw.grid(column=1, row=3)

# Generate password button
gp = Button(text="Generate Password", command=generate)
gp.grid(column=2, row=3)

# Add Button
add = Button(text="Add", width=42, command=save)
add.grid(column=1, row=4, columnspan=3)

screen.mainloop()
