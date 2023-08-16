def even_numbers(n):
    for i in range(2, n + 1, 2):
        yield i

even_gen = even_numbers(10)
for num in even_gen:
    print(num)

'''

A generator function is defined using the yield
keyword instead of the return keyword. When the
generator function is called, it doesn't execute 
the entire function immediately. 
Instead, it returns a generator object, 
which can be iterated over using a loop 
or other iteration mechanisms.



'''
even_gen = (x for x in range(2, 11, 2))
for num in even_gen:
    print(num)



even_gen = (x for x in range(2, 11, 2))
values_as_strings = (str(num) for num in even_gen)
result = ', '.join(values_as_strings)
print(result)
