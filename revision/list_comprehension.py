'''

List comprehension is a concise and expressive way to create 
lists in programming languages like Python. It allows you to 
generate new lists by applying an expression to each item in 
an existing iterable (such as a list, tuple, or range) and 
optionally filtering those items based on a condition. List 
comprehensions are favored for their readability and compactness
 when compared to traditional loops for creating lists.

'''

squares = [x ** 2 for x in range(1, 6)]
# Result: [1, 4, 9, 16, 25]
print(squares)



string = "hello world"
uppercase_chars = [char.upper() for char in string if char.isalpha()]
# Result: ['H', 'E', 'L', 'L', 'O', 'W', 'O', 'R', 'L', 'D']
print(uppercase_chars)