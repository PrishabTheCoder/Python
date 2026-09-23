# Function to get fibonacci number using recursion
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Get number of terms from user
n_terms = int(input("Enter how many terms: "))

# Check if input is valid
if n_terms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(n_terms):
        print(fibonacci(i))