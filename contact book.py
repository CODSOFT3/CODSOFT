import json

CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Show menu options
def show_menu():
    print("\n===== CONTACT MANAGEMENT SYSTEM =====")
    print("⿡  Add Contact")
    print("⿢  View Contacts")
    print("⿣  Search Contact")
    print("⿤  Update Contact")
    print("⿥  Delete Contact")
    print("⿦  Exit")

# Add a new contact
def add_contact(contacts):
    print("\n📌 Add New Contact")
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()

    if name and phone:
        contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        save_contacts(contacts)
        print("✅ Contact added successfully!")
    else:
        print("⚠ Name and Phone Number are required!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("\n📂 No contacts found!")
    else:
        print("\n📞 Contact List:")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['name']} - {contact['phone']}")

# Search for a contact
def search_contact(contacts):
    search_term = input("\n🔍 Enter Name or Phone Number to Search: ").strip().lower()
    results = [c for c in contacts if search_term in c["name"].lower() or search_term in c["phone"]]

    if results:
        print("\n🔹 Search Results:")
        for contact in results:
            print(f"📌 Name: {contact['name']}\n📞 Phone: {contact['phone']}\n📧 Email: {contact['email']}\n🏠 Address: {contact['address']}\n")
    else:
        print("❌ No contacts found!")

# Update a contact
def update_contact(contacts):
    search_term = input("\n✏ Enter Name or Phone Number to Update: ").strip().lower()
    for contact in contacts:
        if search_term in contact["name"].lower() or search_term in contact["phone"]:
            print(f"\nUpdating Contact: {contact['name']} ({contact['phone']})")
            contact["name"] = input("Enter New Name (or press Enter to keep current): ") or contact["name"]
            contact["phone"] = input("Enter New Phone (or press Enter to keep current): ") or contact["phone"]
            contact["email"] = input("Enter New Email (or press Enter to keep current): ") or contact["email"]
            contact["address"] = input("Enter New Address (or press Enter to keep current): ") or contact["address"]
            save_contacts(contacts)
            print("✅ Contact updated successfully!")
            return
    print("❌ Contact not found!")

# Delete a contact
def delete_contact(contacts):
    search_term = input("\n🗑 Enter Name or Phone Number to Delete: ").strip().lower()
    for contact in contacts:
        if search_term in contact["name"].lower() or search_term in contact["phone"]:
            contacts.remove(contact)
            save_contacts(contacts)
            print("🗑 Contact deleted successfully!")
            return
    print("❌ Contact not found!")

# Main function
def main():
    contacts = load_contacts()

    while True:
        show_menu()
        choice = input("\n🔹 Choose an option (1-6): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("\n👋 Exiting... Have a great day!")
            break
        else:
            print("⚠ Invalid choice! Please enter a number between 1-6.")

if __name__ == "_main_":
    main()
