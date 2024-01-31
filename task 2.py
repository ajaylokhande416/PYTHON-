class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

def add_contact(contact_list, name, phone, email):
    contact = Contact(name, phone, email)
    contact_list.append(contact)
    print(f"Contact {name} added successfully!")

def view_contacts(contact_list):
    if not contact_list:
        print("Contact book is empty.")
    else:
        print("Contacts:")
        for idx, contact in enumerate(contact_list, start=1):
            print(f"{idx}. {contact.name} - Phone: {contact.phone}, Email: {contact.email}")

def search_contact(contact_list, name):
    for contact in contact_list:
        if contact.name.lower() == name.lower():
            print(f"Contact found: {contact.name} - Phone: {contact.phone}, Email: {contact.email}")
            return
    print(f"No contact found with the name {name}.")

def main():
    contacts = []

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Enter choice (1/2/3/4): ")

        if choice == '4':
            print("Exiting the Contact Book.")
            break

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            email = input("Enter contact email: ")
            add_contact(contacts, name, phone, email)

        elif choice == '2':
            view_contacts(contacts)

        elif choice == '3':
            name_to_search = input("Enter contact name to search: ")
            search_contact(contacts, name_to_search)

        else:
            print("Invalid Input. Please enter a valid option.")

if __name__ == "__main__":
    main()
