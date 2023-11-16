#program to remove punctuations
punctuations = '''!()-[];:'"\,<>./?@$#%^&*_~'''

my_string = input("Enter a string: ")
no_punct = ""
for char in my_string:
  if char not in punctuations:
    no_punct += char

print(no_punct)
