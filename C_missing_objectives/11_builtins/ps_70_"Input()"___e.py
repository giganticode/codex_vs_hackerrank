"""
You are given a polynomial P of a single indeterminate (or variable), x.
"""

from sympy import Symbol, sympify, solve

x = Symbol('x')

p = input('Enter a polynomial P(x): ')
p = sympify(p)

print(f'All solutions of {p} are: {solve(p)}')