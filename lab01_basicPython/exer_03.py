# Write a Python program to calculate the compound interest based on the given formula. Read inputs
# from the user.
# A = P * (1 + R/100)

# T where P is the principle amount, R is the interest rate and T is time (in years).
# Define a function named as compound_interest_<your-student-id> in your program.

# ######## Answer ###############


def comp_interest_2022_1_60_113(p , r , t):
    A = p * (1 + r / 100) ** t
    return A


p = float(input("enter your principle amount : "))
r = float(input("enter your interest rate : "))
t = float(input("enter your time (in years) :"))

result = comp_interest_2022_1_60_113(p , r , t)

print(f"final amout after {t} years = {result:.2f}")
