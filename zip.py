''''

The zip() function in Python is used to combine 
multiple iterables (such as lists, tuples, or 
other sequences) element-wise into a single 
iterable. It aggregates corresponding 
elements from each input iterable and 
returns an iterator that produces tuples
containing those elements.

'''
a =[1,2,4,5]
b = ['e','r' , 't' , 'r']
s = zip(a,b)
list=list(s)
print(list)