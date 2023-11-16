#Operations on Tuple
# Empty tuple
my_tuple = ()
print(my_tuple)  # Output: ()
# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)  # Output: (1, 2, 3)
# tuple with mixed datatypes
t1 = (123, 10.5, 'hi', 'hello')
print(type(t1))
print('Elements in tuple are', t1)
# Slicing and indexing
print(t1[1:])
print(t1[:3])
print(t1[3])
# Tuple operations
print('Index value for 123 ', t1.index(123))
print('hi vale occured times in tuple is', t1.count('hi'))
print('Lenght of the tuple is', len(t1))
t2 = ['acd', 'bca', 'abc', 'acd']
t3 = ['xza', 'xyz']
print(max(t2))
print(min(t2))
print(max(t3))
print(min(t3))
del t3
print(t3)