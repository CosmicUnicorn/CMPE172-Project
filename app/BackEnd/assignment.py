class Assignment(Worksheet):
    def __init__(self, title, difficulty, subject, due, delivered, score):
        self.due = due
        self.delivered = delivered
        self.score = score
        super().__init__(title, difficulty, subject)