"""
Password Manager by Benedict Z. Castro | benedict.zcastro@gmail.com
"""

# Import needed modules
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# Declare constants
FONT_NAME = "Arial"


# Build program functions
def generate_pw():
    """This function generates a random string based on user-defined conditions as a password."""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
               'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
               'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pw_list = [random.choice(letters) for _ in range(random.randint(8, 10))] + \
              [random.choice(numbers) for _ in range(random.randint(2, 4))] + \
              [random.choice(symbols) for _ in range(random.randint(2, 4))]
    random.shuffle(pw_list)
    pw_str = "".join(pw_list)

    # Insert password
    if pw_entry.get():
        pw_entry.delete(0, END)
    pw_entry.insert(0, pw_str)
    pyperclip.copy(pw_str)


def add_pw():
    """This function gets the user inputs or entries and then save to a file."""
    # Get entries
    website_input = website_entry.get()
    email_input = email_entry.get()
    pw_input = pw_entry.get()
    new_data = {
        website_input.title(): {
            "Email": email_input,
            "Password": pw_input,
        }
    }

    # Create a messagebox and save data
    if website_input and email_input and pw_input:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                data.update(new_data)
                json.dump(data, data_file, indent=4)
        finally:
            # Delete entered data from entries
            website_entry.delete(0, END)
            pw_entry.delete(0, END)
    else:
        messagebox.showwarning(title="Warning!", message="Please don't leave any field empty.")


def find_pw():
    """This function searches the JSON file for the password details for a given site. The details are displayed in a message box."""
    website_input = website_entry.get().title()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            email = data[website_input]["Email"]
            password = data[website_input]["Password"]
    except (KeyError, FileNotFoundError):
        messagebox.showwarning(title="Oops!", message=f"There are no saved details for {website_input}. Please provide a valid one.")
    else:
        messagebox.showinfo(title=f"Password Details for {website_input}",
                            message=f"Email: {email} \nPassword: {password}")


# UI Setup
window = Tk()
window.title("0xAstroc's Password Manager")
window.minsize(height=450, width=550)
window.maxsize(height=450, width=550)
window.config(padx=50, pady=50)

# Create Canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.pack()

# Create Labels
website_label = Label(text="Website:")
website_label.place(x=0, y=200)
email_label = Label(text="Email/Username:")
email_label.place(x=0, y=235)
pw_label = Label(text="Password:")
pw_label.place(x=0, y=270)

# Create Entries
website_entry = Entry(width=25)
website_entry.focus()
website_entry.place(x=125, y=200)
email_entry = Entry(width=45)
email_entry.insert(0, "benedict.zcastro@gmail.com")
email_entry.place(x=125, y=235)
pw_entry = Entry(width=25)
pw_entry.place(x=125, y=270)

# Create Buttons
search_button = Button(text="Search", width=16, relief=RIDGE, command=find_pw)
search_button.place(x=320, y=195)
generate_button = Button(text="Generate Password", width=16, relief=RIDGE, command=generate_pw)
generate_button.place(x=320, y=265)
add_button = Button(text="Add", width=45, relief=RIDGE, command=add_pw)
add_button.place(x=125, y=305)

# Keep screen open
window.mainloop()
