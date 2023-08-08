"""
Pomodoro Application by Benedict Z. Castro | benedict.zcastro@gmail.com
"""
# Import needed modules
from tkinter import *

# Declare constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# Timer Mechanism
def start_timer():
    """This function starts the countdown timer."""
    global reps
    reps += 1  # Add 1 for every instance

    # Convert to seconds
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Conditionals based on reps
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work")


def reset_timer():
    """This function resets the countdown timer."""
    global reps
    reps = 0

    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")


# Countdown Mechanism
def count_down(count):
    """This function acts as a countdown timer in this format: 00:00"""
    count_min = count // 60
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        if reps % 2 == 0:
            work_sessions = reps // 2
            check_label.config(text=work_sessions*"✔️")


# UI SETUP
window = Tk()
window.title("0xAstroc's Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="C:/Users/bened/Desktop/python/udemy_100days/day028/tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Application Properties

timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 43, "bold"))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", relief="flat", font=("Helvetica", 11, "normal"), highlightthickness=0)
start_button.config(command=start_timer)
# flat, groove, raised, ridge, solid, or sunken
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", relief="flat", font=("Helvetica", 11, "normal"), highlightthickness=0)
reset_button.config(command=reset_timer)
reset_button.grid(column=2, row=2)

check_label = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 10, "bold"))
check_label.grid(column=1, row=3)

# Keep the window open
window.mainloop()
