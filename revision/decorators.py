def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

'''Decorators are a powerful and flexible 
feature in Python that allow you to modify 
or extend the behavior of functions or methods
 without changing their actual code. Decorators
   are often used to add functionality, such as 
   logging, caching, authentication, or validation,
     to existing functions without directly modifying
       their implementation.

In Python, decorators are implemented using functions themselves. They take another function as input, perform some actions before or after the input function is called, and optionally return a modified or wrapped version of the input function




'''
def greeting_decorator(greeting_message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(greeting_message)
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@greeting_decorator("Welcome!")
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")

