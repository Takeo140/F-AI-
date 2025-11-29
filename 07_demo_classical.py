"""Demo: symbolic Euler-Lagrange for simple free particle"""
from sympy import symbols, Function
from ftheory.functional import Action

t = symbols('t')
q = Function('q')(t)
# Lagrangian for a free particle (1/2 m qdot^2) with m=1 for simplicity
L = 0.5 * (q.diff(t))**2
A = Action(L, [q], t)
print('Euler-Lagrange eqns:', A.euler_lagrange())
print('Is stationary (symbolically):', A.is_stationary())
