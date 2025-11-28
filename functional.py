# Minimal symbolic Lagrangian / Action utilities using sympy
import sympy as sp

class Action:
    def __init__(self, L, coords, t):
        self.L = sp.sympify(L)
        self.coords = coords
        self.t = t

    def euler_lagrange(self):
        # For each coordinate q(t), compute Euler-Lagrange equation
        eqs = []
        for q in self.coords:
            qdot = sp.diff(q, self.t)
            dL_dq = sp.diff(self.L, q)
            dL_dqdot = sp.diff(self.L, qdot)
            ddt = sp.diff(dL_dqdot, self.t)
            eqs.append(sp.simplify(ddt - dL_dq))
        return eqs

    def is_stationary(self):
        eqs = self.euler_lagrange()
        # Stationary if all Euler-Lagrange eqs simplify to 0 symbolically
        return all(sp.simplify(e) == 0 for e in eqs)
