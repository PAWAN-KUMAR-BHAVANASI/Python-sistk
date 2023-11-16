#Program to find the Biggest number among three
print("Finding the Biggest number among the 3 number")
a=int(input("Enter number-a: "))
b=int(input("Enter number-b: "))
c=int(input("Enter number-c: "))
if a>b and a>c:
    print(a,"a is maximum")  
elif b>c:
    print(b,"b is maximum")
else:
    print(c,"c is maximum")

#Another method using max() function
print(max(a,b,c),"is the maximum number")