# # Functions with parameters
# def greet_person(name):
#     print(f"Hello, {name}!")
    
# greet_person("Alice")

# # Function with return value
# def add_numbers(a, b):
#     return a + b

# result = add_numbers(5, 3)
# print(result) 

# # Default parameter 
# def greet_with_tile(name, title="Mr."):
#     return f"Hello, {title} {name}!"

# print(greet_with_tile("Smith"))
# print(greet_with_tile("Jahnson", "Dr."))



# # *args - variable number of arguments
# def sum_all(*args):
#     return sum(args)

# print(sum_all(1, 2, 3, 4, 5))


# # **kwargs - keyword arguments
# def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_info(name="Alice", age=25, city="New York")



# # Combining *args and **kwargs
# def flexible_function(*args, **kwargs):
#     print("Positional arguments:", args)
#     print("Keyword arguments:", kwargs)

# flexible_function(1, 2, 3, name="ALice", age=25)


# # Lambda function
# square = lambda x: x**2
# print(square(5))

# add = lambda x, y: x + y
# print(add(3, 4))



# Exiercise
# 1.write afunction that check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# test
print(is_prime(7))   # True
print(is_prime(10))  # False



# 2.Build a temperatur converter function 
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# test
print(celsius_to_fahrenheit(0))     # 32.0
print(celsius_to_fahrenheit(25))    # 77.0
print(celsius_to_fahrenheit(100))   # 212.0
