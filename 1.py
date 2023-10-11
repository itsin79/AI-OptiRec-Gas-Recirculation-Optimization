from scipy.optimize import fsolve

# Constants (replace these with actual values)
O = 0.5  # Example value for [O]
Fe = 0.7  # Example value for [Fe]
in_value = 2  # Example value for in
fb = 0.8  # Example value for fb
fp = 0.9  # Example value for fp
n = 1.5  # Example value for n

def equations(variables):
    a1, a2, a3, a4, b1, b2, b3, b4 = variables
    M = 1 - 0.95 * (O * Fe) ** in_value - 3.5 * ((1 - fb) - (1 - fp))
    eq1 = a1 + a2 - b1 - b2
    eq2 = a3 + a4 - b3 - b4
    eq3 = a1 + a2 + a3 - a4 - 10
    eq4 = m * a2 + a4 + (O * Fe) ** in_value - (1 - M / 0.95) - (b1 + b4) * n
    eq5 = M - (1 - 0.95 * (O * Fe) ** in_value - 3.5 * ((1 - fb) - (1 - fp)))
    return [eq1, eq2, eq3, eq4, eq5]

# Initial guess for the variables
initial_guess = [0, 0, 0, 0, 0, 0, 0, 0]

# Solve the equations numerically
solution = fsolve(equations, initial_guess)

# Print or use the solution for further analysis
print("Solution:", solution)
