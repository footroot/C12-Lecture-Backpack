import sqlite3

conn = sqlite3.connect("contacts.sqlite")
cursor = conn.cursor()

with conn:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(50) NOT NULL,
            phone_number VARCHAR(15) NOT NULL UNIQUE
        );
        """)


def add_contact(name, phone):
    try:
        with conn:
            cursor.execute("""INSERT INTO contacts (name, phone_number) 
                           VALUES (?, ?)""", (name, phone,))
        print("Contact has been added successfully.")
    except sqlite3.IntegrityError:
        print("A contact with this phone number already exists.")

def view_contacts():
    cursor.execute("SELECT * FROM contacts;")
    contacts = cursor.fetchall()
    if contacts:
        print("Contacts:")
        for contact in contacts:
            print(f"ID: {contact[0]}, Name: {contact[1]}, Number {contact[2]}")

def update_contact(contact_id, new_name, new_phone):
    cursor.execute("UPDATE contacts SET name = ?, phone_number = ? WHERE id = ?;",
                   (new_name, new_phone, contact_id,))
    if cursor.rowcount:
        conn.commit()
        print("Contact has been updated.")
    else:
        print("No contact with that ID.")

def delete_contact(contact_id):
    cursor.execute("DELETE FROM contacts WHERE id = ?;", (contact_id,))
    if cursor.rowcount:
        conn.commit()
        print(f"Contact deleted.")
    else:
        print(f"No contact found.")

MENU = """Please select an option below:

1. Add Contact
2. View Contacts
3. Update Contact
4. Delete Contact

0. Exit
"""

while True:
    print(MENU)
    user_option = input(": ")

    if user_option == "1":
        name = input("Enter a name: ")
        phone = input("Enter a phone number: ")
        add_contact(name, phone)
    elif user_option == "2":
        view_contacts()
    elif user_option == "3":
        view_contacts()
        contact_id = int(input("Please enter ID of contact to edit: "))
        new_name = input("Enter new name: ")
        new_phone = input("Enter new phone number: ")
        update_contact(contact_id, new_name, new_phone)
    elif user_option == "4":
        view_contacts()
        contact_id = int(input("Please enter ID of contact to delete: "))
        delete_contact(contact_id)
    elif user_option == "0":
        break

conn.close()