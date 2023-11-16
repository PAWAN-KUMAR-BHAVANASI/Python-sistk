#Reversal of a number as int
Number = int(input("Please Enter any Number: ")) 
Reverse = 0 
while(Number > 0): 
   Reminder = Number % 10 
   Reverse = (Reverse *10) + Reminder 
   Number = Number //10 
print("Reverse of entered number is :" ,Reverse)


# Input a number as a string
num_str = input("Enter a number: ")
reverse_num = int(num_str[::-1])
print("Reversed number:", reverse_num)
