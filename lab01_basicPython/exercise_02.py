import math  # Importing math module for pi

# Take input from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate area and perimeter
area = math.pi * radius ** 2  # πr²
perimeter = 2 * math.pi * radius  # 2πr

# Print the results
print(f"Area of the circle: {area:.2f}")
print(f"Perimeter (Circumference) of the circle: {perimeter:.2f}")
