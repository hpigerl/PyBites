class RecordScore:
    """Class to track a game's maximum score"""

    def __init__(self):
        pass

    def __call__(self, score):
        if hasattr(self, "high_score"):
            if score > self.high_score:
                self.high_score = score
        else:
            self.high_score = score
        return self.high_score
