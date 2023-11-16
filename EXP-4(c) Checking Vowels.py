#Program 
def check_vow(string,vowerls):
    vowel=[]
    cons=[]
    for each in string:
        if each in vowels:
            vowel.append(each)
        else:
            cons.append(each)
    print("Number of values",len(vowel))
    print("Vowels are",vowel)
    print("Number of consonents",len(cons))
    print("Consonents are",cons)
#Driver Code
string = input("Enter the First name if student: ")
vowels = 'AaEeIiOoUu'
check_vow(string,vowels)