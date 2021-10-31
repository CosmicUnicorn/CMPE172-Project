from .worksheet import Worksheet
class Assignment(Worksheet):
    def __init__(self, title, difficulty, subject, due, delivered, score):
        self.id = None
        self.due = due
        self.delivered = delivered
        self.score = score
        super().__init__(title, difficulty, subject)