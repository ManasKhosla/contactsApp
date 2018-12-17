''' main file for ui of contactsBook in python'''
from ast import literal_eval       # for converting string to dict
import module

# opening and reading the contacts
fo = open("phoneBook.txt", "r+")
text = fo.read()        # info saved in txt file
fo.close()

# converting string to dictionary using fxn from ast module
phoneBook = literal_eval(text)      # dict for saving info

# Introduction
print()
print("Python Contacts App v0.1\n")
module.show(phoneBook)
print("-"*100)
print("Number of contacts:",len(phoneBook.keys()))

# Menu
repeat = True
while repeat:
    print()
    print("*"*100)
    print("\tMenu")
    print("\t 1. Add new Contact")
    print("\t 2. Update Contact")
    print("\t 3. Delete Contact")
    print("\t 4. Search Contact")
    print("\t 5. Show all Contacts")
    print("\t 6. EXIT")
    print("*"*100)
    choice = int(input("Enter your choice: "))

    if choice==1:
        module.add(phoneBook)
    elif choice==2:
        module.update(phoneBook)
    elif choice==3:
        module.delete(phoneBook)
    elif choice==4:
        num = module.search(phoneBook)
        print("Contact information:",num)
    elif choice==5:
        module.show(phoneBook)
    elif choice==6:
        repeat = False
        break

# updating info
print("\n\nUpdating information...")
fo = open("phoneBook.txt", "w+")
text = fo.write(str(phoneBook))
fo.close()
print("Saved.")
input("Press Enter to Exit.")