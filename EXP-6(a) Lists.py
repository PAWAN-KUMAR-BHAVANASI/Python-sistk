#Operations on Lists
# Creating List
list1 = [123, 'hello', 12.6, 'mango']
print(list1)
print(type(list1))
# Access Elements in list
print(list1[0])
print(list1[2])
# Slice List
print(list1[0:2])
print(list1[2:3])
# change or add elements to a list
list1[2] = 10
print('List after changing value at index 2 is', list1)
list1.append(-1)
list1.extend([123, 45])
print(list1)
list1.insert(3, 20)
print('List after adding elements', list1)
# Delete or remove elements from a list
list1.remove('hello')
print('After Deleting', list1)