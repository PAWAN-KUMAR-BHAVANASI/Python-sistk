#Python script to display the power of given Number using function 
number = int(input("Enter any positive Integer: "))
exponent = int(input("Enter any Exponent Value: "))

power = 1
i = 1

while(i<=exponent):
    power = power*number
    i=i+1
print(f"The result of {number} power {exponent} = {power}")