from scipy.optimize import fsolve

# Constants (replace these with actual values)
F = 0.5  # Example value for F
O = 0.7  # Example value for [O]
Fe = 0.8  # Example value for [Fe]
in_value = 2  # Example value for in
M = 0.9  # Example value for M
C0 = 0.2  # Example value for C0

def equations(variables):
    b1, b2, b3, b4, n, n1 = variables
    X = (1 - F) * (b3 + b4) * n
    eq1 = X - (1 - F) * (b3 + b4) * n
    eq2 = 2 * X - (b1 + b2) * n + F * b1 * n + F * C0 * n1
    eq3 = (O * Fe) ** in_value - ((1 - M) / 0.95) - n * (b3 + 2 * b4) * (1 - F) - b2 * n + F * C0 * n1
    eq4 = n1 - (1 - b2 / (1 - C0))
    return [eq1, eq2, eq3, eq4]

# Initial guess for the variables
initial_guess = [1, 1, 1, 1, 1, 1]  # You might want to provide better initial guesses based on the problem

# Solve the equations numerically
solution = fsolve(equations, initial_guess)

# Print or use the solution for further analysis
print("Solution:", solution)
