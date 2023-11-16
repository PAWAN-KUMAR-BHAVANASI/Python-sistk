#Program to swap numbers
# To take input from the user
a = int(input('Enter value of a: '))
b = int(input('Enter value of b: '))
#if a is 10 & b is 52 
a=a+b  #from 10 to 62
b=a-b  #from 52 to 10
a=a-b  #from 62 to 52
print('The value of a after swapping: {}'.format(a))
print('The value of b after swapping: {}'.format(b))

#Swapping of two numbers using a temp variable
x = int(input('\nEnter value of x: '))
y = int(input('Enter value of y: '))
temp = x
x = y
y = temp
print('The value of a after swapping: {}'.format(x))
print(f'The value of b after swapping: {y}')

#Swapping of numbers in defferent method
_1st = int(input("\nEnter the first number:"))
_2nd = int(input("Enter the second number:"))
_1st,_2nd = _2nd,_1st
print(f"After swapping 1st number = {_1st} and 2nd number = {_2nd}")