# # if-else: 2 conditions
# age = 18

# if age >= 18:
#     print("You are an adult.")
# else:
#     print("You are a minor.")

#if-elif-else: more than 2 conditions

# score = 85

# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# elif score >= 60:
#     grade = "D"
# else:
#     grade = "F"

# print(f"Your grade is: {grade}")


# # and: both conditions must be True
# user_age = 25
# has_license = True

# if user_age >= 18 and has_license:
#     print("You are allowed to drive.")
# else:
#     print("You are not allowed to drive.")


# # or: at least one condition must be True
# day = "Saturday"

# if day == "Saturday" or day == "Sunday":
#     print("It's the weekend!")
# else:
#     print("It's a weekday.")


# # Nested conditions: Conditio withi condition
# weather = "sunny"
# temperature = 75
 
# if weather == "sunny":
#     if temperature > 70:
#         print("It's sunny and warm.")
#     else:
#         print("It's sunny but cool.")



### Exercise:
###1.Write  a  program  that  categorizes  BMI  (Body  Mass  Index)  intounderweight(<18.5),  normal  weight(<24.9),  overweight(<29.9),  and obesity(<30.0). (formula = kg/m^2)

# Get user input
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Determine BMI category
if bmi < 18.5:
    category = "Underweight"
elif bmi < 24.9:
    category = "Normal weight"
elif bmi < 29.9:
    category = "Overweight"
else:
    category = "Obesity"

# Display the result
print(f"Your BMI is: {bmi:.2f}")
print(f"You are classified as: {category}")
