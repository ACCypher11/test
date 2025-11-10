# # Sets operations
# fruits = {"apple", "banana", "orange"}
# numbers = {1, 2, 3, 4, 5}

# fruits.add("grape")
# fruits.remove("banana")
# fruits.discard("kiwi")

# print(fruits)

# # Sets mathematic operations
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.difference(set2))


# Exercise
grades= [
    ("Alice", "Math", 85),
    ("Bob", "Science", 92),
    ("Alice", "Science", 78),
    ("Charlie", "Math", 90),
    ("Bob", "Math", 88),
    ("Alice", "English", 95),
]

# Use sets to find unique students and subjects
students = {record[0] for record in grades}
subjects = {record[1] for record in grades}

# Display results
print("Unique Students:", students)
print("Unique Subjects:", subjects)

# Optional: Display all grades nicely
print("\nAll Grades:")
for name, subject, grade in grades:
    print(f"{name} - {subject}: {grade}")