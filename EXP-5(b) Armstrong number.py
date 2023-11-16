#Program to find the armstrong number between the range
armstrong = []
for i in range(0,1000):
    a = list(map(int,str(i)))
    b = list(map(lambda x:x**3,a))
    if(sum(b)==i):
        armstrong.append(i)
print(f"Armstrong number b/w 0 & 999 are {armstrong}")