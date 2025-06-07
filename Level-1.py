# Task-1: String Reversal
def reverse_string(input_str):
    return input_str[::-1]
user_input = input("Enter a string: ")
reversed_output = reverse_string(user_input)
print("Reversed string:", reversed_output)
#Task-2: Temperature Conversion
temperature = float(input("Enter the temperature value: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").strip().upper()
if unit == "C":
    converted = (temperature * 9/5) + 32
    print(f"{temperature}°C is equal to {converted:.2f}°F")
elif unit == "F":
    converted = (temperature - 32) * 5/9
    print(f"{temperature}°F is equal to {converted:.2f}°C")
else:
    print("Invalid unit entered. Please use 'C' for Celsius or 'F' for Fahrenheit.")
# Task-3: Email Validator
def is_valid_email(email):
    if " " in email:
        return False
    if email.count("@") != 1:
        return False

    local_part, domain_part = email.split("@")

    if not local_part or not domain_part:
        return False
    if "." not in domain_part:
        return False
    if domain_part.startswith(".") or domain_part.endswith("."):
        return False

    return True

email = input("Enter an email address: ")
if is_valid_email(email):
    print("Valid email address.")
else:
    print("Invalid email address.")
#Task-4: Calculator Program
num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /, %): ")
num2 = float(input("Enter the second number: "))
if operator == "+":
    result = num1 + num2
    print("Result:", result)
elif operator == "-":
    result = num1 - num2
    print("Result:", result)
elif operator == "*":
    result = num1 * num2
    print("Result:", result)
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")
elif operator == "%":
    if num2 != 0:
        result = num1 % num2
        print("Result:", result)
    else:
        print("Error: Modulus by zero is not allowed.")
else:
    print("Invalid operator.")
# Task-5: Palindrome Checker
def is_palindrome(text):
    # Remove spaces and convert to lowercase
    cleaned_text = text.replace(" ", "").lower()
    # Check if it reads the same backward
    return cleaned_text == cleaned_text[::-1]
user_input = input("Enter a word or phrase: ")
if is_palindrome(user_input):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
