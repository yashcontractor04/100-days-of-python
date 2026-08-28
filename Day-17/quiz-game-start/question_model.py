class Question:
    """Domain model representing an individual trivia question."""
    def __init__(self, question, answer):
        self.text = question
        self.answer = answer