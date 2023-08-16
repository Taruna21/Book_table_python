'''


Dictionary comprehension is a concise and 
expressive way to create dictionaries in 
Python. Similar to list comprehensions, 
dictionary comprehensions allow you to 
create new dictionaries by specifying 
key-value pairs based on an expression 
and optionally filtering those pairs 
based on a condition. This feature 
was introduced in Python 3.

'''
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = {k: v for k, v in zip(keys, values)}
# Result: {'a': 1, 'b': 2, 'c': 3}
