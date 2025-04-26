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

def add_contacts(phonebook):
    dip = []
    for i in range(len(phonebook[0])):
        if i == 0:
            dip.append(input("Enter name: "))
        if i ==1:
            dip.append(input("Enter phone number: "))
        if i == 2:
            dip.append(input("Enter email: "))
        if i == 3:
            dip.append(input("Enter date of birth(mm/dd/yy): "))
        if i == 4:
            dip.append(input("Enter category (Family/Friends/Work/Others): "))

    phonebook.append(dip)
    return phonebook

def remove_existing_contact(phonebooks):
    query = input("Pleae enter the name of the contact you wish to remove: ")
    temp = 0

    for i in range(len(phonebooks)):
        if query == phonebooks[i][0]:
            temp += 1
            print(phonebooks.pop(i))
            print(f"Conacts has been removed for {query}")
            return phonebooks
    if temp == 0:
        print("Sorry, you have entered the wrong contact name.")
    return phonebooks

def search_for_contact(phonebooks):
    print("Enter search criteria: ")
    print("1. Name")
    print("2. Phoen Number")
    print("3. Email")
    print("4. Date of Birth (mm/dd/yy)")
    print("5. Category (Family/Friends/Work/Others)")
    choice = int("Enter your choice")
    
    temp = []
    check = -1
    if choice == 1:
        query = input("Enter the name: ")
        for i in range(len(phonebooks)):
            if query == phonebooks[i][0]:
                check = i
                temp.append(phonebooks[i])

    elif choice == 2:
        query = input("Enter the phone number: ")
        for i in range(len(phonebooks)):
            if query == phonebooks[i][1]:
                check = i
                temp.append(phonebooks[i])
    
    elif choice == 3:
        query = input("Enter the email: ")
        for i in range(len(phonebooks)):
            if query == phonebooks[i][2]:
                check = i
                temp.append(phonebooks[i])

    elif choice == 4:
        query = input("Enter the dob (mm/dd/yy): ")
        for i in range(len(phonebooks)):
            if query == phonebooks[i][3]:
                check = i
                temp.append(phonebooks[i])

    elif choice == 5:
        query = input("Enter the category (Family/Friends/Work/Others): ")
        for i in range(len(phonebooks)):
            if query == phonebooks[i][4]:
                check = i
                temp.append(phonebooks[i])  

    else:
        print("Invalid option: ")
        return -1
    if check == -1:
        return check
    else:
        display_all(temp)
        return check       
        
def display_all(phonebooks):
    if not phonebooks:
        print("No contatcs found")
    else: 
        for i in range(len(phonebooks)):
            print(phonebooks[i])

def delete_all(phonebooks):
    return phonebooks.clear()

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
while choice in (1, 2, 3, 4, 5):
    choice = menu()
    if choice == 1:
        phonebooks = add_contacts(phonebooks)
    elif choice == 2:
        phonebooks = remove_existing_contact(phonebooks)
    elif choice == 3:
        row = search_for_contact(phonebooks)
        if row == -1:
            print("The contact does not exist.")
        else:
            print(f"The contact found at row {row+1}")
    elif choice == 4:
        display_all(phonebooks)
    elif choice == 5:
         delete_all(phonebooks)
    elif choice == 6:
        sys.exit()
    else: 
        thanks()