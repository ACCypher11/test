# single_quote = 'Hello'
# double_quote = "World"
# triple_quote = """Multi-line 
# string"""

# print(single_quote)
# print(double_quote)
# print(triple_quote)

# text = "Python Programming"

# print(text[0])
# print(text[-1])
# print(text[0:6])
# print(text[:6])
# print(text[7:])

# name = "bob the builder"

# print(len(name))
# print(name.strip())                 # Length
# print(name.upper())                 # Remove whitespace
# print(name.lower())                 # Uppercase
# print(name.title())                 # Title case
# print(name.replace("bob","jane"))   # Replace

# name = "John Doe"
# age = 30

# message_1 = f"My name is {name} and I am {age} years old."           # f-strings
# message_2 = "My name is {} and I am {} years old.".format(name, age) # str.format()
# message_3 = "My name is %s and I am %d years old." %(name, age)      # %-formatting

# print(message_1)
# print(message_2)
# print(message_3)

# 1. Build a simple text analyzer that counts words, characters, and sentences in a given text.
text = """Python is a powerful programming language. It's easy to learn and versatile!
You can use Python for web development, data science, and automation. The syntax is clean and readable.
This makes Python perfect for beginners and experts alike."""

char_count = len(text)
char_count_no_spaces = len(text.replace(' ', ''))
word_count = len(text.split())
sentence_count = text.count('.') + text.count('!') + text.count('?')

print(f"Character count (including spaces): {char_count}")            # 239
print(f"Character count (excluding spaces): {char_count_no_spaces}")  # 204
print(f"Word count: {word_count}")                                    # 38
print(f"Sentence count: {sentence_count}")                            # 5