import numpy as np

class QuantumAction:
    def __init__(self, action, hbar=1.0):
        self.action = action
        self.hbar = hbar

    def path_integral(self, paths):
        """Compute a discrete approximation of the path integral over a given list of 'paths'.
        Each path must implement evaluate_action(action) -> numeric.
        This is intentionally small and illustrative, not production QFT code.
        """
        weights = []
        for psi in paths:
            S_val = psi.evaluate_action(self.action)
            weights.append(np.exp(1j * S_val / self.hbar))
        return sum(weights)
