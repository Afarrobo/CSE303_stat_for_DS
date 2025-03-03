# series in python 

# Read a positive integer N from the user
N = int(input("Enter a positive integer N: "))

# Initialize the sum
sum_of_squares = 0

# Calculate the sum of squares from 1 to N
for i in range(1, N + 1):
    sum_of_squares += i ** 2

# Print the result
print("The sum of squares from 1 to", N, "is:", sum_of_squares)
