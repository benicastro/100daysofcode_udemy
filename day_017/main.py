"""
The Quiz Game by Benedict Castro | benedict.zcastro@gmail.com
"""

# Import needed modules
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random


def main():
    """
    The Quiz Game
    by Benedict Castro | benedict.zcastro@gmail.com
    """

    play_again = True
    while play_again:  # Main program loop

        # Create a question bank to store all the question objects for the game
        question_bank = []
        # random.shuffle(question_data)
        for item in question_data:
            question_bank.append(Question(item["text"], item["answer"]))

        # Create an instance of the QuizBrain class
        quiz_master = QuizBrain(question_bank)

        while quiz_master.still_has_questions():  # Continue game as long as there are still questions available
            # Ask the user a question
            quiz_master.next_question()

        print("You've completed the quiz.")
        print(f"Your final score was: {quiz_master.score}/{quiz_master.question_number}")

        # Ask user if they want to try again
        if input("Do you want to try the quiz again? (Yes | No): ").lower() != "yes":
            print("\n")
            play_again = False


# If the program is run (instead of imported), run the program
if __name__ == "__main__":
    main()
