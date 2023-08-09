"""
Password Manager by Benedict Z. Castro | benedict.zcastro@gmail.com
"""

# Import needed modules
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

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

    # Create a messagebox

    if website_input and email_input and pw_input:
        is_ok = messagebox.askokcancel(title=website_input,
                                       message=f"These are the details you've entered: \n\nEmail: {email_input} "
                                               f"\nPassword: {pw_input} \n\nDo you want to save?")
        # Save data to a file
        if is_ok:
            with open(file="data.txt", mode="a") as file:
                file.write(f"{website_input} | {email_input} | {pw_input}\n")

            # Delete entered data from entries
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            pw_entry.delete(0, END)
    else:
        messagebox.showwarning(title="Warning!", message="Please don't leave any field empty.")


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
website_entry = Entry(width=45)
website_entry.focus()
website_entry.place(x=125, y=200)
email_entry = Entry(width=45)
email_entry.insert(0, "benedict.zcastro@gmail.com")
email_entry.place(x=125, y=235)
pw_entry = Entry(width=25)
pw_entry.place(x=125, y=270)

# Create Buttons
generate_button = Button(text="Generate Password", relief=RIDGE, command=generate_pw)
generate_button.place(x=320, y=265)
add_button = Button(text="Add", width=45, relief=RIDGE, command=add_pw)
add_button.place(x=125, y=305)

# Keep screen open
window.mainloop()
