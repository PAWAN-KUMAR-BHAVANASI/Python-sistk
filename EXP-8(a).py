def print_menu():
  print('Phone Book Menu')
  for i, item in enumerate(['Add name', 'Add phone number', 'Remove phone number', 'Lookup phone number', 'Quit']):
    print(f'{i + 1}. {item}')

numbers = {}
menu_choice = 0

while menu_choice != 5:
  print_menu()
  menu_choice = int(input("Type in a number (1-5): "))

  if menu_choice == 1:
    name = input("Enter a name: ")
    while name not in numbers:
      print("Name must be unique.")
      name = input("Enter a name: ")

    numbers[name] = None
    print("Name added successfully.")

  elif menu_choice == 2:
    name = input("Enter the name of the person whose phone number you want to add: ")
    if name not in numbers:
      print("Name not found.")
    else:
      phone = input("Enter the phone number: ")
      numbers[name] = phone
      print("Phone number added successfully.")

  elif menu_choice == 3:
    name = input("Enter the name of the person whose phone number you want to remove: ")
    if name in numbers:
      del numbers[name]
      print("Phone number removed successfully.")
    else:
      print("Name not found.")

  elif menu_choice == 4:
    name = input("Enter the name of the person whose phone number you want to lookup: ")
    if name in numbers:
      print(f"The phone number of {name} is {numbers[name]}")
    else:
      print("Name not found.")

  elif menu_choice != 5:
    print("Invalid choice.")

print("Goodbye!")
