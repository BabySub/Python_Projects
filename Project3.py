import json

def add_person():
    Name = input("Name: ")
    Age = input("Age: ")
    Email = input("Email: ") 

    # dictionary has keys that associates the values to it
    # here 'NAMES' is the key and value will be the input put in 'Name'  
    person ={"NAMES": Name, "AGES": Age, "EMAILS":Email}
    return person

def delete_person(people):
    if not people:  # Check if the contact list is empty
        print("No contacts to delete.")
        return

    # Display all contacts
    print("\nContacts List:")
    for i, person in enumerate(people):
        print(i+1, "-", person["NAMES"], "|", person["AGES"], '|', person["EMAILS"])

    while True:
        number = input("\nEnter the index number to delete: ")
        try:
            number = int(number)
            if 1 <= number <= len(people):
                # Remove the selected contact, and saves it in deleted_person to display later
                deleted_person = people.pop(number - 1)
                print("\nContact deleted successfully:")
                print(deleted_person["NAMES"], deleted_person["AGES"], deleted_person["EMAILS"])
                break  # Exit the loop after successful deletion
            else:
                print("INVALID! Number out of range.")
        except:
            print("Invalid input! Please enter a valid number.")


def display(people):
    print("\nContacts List:")
    for i, person in enumerate(people):
        print(i+1, "-", person["NAMES"], "|", person["AGES"], '|', person["EMAILS"])


def search(people):
    search_name = input("\nEnter name to search: ").lower()
    results = []
    for person in people:
        name = person["NAMES"]
        if search_name in name.lower():
            results.append(person)
    display(results)

print("Hi, welcome to my contact management system")


# this section here helps to read the previosuly saved input (if there are any)
# previous inputs are svaed inside json file nmaed "contacts.json"
with open("contacts.json", "r") as f:           # 'r' -> for read
    people= json.load(f)["contacts"]



if len(people) != 0:
    display(people)

while True:
    command = input("\nYou can 'add', 'delete', 'display' or 'search' contacts contacts. Press 'Q' to quit. \n").lower()

    if command == "add":
        person = add_person()
        people.append(person)
        print("Your person has been added")
    elif command == "delete":
        delete_person(people)
    elif command == "search":
        search(people)
    elif command == "q":
        break
    elif command== "display":
        display(people)
    else:
        print("INVALID INPUT")



# after every action has been performed, this little section of json helps write  
# in the json file named "contacts.json" so that next time when the code is run 
# it has the previously saved inputs 
with open("contacts.json", "w") as f:               # 'w' -> for write
    json.dump({"contacts": people},f)