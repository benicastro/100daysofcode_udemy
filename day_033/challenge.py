"""
Taylor Swift Quotes App by Benedict Z. Castro | benedict.zcastro@gmail.com
"""

# Import needed modules ################################################################################################################
import requests
from tkinter import *

# Declare constant variables ###########################################################################################################
API_ENDPOINT = "https://taylorswiftapi.onrender.com/get"


# Create function
def get_quote():
    """This function obtains a random Taylor Swift quote from the given API."""
    response = requests.get(API_ENDPOINT)
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)



# Setup UI #############################################################################################################################
# Create Window
window = Tk()
window.title("Taylor Says...")
window.config(padx=50, pady=50)

# Create Canvas
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Taylor Swift Quote Goes Here", width=250,
                                font=("Arial", 17, "bold"), fill="white")
canvas.grid(row=0, column=0)

# Create Button
taylor_img = PhotoImage(file="taylor.png")
taylor_button = Button(image=taylor_img, highlightthickness=0, command=get_quote, relief=FLAT)
taylor_button.grid(row=1, column=0)

# Keep window open
window.mainloop()
