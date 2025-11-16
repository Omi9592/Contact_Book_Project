import json
import uuid
from typing import List, Dict, Optional

DATAFILE = "contacts_data.json"

class Contact:
    def __init__(self , name: str, email: str, phone: str, contact_id: Optional[str]= None):
        self.id = contact_id if contact_id else str(uuid.uuid4())
        self.name = name
        self.email = email 
        self.phone = phone

    @staticmethod
    def is_valid_email(email: str) -> bool: 
        return email.endswith("@gmail.com")    
    
    @staticmethod
    def is_valid_phone(phone: str) -> bool:
        return phone.isdigit() and len(phone) == 10
    
class ContactBook:
    def __init__(self , path: str = DATAFILE):
        self.path = path
        self.contacts: Dict[str, Contact] = {}
        self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.path, 'r') as file:
                data = json.load(file)
                for contact_data in data:
                    contact = Contact(**contact_data)
                    self.contacts[contact.id] = contact
        except FileNotFoundError:
            self.contacts = {}
        except json.JSONDecodeError:
            self.contacts = {}

    def save_contacts(self):
        with open(self.path, 'w') as file:
            data = [vars(contact) for contact in self.contacts.values()]
            json.dump(data, file, indent=4)

    def add_contact(self, name: str, email: str, phone: str) -> Optional[Contact]:
        if not Contact.is_valid_email(email):
            print("Invalid email format. Must end with '@gmail.com'.")
            return None
        if not Contact.is_valid_phone(phone):
            print("Invalid phone number. Must be 10 digits.")
            return None
        contact = Contact(name, email, phone)
        self.contacts[contact.id] = contact
        self.save_contacts()
        return contact
    
    def view_contacts(self) -> List[Contact]:
        return list(self.contacts.values()) 
        print("No contacts available.") 
    
    def find_contact_by_name(self, name: str) -> List[Contact]:
        return [contact for contact in self.contacts.values() if contact.name.lower() == name.lower()]
        print
    
    def find_contact_by_email(self, email: str) -> List[Contact]:
        return [contact for contact in self.contacts.values() if contact.email.lower() == email.lower()]
        print
    
    def find_contact_by_phone(self, phone: str) -> List[Contact]:
        return [contact for contact in self.contacts.values() if contact.phone == phone]
        print("No contact found with the given phone number.")
    
    def update_contact(self, contact_id: str, name: Optional[str]= None, email: Optional[str]= None, phone: Optional[str]= None) -> bool:
        contact = self.contacts.get(contact_id)
        if not contact:
            return False
        if name:
            contact.name = name
        if email:
            if not Contact.is_valid_email(email):
                print("Invalid email format. Must end with '@gmail.com'.")
                return False
            contact.email = email
        if phone:
            if not Contact.is_valid_phone(phone):
                print("Invalid phone number. Must be 10 digits.")
                return False
            contact.phone = phone
        self.save_contacts()
        return True
    def delete_contact(self, contact_id: str) -> bool:
        if contact_id in self.contacts:
            del self.contacts[contact_id]
            self.save_contacts()
            return True
        return False
       
    def count_contacts(self) -> int:
        return len(self.contacts)
        
def menu() -> None:
    cb = ContactBook()
    while True:
        print("Contact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact by Name")
        print("4. Search Contact by Email")
        print("5. Search Contact by Phone")
        print("6. Update Contact")
        print("7. Delete Contact")
        print("8. Count Contacts")
        print("9. Exit")
        
        choice = input("Enter your choice (1-9): ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            contact = cb.add_contact(name, email, phone)
            if contact:
                print(f"Contact added with ID: {contact.id} successfully.")
        
        elif choice == '2':
            contacts = cb.view_contacts()
            if contacts:
                for contact in contacts:
                    print(f"ID: {contact.id}, Name: {contact.name}, Email: {contact.email}, Phone: {contact.phone}")
            else:
                print("No contacts available.")

        elif choice == '3':
            name = input("Enter name to search: ")
            results = cb.find_contact_by_name(name)
            if results:
                for contact in results:
                    print(f"ID: {contact.id}, Name: {contact.name}, Email: {contact.email}, Phone: {contact.phone}")
            else:
                print("No contact found with the given name.")

        elif choice == '4':
            email = input("Enter email to search: ")
            results = cb.find_contact_by_email(email)
            if results:
                for contact in results:
                    print(f"ID: {contact.id}, Name: {contact.name}, Email: {contact.email}, Phone: {contact.phone}")
            else:
                print("No contact found with the given email.")

        elif choice == '5':
            phone = input("Enter phone to search: ")
            results = cb.find_contact_by_phone(phone)
            if results:
                for contact in results:
                    print(f"ID: {contact.id}, Name: {contact.name}, Email: {contact.email}, Phone: {contact.phone}")
            else:
                print("No contact found with the given phone number.")

        elif choice == '6':
            contact_id = input("Enter contact ID to update: ")
            name = input("Enter new name (leave blank to keep unchanged): ")
            email = input("Enter new email (leave blank to keep unchanged): ")
            phone = input("Enter new phone (leave blank to keep unchanged): ")
            updated = cb.update_contact(contact_id, name if name else None, email if email else None, phone if phone else None)
            if updated:
                print("Contact updated successfully.")
            else:
                print("Failed to update contact. Check the ID and try again.")
        
        elif choice == '7':
            contact_id = input("Enter contact ID to delete: ")
            deleted = cb.delete_contact(contact_id)
            if deleted:
                print("Contact deleted successfully.")
            else:
                print("Failed to delete contact. Check the ID and try again.")

        elif choice == '8':
            count = cb.count_contacts()
            print(f"Total contacts: {count}")   

        elif choice == '9':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()

            
           
        


    

    

  
    
   
    
        
    
    

    

    


        