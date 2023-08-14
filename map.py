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
