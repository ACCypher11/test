student = {
    "name": "Alice",
    "age": 20, 
    "grade": "A",
    "courses": ["Math", "Science", "English"]
}

# # Accessing and modifying
# print(student["name"])
# print(student.get("age"))
# student["age"] = 21
# student["email"] = "alice@gmail.com"

# # print(student)

# keys = student.keys()
# values = student.values()
# items = student.items()

# print(keys)
# print(values)
# print(items)


# # Iterating through dictionaries
# for key in student:
#     print(f"{key}: {student[key]}")

# for key, value in student.items():
#     print(f"{key}: {value}")


# Nested dictionaries
# company = {
#     "employees": {
#         "john": {"age": 30, "department": "IT"},
#         "jane": {"age": 25, "department": "HR"}
#     },
#     "departments": ["IT","HR", "Finance"]
# }

# print(company["employees"].items())
# print(company["departments"])


# Exersice
# 1. Create the dictionary
student_records = {
    "student_001": {
        "name": "John",
        "age": 19,
        "major": "Computer Science",
        "grades": [85, 92, 78]
    },
    "student_002": {
        "name": "Sarah",
        "age": 20,
        "major": "Biology",
        "grades": [90, 88, 95]
    }
}

# 2. Add a new student
student_records["student_003"] = {
    "name": "Mike",
    "age": 18,
    "major": "Math",
    "grades": [82, 79, 91]
}

# 3. Update John's age to 20
student_records["student_001"]["age"] = 20

# 4. Loop through and print info
for student_id, info in student_records.items():
    print(f"Student ID: {student_id}, Name: {info['name']}, Major: {info['major']}")
