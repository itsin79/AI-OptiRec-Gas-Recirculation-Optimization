from math import log
from scipy.optimize import fsolve

# Constants (replace these with actual values)
TR = 1000  # Example value for TR
TF = 1200  # Example value for TF

def equations(variables):
    a1, a2, a3, a4, b1, b2, b3, b4 = variables
    eq1 = log(a1 * a4 / (a2 * a3)) - 1.66 - 1890 / TR
    eq2 = log(b1 * b4 / (b2 * b3)) + 1.66 - 1890 / TF
    return [eq1, eq2]

# Initial guess for the variables
initial_guess = [1, 1, 1, 1, 1, 1, 1, 1]  # You might want to provide better initial guesses based on the problem

# Solve the equations numerically
solution = fsolve(equations, initial_guess)

# Print or use the solution for further analysis
print("Solution:", solution)
