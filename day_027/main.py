"""
Miles to Kilometers Converter Project by Benedict Z. Castro | benedict.zcastro@gmail.com
"""

# Import needed module(s)
from tkinter import *

# Declare constants/global variables
FONT = ("Arial", 11, "normal")


def main():

    def convert():
        """Converts the given miles value to kilometers."""
        mi_input = float(user_input.get())
        print(type(mi_input))
        km = mi_input * 1.609
        ans_label.config(text=f"{km}")

    # Configure window
    window = Tk()
    window.title("0xAstroc's Miles to Kilometers Converter")
    # window.minsize(width=450, height=150)
    window.config(padx=20, pady=20)

    # Create Label objects
    mi_label = Label(text="Miles", font=FONT)
    km_label = Label(text="Kilometers", font=FONT)
    eq_label = Label(text="is equal to", font=FONT)
    ans_label = Label(text="0", font=FONT)

    # Create a Button object
    button = Button(text="Calculate", command=convert)

    # Create an Entry object
    user_input = Entry(width=5)

    # Arrange widgets in the window
    user_input.grid(column=1, row=0)
    mi_label.grid(column=2, row=0)
    eq_label.grid(column=0, row=1)
    ans_label.grid(column=1, row=1)
    km_label.grid(column=2, row=1)
    button.grid(column=1, row=2)

    # Keep window open
    window.mainloop()


# Run the program
if __name__ == "__main__":
    main()
