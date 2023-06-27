# Create a class to manage all the quiz game functions
class QuizBrain:

    def __init__(self, questions_list):
        self.score = 0
        self.question_number = 0
        self.questions_list = questions_list

    def still_has_questions(self):
        """This function tells if there are still questions and returns a boolean."""
        return self.question_number < len(self.questions_list)

    def next_question(self):
        """This function pulls up a question from the questions list."""
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True | False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, current_user_answer, current_question_answer):
        """This function checks whether the user's answer is right or wrong. It returns a boolean value."""
        if current_user_answer.lower() == current_question_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The current answer was: {current_question_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")


# Checking if the answer was correct
# checking if we're at the end of the quiz
