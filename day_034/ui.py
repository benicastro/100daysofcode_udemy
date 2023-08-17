"""
QuizInterface Class - This represents the UI of the App
"""

# Import needed modules/libraries ######################################################################################################
from tkinter import *
from quiz_brain import QuizBrain

# Declare constant variables ###########################################################################################################
THEME_COLOR = "#375362"
FONT = ("Arial", 17, "italic")


# Class ################################################################################################################################
class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # Create Window
        self.window = Tk()
        self.window.title("0xAstroc's Quizler")
        self.window.minsize(width=340, height=500)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Create Label
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Create Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Hello, World!",
            width=280,
            font=FONT,
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Create Buttons
        right_button_img = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_button_img)
        self.right_button.config(highlightthickness=0, relief=FLAT, command=self.answered_true)
        self.right_button.grid(row=2, column=0)
        wrong_button_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_button_img)
        self.wrong_button.config(highlightthickness=0, relief=FLAT, command=self.answered_false)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()  # Keep window open

    def get_next_question(self):
        """This function gets the next question from the question_data."""
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def answered_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def answered_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
