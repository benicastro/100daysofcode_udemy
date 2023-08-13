"""
Flash Card App by Benedict Z. Castro | benedict.zcastro@gmail.com
"""

# Import needed modules
import pandas as pd
import random
from tkinter import *


# Declare constant variables
BACKGROUND_COLOR = "#B1DDC6"

# Create variable for the current card
current_card = {}
words_to_learn = {}

# Export data from csv file
try:
    words_data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    orig_data = pd.read_csv("data/french_words.csv")
    words_to_learn = orig_data.to_dict(orient="records")
else:
    words_to_learn = words_data.to_dict(orient="records")


# Define Functions for the App
def create_card():
    """ This function creates a new content for the flash card with a random data from the csv file."""
    global words_to_learn, current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_to_learn)
    canvas.itemconfig(card_background, image=bg_image_front)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    """This function shows the English translation of the word in the current flash card."""
    global current_card
    canvas.itemconfig(card_background, image=bg_image_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def is_known():
    """This function removes the card from the current dictionary of words to learn."""
    words_to_learn.remove(current_card)
    data = pd.DataFrame(words_to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    create_card()


# Setup UI #############################################################################################################################
window = Tk()
window.title("0xAstroc's Flash Card App")
window.minsize(width=800, height=526)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# Create Canvas
canvas = Canvas(width=800, height=526)
bg_image_front = PhotoImage(file="images/card_front.png")
bg_image_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=bg_image_front)
card_title = canvas.create_text(400, 90, font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Create Buttons
cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_image)
cross_button.config(bg=BACKGROUND_COLOR, highlightthickness=0, relief=FLAT, command=create_card)
cross_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image)
check_button.config(bg=BACKGROUND_COLOR, highlightthickness=0, relief=FLAT, command=is_known)
check_button.grid(row=1, column=1)

# Main App Loop ########################################################################################################################
# Initialize app with first word
create_card()

# Keep window open
window.mainloop()
