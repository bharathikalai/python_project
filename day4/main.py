def add_contact(contacts,name,phone_number,email):
    num_contact = (name,phone_number,email)
    contacts.append(num_contact)
    print(f"contact {name} added successfully")


def display_contacts(contacts):
    if not contacts:
        print("no contacts found")
    else:
        print("list of contacts: ")
        for idx,contact in enumerate(contacts, start=1):
            a,b,c = contact
            print(f"{idx}. name: {a},phone:{b},{c}email")


def main():
    contacts = []

    while True:
        print("\n1. Add Contact")
        print("2. Display Contacts")
        print("3. Exit")

        choice = input("enter your choice: ")

        if choice == "1":
            name = input("enter your contact name")
            phone_number = input("Enter your phone number")
            email = input("enter your email address")

            add_contact(contacts,name,phone_number,email)
        elif choice == "2":
            display_contacts(contacts)

        elif choice == "3":
            print("exiting program")
            break
        else:
            print("invalid choice please enter valid choice")

if __name__ == "__main__":
    main()