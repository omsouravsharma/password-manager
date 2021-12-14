from tkinter import *
from tkinter import messagebox
from random import random, choice, shuffle, randint
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for i in range(randint(8, 10))]
    symbol_list = [choice(symbols) for i in range(randint(2, 4))]
    number_list = [choice(numbers) for i in range(randint(2, 4))]

    password_list = letter_list + symbol_list + number_list
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'email': email,
            'password': password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Missing Value", message=f"Value is missing")
    else:
        try:
            with open("data.json", "r") as file_object:
                data = json.load(file_object)

        except FileNotFoundError:
            with open("data.json", "w") as file_object:
                json.dump(new_data, file_object, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file_object:
                json.dump(data, file_object, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as file_object:
            data = json.load(file_object)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message="No Data File exit")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['pass word']
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title='Error', message="No Data exit")
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
# window.minsize(width=500, height=400)
window.config(padx=60, pady=60)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Label

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
username_entry = Entry(width=35)
username_entry.insert(0, "sourav.sharma@exxonmobil.com")
username_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=17)
password_entry.grid(row=3, column=1)

# Button
generate_password_button = Button(text="Generate Password", width=14, command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=30, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)
window.mainloop()
