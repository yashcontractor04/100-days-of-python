from tkinter import simpledialog, Tk
from question_model import Question
from data import get_question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# Create a temporary hidden root window to host standard prompt dialogs
prompt_root = Tk()
prompt_root.withdraw()

# Ask for question count (default 10, bounds 1 to 50)
q_amount = simpledialog.askinteger(
    title="Quiz Configuration",
    prompt="How many questions would you like? (1-50):",
    initialvalue=10,
    minvalue=1,
    maxvalue=50,
) or 10

# Ask for category (default 'science')
q_category = simpledialog.askstring(
    title="Quiz Category",
    prompt="Choose a category ('science' or 'general'):",
    initialvalue="science",
) or "science"

prompt_root.destroy()

# Fetch questions dynamically based on user selections
raw_questions = get_question_data(amount=q_amount, category_name=q_category)

question_bank = [
    Question(q["question"], q["correct_answer"]) for q in raw_questions
]

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
