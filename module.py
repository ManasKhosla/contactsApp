''' This is a module for contacts app made in python '''

# for adding new numbers
def add(dict):
    name = input("Enter the name: ")
    number = int(input("Enter the number: "))
    dict[name.capitalize()] = number
    return

# for deleting the contacts
def delete(dict):
    name = input("Enter the name you want to delete: ")
    del dict[name.capitalize()]
    return

# for updating contacts 
def update(dict):
    name = input("Enter the name you want to update: ")
    number = int(input("Enter the number: "))
    dict[name.capitalize()] = number
    return

# for searching contacts
def search(dict):
    name = input("Enter the name you want to search: ")
    return dict.get(name.capitalize())

# for showing all contacts
def show(dict):
    print("-"*100)
    print("Name"," "*46,"Number")
    print("-"*100)
    for i in sorted(dict.keys()):
        c = 50-len(str(i))-2
        print("  ",i," "*c,dict.get(i))
    return