from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Transform raw dictionary data into structured Question model instances
question_bank = []
for question in question_data:
    question_text = question["question"]
    answer_text = question["correct_answer"]
    new_question = Question(question_text, answer_text)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

# Drive quiz lifecycle until the question pool is exhausted
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")

