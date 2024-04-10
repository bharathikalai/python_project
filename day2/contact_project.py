class Contact:
    def __init__(self,name,phone_number,email):
        self.name = name
        self.phone_number = phone_number
        self.email = email
    def __str__(self):
        return f"name: {self.name}\nPhone: {self.phone_number}\nEmail: {self.email}"

class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self,contact):
        self.contacts.append(contact)

    def display_contacts(self):
        if not self.contacts:
            print("no contacts found")
        else:
            for contact in self.contacts:
                print(contact)
                print("-" * 20)



def main():
    contact_list = ContactList()

    while True:
        print("\n1. Add contact")
        print("2. Display Contacts")
        print("3. Exit")

        choice = input("enter your choice:")
        if choice == "1":

            name = input("enter contact name: ")
            phone = input("enter contact phone number: ")
            email = input("enter contact email ")

            contact = Contact(name,phone,email)
            contact_list.add_contact(contact)
            print("contact added successfully")
        elif choice == "2":
            contact_list.display_contacts()
        elif choice == "3":
            print("Exiting..........")
            break
        
        else:
            print("invalid choice please try again")

if __name__ =="__main__":
    main()
