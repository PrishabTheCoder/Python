def is_armstrong(num):
    num_str = str(num)
    power = len(num_str)
    total = sum(int(digit) ** power for digit in num_str)
    return total == num

user_input = input("Enter a whole number to check: ")

try:
    number = int(user_input)
    
    if is_armstrong(number):
        print(f"Yes! {number} is an Armstrong number.")
    else:
        print(f"No. {number} is not an Armstrong number.")

except ValueError:
    print("Invalid input. Please enter a valid whole number.")
