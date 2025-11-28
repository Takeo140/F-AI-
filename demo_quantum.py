"""Demo: simple discrete path integral approximation (illustrative)"""
from ftheory.quantum import QuantumAction

class DummyPath:
    def __init__(self, val):
        self.val = val
    def evaluate_action(self, action):
        # trivial placeholder numeric evaluation
        return float(self.val)

# dummy action placeholder
action = object()
QA = QuantumAction(action, hbar=1.0)
paths = [DummyPath(v) for v in [0.0, 1.0, -1.0]]
print('Discrete path integral (sum of weights):', QA.path_integral(paths))
