contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")
        contacts[name] = [phone, email, address]
        print("Contact Added Successfully!")

    elif choice == "2":
        if contacts:
            for name, details in contacts.items():
                print(name, ":", details)
        else:
            print("No contacts found.")

    elif choice == "3":
        name = input("Enter Name to Search: ")
        if name in contacts:
            print(name, ":", contacts[name])
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter Name to Update: ")
        if name in contacts:
            phone = input("Enter New Phone: ")
            email = input("Enter New Email: ")
            address = input("Enter New Address: ")
            contacts[name] = [phone, email, address]
            print("Contact Updated!")
        else:
            print("Contact not found.")

    elif choice == "5":
        name = input("Enter Name to Delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact Deleted!")
        else:
            print("Contact not found.")

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")
