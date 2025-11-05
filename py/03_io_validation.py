# name = input("Enter your name: ")
# height = float(input("Enter your height: "))     # Convert to float

# # Input validation
# while True:
#     try:
#         age = int(input("Enter your age: "))
#         if age > 0:
#             break
#         else:
#             print("Age must be positive!")
#     except ValueError:
#         print("Please enter a valid number!")

# # Output validation
# print(f"Hello, {name}!")
# print(f"You are {age} years old and {height} feet tall.")



# Exercises:
# 1.Create a simple calculator that takes two number and an operation fromuser.
# Simple Calculator

# # Get input from user
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# operation = input("Enter operation (+, -, *, /): ")

# # Perform calculation
# if operation == '+':
#     result = num1 + num2
# elif operation == '-':
#     result = num1 - num2
# elif operation == '*':
#     result = num1 * num2
# elif operation == '/':
#     if num2 != 0:
#         result = num1 / num2
#     else:
#         result = "Error! Division by zero."
# else:
#     result = "Invalid operation."

# # Display result
# print("Result:", result)



# 2.Create  a  simple  quiz  program  with  3  questions.  At  the  end  of  the  quiz,display score.
# Simple Quiz Program

# score = 0

# print("Welcome to the Quiz!\n")

# # Question 1
# answer = input("1. What is the capital of France? ")
# if answer.lower() == "paris":
#     score += 1

# # Question 2
# answer = input("2. What is 5 + 7? ")
# if answer == "12":
#     score += 1

# # Question 3
# answer = input("3. What is the color of the sky on a clear day? ")
# if answer.lower() == "blue":
#     score += 1

# # Display final score
# print("\nYou got", score, "out of 3 questions correct!")


# 2. Create a simple quiz program with 3 questions.
score = 0

# # Question 1
answer1 = input("What is the capital of France? ").lower()
if answer1 == "paris":
    print("Correct!")
    score += 1
    print(score)
else:
    print("Wrong! The answer is Paris.")

# # Question 2
answer2 = input("What is 5 + 3? ")
if answer2 == "8":
    print("Correct!")
    score += 1
    print(score)
else:
    print("Wrong! The answer is 8.")

# # Question 3
answer3 = input("What color do you get when you mix red and blue? ").lower()
if answer3 == "purple":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is purple.")

# Final score
print(f"\nYour final score: {score}/3")
if score == 3:
    print("Perfect score!")
elif score >= 2:
    print("Good job!")
else:
    print("Better luck next time!")