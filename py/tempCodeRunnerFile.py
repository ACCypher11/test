# and: both conditions must be True
user_age = 25
has_license = True

if user_age >= 18 and has_license:
    print("You are allowed to drive.")
else:
    print("You are not allowed to drive.")


# or: at least one condition must be True
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
else:
    print("It's a weekday.")