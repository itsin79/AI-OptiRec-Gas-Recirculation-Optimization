from scipy.optimize import fsolve

# Constants (replace these with actual values)
# ... (other constants are assumed to be defined already)
Ai = 0.1  # Example value for Ai
Ei = 50000  # Example value for Ei
R = 8.314  # Universal gas constant, J/(mol·K)
ρg = 0.5  # Example value for ρg
g1 = 0.2  # Example value for g1
g2 = 0.3  # Example value for g2
g3 = 0.25  # Example value for g3
g4 = 0.15  # Example value for g4
KH = 0.05  # Example value for KH

def equations(variables):
    # ... (previous equations remain unchanged)
    ρ1, ρ2, dFi_dt, ki = variables
    
    # New equations from formula 8
    ρ1_calc = ((O / Fe) ** in_value - 1 / 0.95) * Δfb / 56
    ρ2_calc = (Δfb / 56) / 0.95
    dFi_dt_calc = (6 * k1 * (1 - Fi) ** (2/3)) / (ρ1 * d)
    ki_calc = Ai * math.exp(-Ei / (R * T)) * ρg * (g1 + g3 - g2 / KH - g4 / K)
    
    # Enforce the equations
    equation8_1 = ρ1 - ρ1_calc
    equation8_2 = ρ2 - ρ2_calc
    equation8_3 = dFi_dt - dFi_dt_calc
    equation8_4 = ki - ki_calc
    
    # ... (previous equations remain unchanged)
    
    return [eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8, eq9, eq10, eq11, eq12, eq13, equation6, eq14, eq15, equation8_1, equation8_2, equation8_3, equation8_4]

# Initial guess for the variables
initial_guess = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # You might want to provide better initial guesses based on the problem

# Solve the equations numerically
solution = fsolve(equations, initial_guess)

# Print or use the solution for further analysis
print("Solution:", solution)
