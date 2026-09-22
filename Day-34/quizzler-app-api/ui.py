from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    """Desktop GUI interface for quizzler using Tkinter and Canvas text layout."""
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.question = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.question.create_text(150, 125, width=270, text="Some Question Text", fill=THEME_COLOR, font=("Arial", 14, "italic"))
        self.question.grid(row=1, column=0, columnspan=2, pady=30)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, bg=THEME_COLOR, fg=THEME_COLOR, highlightthickness=0, border=0, command=self.pressed_true)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, bg=THEME_COLOR, fg=THEME_COLOR, highlightthickness=0, border=0, command=self.pressed_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        """Resets canvas background, re-enables buttons, and draws the next question."""
        self.question.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.question.itemconfig(self.question_text, text=q_text)
        else:
            self.question.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def pressed_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def pressed_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        """Briefly changes canvas color to indicate correctness and throttles multi-clicks."""
        if is_right:
            self.question.config(bg="green")
        else:
            self.question.config(bg="red")
        self.window.after(1000, self.get_next_question)