#Program to check the matching lists
import collections 
list1 = [10, 20, 30, 40, 50] 
list2 = [10, 20, 30, 50, 40, 70] 
list3 = [50, 10, 30, 20, 40] 
list1.sort() 
list2.sort() 
list3.sort() 
if list1 == list3: 
 print ("The lists list1 and list3 are the same") 
else: 
 print ("The lists list1 and list3 are not the same") 
if list1 == list2: 
 print ("The lists list1 and list2 are the same") 
else: 
 print ("The lists list1 and list2 are not the same") 
if list2==list3:
    print("The lists list2 and list3 are the same")
else:
    print("The lists list2 and list3 are not the same")