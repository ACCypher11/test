# # For loop
# for i in range(5):
#     print(i)

# for i in range(1, 6):
#     print(i)

# for i in range(0, 10, 2):
#     print(i)

# While Loop
# count = 0
# while count < 5:
#     print(count)
#     count += 1


# # Loop control statement
# for i in range(10):
#     if i == 3:
#         continue
#     if i == 7:
#         break
#     print(i)

# # Nested Loop
# for i in range(2):
#     for j in range(3):
#         print(f"({i},{j})")



# Exercises
# Multiplication Table & Prime Number Generator

def multiplication_table():
    num = int(input("Enter a number to generate its multiplication table: "))
    print(f"\nMultiplication Table of {num}")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")


def prime_numbers():
    limit = int(input("Enter the limit (e.g. 20): "))
    print(f"\nPrime numbers up to {limit}:")
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")
    print()  # new line


# --- Main Menu ---
while True:
    print("\n=== Menu ===")
    print("1. Generate Multiplication Table")
    print("2. Find Prime Numbers up to a Limit")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        multiplication_table()
    elif choice == "2":
        prime_numbers()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
