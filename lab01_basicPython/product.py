# Take input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculate the product
product = num1 * num2

# Check if the product is greater than 1000
if product > 1000:
    result = num1 + num2  # Return sum if product > 1000
else:
    result = product  # Return product otherwise

# Print the result
print("Result:", result)
