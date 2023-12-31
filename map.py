from collections import deque

def add(a, b):
    return a + b

odds = [1, 3, 5, 7, 9]
evens = [2, 4, 6, 8, 10]

totals = map(add, odds, evens)
print(*totals, sep=", ")  # 3, 7, 11, 15, 19

def cube(number):
    return number ** 3

numbers = [1, 2, 3, 4, 5]
cubed_numbers = map(cube, numbers)

print(*cubed_numbers, sep=", ")


def cube(number):
    return number ** 3

numbers = [1, 2, 3, 4, 5]
cubed_numbers = map(cube, numbers)

print(*cubed_numbers)


def cube(number):
    return number ** 3

numbers = [1, 2, 3, 4, 5]
cubed_numbers = list(map(cube, numbers))
print(*cubed_numbers)
print(cubed_numbers)

numbers = [1, 2, 3, 4, 5]
cubed_numbers = map(lambda number: number ** 3, numbers)

print(*cubed_numbers)

def multigreet(*args):
    for name in args:
        print(f"Hello, {name}!")

multigreet("Rolf", "Bob", "Anne")

def multigreet(*names):
    for name in names:
        print(f"Hello, {name}!")



multigreet("Jose", "Phil")

def pretty_print(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

pretty_print(title="The Matrix", director="Wachowski", year=1999)

# title: The Matrix
# director: Wachowski
# year: 1999

def print_movie(*args):
    for value in args:
        print(value)

movie = {
    "title": "The Matrix",
    "director": "Wachowski",
    "year": 1999
}

print_movie(*movie.values())
print_movie(*movie.keys())

# title
# director
# year

# The Matrix
# Wachowski
# 1999

def print_movie(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

movie = {
    "title": "The Matrix",
    "director": "Wachowski",
    "year": 1999
}

print_movie(**movie)

# title: The Matrix
# director: Wachowski
# year: 1999

def print_movie(movie_details):
    for key, value in movie_details.items():
        print(f"{key}: {value}")

movie = {
    "title": "The Matrix",
    "director": "Wachowski",
    "year": 1999
}

print_movie(movie)

# title: The Matrix
# director: Wachowski
# year: 1999

def sum(*args):
    sum = 0
    for number in args:
        sum = sum+number
    print(sum)

sum(1,4)



def country_name(names):
    print()

    for name in names:
        print(country.format(**country))
    print()


country = {
    "name": "Germany",
    "population": "83 million",
    "capital": "Berlin",
    "currency": "Euro"
}

country = {
    "name": "Germany",
    "population": "83 million",
    "capital": "Berlin",
    "currency": "Euro"
}

output = "Country: {name}\nPopulation: {population}\nCapital: {capital}\nCurrency: {currency}"

print(output.format(**country))

def country_name(names):
    country = {
        "name": "Germany",
        "population": "83 million",
        "capital": "Berlin",
        "currency": "Euro"
    }

    for name in names:
        print(f"Country: {name}")
        print(f"Population: {country['population']}")
        print(f"Capital: {country['capital']}")
        print(f"Currency: {country['currency']}")
        print()

country_names = ["Germany", "France", "Spain"]
country_name(country_names)

numbers = range(1, 21)
print(*numbers, sep='\n')

base = deque([1, 2, 3, 4, 5])
    
# rotates base 2 steps to the left
base.rotate(-2)  # deque([3, 4, 5, 1, 2])
print(base) 
# rotates base 3 steps to the right
base.rotate(3)   # deque([5, 1, 2, 3, 4])

base = deque([1, 2, 3])
base.rotate()  #
print(base) 


names = ["John", "Anne", "Peter"]
ages = [26, 31, 29]

for i in range(len(names)):
	print(f"{names[i]} is {ages[i]} years old.")
        
ames = ["John", "Anne", "Peter"]
ages = [26, 31, 29]

for name, age in zip(names, ages):
	print(f"{name} is {age} years old.")
        
zipped = [("John", 26), ("Anne", 31), ("Peter", 29)]
names, ages = zip(*zipped)

print(names)  # ("John", "Anne", "Peter")
print(ages)   # (26, 31, 29)

from collections import namedtuple

Student = namedtuple("Student", ["name", "age", "faculty"])

names = ["John", "Steve", "Mary"]
ages = [19, 20, 18]
faculties = ["Politics", "Economics", "Engineering"]

students = [
    Student(*student_details)
    for student_details in zip(names, ages, faculties)
]


def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)

# Convert the result to a list (for Python 3)
squared_numbers_list = list(squared_numbers)

print(squared_numbers_list)  # Output: [1, 4, 9, 16, 25]


'''

In Python, map() is a built-in function that applies a 
specified function to each item in an iterable (such as
 a list, tuple, or other sequence) and returns a new 
 iterable containing the results.It provides a concise
 way to transform the elements of a collection without
   using explicit loops.
map(function, iterable)

'''

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x ** 2, numbers)
squared_numbers_list = list(squared_numbers)

print(squared_numbers_list)  # Output: [1, 4, 9, 16, 25]
