import math
from scipy.integrate import quad
from scipy.constants import pi
from scipy.optimize import fsolve

# Constants (replace these with actual values)
O = 0.7  # Example value for O
Fe = 0.8  # Example value for Fe
in_value = 2  # Example value for in
M = 0.9  # Example value for M
a2 = 0.2  # Example value for a2
b2 = 0.1  # Example value for b2
a3 = 0.3  # Example value for a3
b3 = 0.25  # Example value for b3
a4 = 0.15  # Example value for a4
b4 = 0.1  # Example value for b4
Pfp = 1.5  # Example value for Pfp
xc = 0.7  # Example value for xc
sigma = 0.05  # Example value for sigma
kr = 0.1  # Example value for kr
Tg = 1000  # Example value for Tg
To = 300  # Example value for To
Dh = 0.01  # Example value for Dh

def integrand(z):
    return pi * Dh * (Tg - To)

def equations(variables):
    a1, a2, a3, a4, b1, b2, b3, b4, n, n1, beta_H, beta_C, HR, HP, HL = variables
    
    # Calculate ΔHR
    ΔHR = ((O / Fe) ** in_value / 3) * ΔHFe2O3 - ((1 - M) / 0.95) * ΔHFe0.925 + n * (a2 - b2) * ΔHH2O + n * (a3 + b3) * ΔHCO + n * (a4 - b4) * ΔHCO2
    
    # Calculate NFe
    NFe = 1000 * Pfp / 56
    
    # Calculate integral for HL
    HL_integral, _ = quad(integrand, 0, 1 / NFe)
    HL = 24 * HL_integral / NFe
    
    # Enthalpy balance equation
    enthalpy_balance = HR - (HF + ΔHR + HP + HL)
    
    eq1 = a1  # a1 >= 0
    eq2 = a2  # a2 >= 0
    eq3 = a3  # a3 >= 0
    eq4 = a4  # a4 >= 0
    eq5 = b1  # b1 >= 0
    eq6 = b2  # b2 >= 0
    eq7 = b3  # b3 >= 0
    eq8 = b4  # b4 >= 0
    eq9 = X - F * (b4 * n + C0 * n1)  # X <= F(b4 * n + C0 * n1)
    eq10 = n - (M * 0.99) / ((a1 - a2 * beta_H) * (1 - beta_H))  # n >= (M * 0.99) / ((a1 - a2 * beta_H) * (1 - beta_H))
    eq11 = math.log(beta_H) - (952 * TR * Z) + 0.514  # log(beta_H) = (952 * TR * Z) - 0.514
    eq12 = math.log(beta_C) - (-941 * TR * Z) + 1.15  # log(beta_C) = (-941 * TR * Z) + 1.15
    eq13 = enthalpy_balance  # Enthalpy balance equation
    
    return [eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8, eq9, eq10, eq11, eq12, eq13]

# Initial guess for the variables
initial_guess = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # You might want to provide better initial guesses based on the problem

# Solve the equations numerically
solution = fsolve(equations, initial_guess)

# Print or use the solution for further analysis
print("Solution:", solution)
