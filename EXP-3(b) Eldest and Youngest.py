#Program to find the Youngest and Eldest Persons according to their ages
ram=int(input('Enter ram age: '))
sam=int(input('Enter sam age: '))
khan=int(input('Enter khan age: '))
# check eldest
if ram > sam and ram > khan:
 print("Person Ram is eldest")
elif sam > khan :
 print("Person Sam is eldest")
else:
 print("Person Khan is eldest")
# check youngest
if ram < sam and ram < khan:
 print("Person Ram is youngest")
elif sam < khan :
 print("Person Sam is youngest ")
else:
 print("Person Khan is youngest ")