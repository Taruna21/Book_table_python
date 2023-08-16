'''
F-strings can contain any valid Python 
expression within the curly braces, making 
them quite versatile and powerful. They are 
often used for string formatting and concatenation,
making the code more readable and maintainable compared 
to older string formatting techniques like % formatting
or .format() method.

'''

name = input("enter the name:")

expression = f"Hello {name} ! I am Jungkook"

print(expression)