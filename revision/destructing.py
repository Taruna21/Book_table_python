
'''Destructuring, also known as unpacking,
 is a feature in Python that allows you to 
 assign the elements of an iterable (like a 
 list, tuple, or other sequence) to multiple
   variables in a single statement. It's a 
   convenient way to extract and assign values 
   from iterables without having to write 
   multiple assignment statements.

Python supports destructuring in various contexts, such as assignment, function parameter passing, and even in loops.
'''

# Unpacking a tuple
coordinates = (3, 4)
x, y = coordinates
print(x)  # Output: 3
print(y)  # Output: 4

# Unpacking a list
values = [10, 20, 30]
first, second, third = values
print(first)   # Output: 10
print(second)  # Output: 20
print(third)   # Output: 30



a = 5
b = 10
a, b = b, a  # Swap values of a and b
print(a)  # Output: 10
print(b)  # Output: 5

# Unpacking in a loop
coordinates_list = [(1, 2), (3, 4), (5, 6)]
for x, y in coordinates_list:
    print(f"x: {x}, y: {y}")
# Output:
# x: 1, y: 2
# x: 3, y: 4
# x: 5, y: 6
