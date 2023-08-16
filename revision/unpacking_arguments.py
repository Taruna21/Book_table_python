'''


Unpacking arguments, often referred to as
 "argument unpacking" or "splatting," is a
   feature in Python that allows you to pass
     elements from an iterable (like a list,
       tuple, or other sequence) as individual
         arguments to a function.
 This is particularly useful when you 
 want to call a function with multiple 
 arguments stored in a collection.

'''

def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = add(*numbers)
print(result)  # Output: 6

def string(name , age):
    value = f"Name : {name}, Age : {age}"
    return value
person = {"name": "Alice", "age": 30}
print(string(**person))

def create_string(name, age):
    value = f"Name: {name}, Age: {age}"
    return value

# Prompt the user for input
name = input("Enter name: ")
age = int(input("Enter age: "))

# Create a dictionary using the input values
person = {"name": name, "age": age}

# Call the function with the input dictionary
result = create_string(**person)
print(result)

