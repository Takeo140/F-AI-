class Law:
    def __init__(self, expression):
        self.expression = expression

    def is_consistent(self):
        # Placeholder: in a fuller system this would run SAT/SMT or theorem prover checks.
        return self.expression is not None
