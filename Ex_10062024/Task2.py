num1 = float(input("Enter the first Number: "))
num2 = float(input("Enter the Second Number: "))

# Compare and print using ternary operator

print(f"{num1} is greater than {num2}" if num1 > num2 else
          f"{num1} is less than {num2}" if num1 < num2 else
          f"{num1} is equal to {num2}")