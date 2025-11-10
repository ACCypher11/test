# # Lists

# fruits = ["apple", "banana", "orange"]
# numbers = [1, 2, 3, 4, 5]
# mixed = ["hello", 42, 3.14, True]
# empty_list = []

# # Accessing Elements
# print(fruits[0])
# print(fruits[-1])
# print(numbers[1:4])
# print(numbers[:3])
# print(numbers[2:])

# fruits.append("grape")
# fruits.insert(1, "kiwi")
# fruits.remove("banana")
# popped = fruits.pop()
# fruits.sort()
# fruits.reverse()

# # List operations
# len(fruits)
# "apple" in fruits
# fruits + ["mango"]
# fruits * 2

# print(len(fruits))


# Exercises

# Grocery List & Find Largest/Smallest Number Program

def grocery_list_operations():
    grocery_list = []

    while True:
        print("\n=== Grocery List Menu ===")
        print("1. Add item")
        print("2. Remove item")
        print("3. View list")
        print("4. Clear list")
        print("5. Exit to main menu")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            item = input("Enter item to add: ")
            grocery_list.append(item)
            print(f"{item} added to the list.")
        elif choice == "2":
            item = input("Enter item to remove: ")
            if item in grocery_list:
                grocery_list.remove(item)
                print(f"{item} removed from the list.")
            else:
                print("Item not found in the list.")
        elif choice == "3":
            print("\nYour Grocery List:")
            if grocery_list:
                for i, item in enumerate(grocery_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("(Empty list)")
        elif choice == "4":
            grocery_list.clear()
            print("List cleared.")
        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")


def find_largest_and_smallest():
    numbers = []
    print("\nEnter numbers (type 'done' to finish):")
    
    while True:
        value = input("> ")
        if value.lower() == 'done':
            break
        try:
            numbers.append(float(value))
        except ValueError:
            print("Please enter a valid number.")

    if numbers:
        largest = max(numbers)
        smallest = min(numbers)
        print(f"\nNumbers entered: {numbers}")
        print(f"Largest number: {largest}")
        print(f"Smallest number: {smallest}")
    else:
        print("No numbers entered.")


# --- Main Menu ---
while True:
    print("\n=== Main Menu ===")
    print("1. Grocery List Operations")
    print("2. Find Largest and Smallest Number in a List")
    print("3. Exit")

    main_choice = input("Enter your choice (1-3): ")

    if main_choice == "1":
        grocery_list_operations()
    elif main_choice == "2":
        find_largest_and_smallest()
    elif main_choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
