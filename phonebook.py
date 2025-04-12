# This is a simple Phonebook App. The users can:
# 1) Add new contacts
# 2) Remove contacts
# 3) Search for contacts
# 4) Display all contacts
# 5) Delete all contacts
# 6) Exit the app

import sys

def initial_phonebook():
    # Name -> Mandatory
    # Phone number -> Mandatory
    # Email -> Optional
    # Date of Birth -> Optional
    # Category (Family/Friends/Work/Others) -> Mandatory

    rows = int(input("Enter the initial no. of contacts: "))
    cols = 5

    phone_book = []

    for i in range(rows):
        print(f"Enter contact {i+1} details in the following order ONLY.")
        print("Note: * indicates mandatory fields.")
        print(".............................................")
        temp = []
        
        for j in range(cols):
            if j == 0:
                temp.append(input("Enter name* : "))
                if temp[j] == '' or temp[j] == ' ':
                    sys.exit("Name is a mandatory field. Process exiting due to blank field.")
            if j == 1:
                temp.append(int(input("Enter phone number* : ")))

            if j == 2:
                temp.append(input("Enter email address : "))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
                    
            if j == 3:
                temp.append(input("Enter date of birth (dd/mm/yy) : "))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None

            if j == 4:
                temp.append(input("Enter category (Family/Friends/Work/Others)*: "))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = 'Others'

            
        phone_book.append(temp)
    print(phone_book)
    return phone_book

def menu():
    print(".............................................")
    print("...............-Phonebook Directory-...............")
    print(".............................................")
    print("\nYou can perform following operations: \n")
    print("1) Add new contacts")
    print("2) Remove contacts")
    print("3) Search for contacts")
    print("4) Display all contacts")
    print("5) Delete all contacts")
    print("6) Exit phonebook app")

    choice = int(input("Enter your choice: "))
    return choice  


def thanks():
    print(".............................................")
    print("----------------Thank you for using our Phoneboook Directory System.----------------")
    print("----------------Please visit again. Goodbye. Have a great time.----------------")
    print(".............................................")


print(".............................................")
print("----------------Hello user! Welcome to the Phonebook Directory System.----------------")
print("----------------Now, you can proceed with exploring the directory.----------------")
print(".............................................")

choice = 1
phonebooks = initial_phonebook()
while choice in (1, 2, 3, 4, 5)
    choice = menu()
    if choice == 1:
        phonebooks = []
    elif choice == 2:
        phonebooks = []
    elif choice == 3:
        phonebooks = []
    elif choice == 4:
        phonebooks = []
    elif choice == 5:
        phonebooks = []
    elif choice == 6:
        sys.exit()
    else: 
        thanks()