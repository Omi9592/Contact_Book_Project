# Contact_Book_Project
📒 Contact Book (Python CLI)

A simple, functional Contact Book application written in Python.
It lets you add, view, search, update, and delete contacts, all stored persistently in a JSON file.

🚀 Features

Add new contacts

Email validation (@gmail.com only)

Phone validation (10 digits)

View all saved contacts

Search contacts by:

Name (case-insensitive)

Email

Phone

Update any contact field

Delete contacts

Count total contacts

Auto-save to contacts_data.json

📂 Project Structure
project/
│
├── contact_book.py        # Your main program (contains classes + logic)
├── contacts_data.json     # Auto-created JSON contact database
└── README.md              # Documentation

🛠 Requirements

Python 3.8+

No external modules — uses only:

json

uuid

typing

▶️ How to Run

Open your terminal / PowerShell.

Navigate to your project folder.

Run:

python contact_book.py


Follow the on-screen menu to manage contacts.

🧩 How the Code Works
Contact Class

Generates a unique ID per contact

Validates email and phone

Converts contact to/from dictionary for JSON storage

ContactBook Class

Handles:

Loading contacts from JSON

Saving contacts after changes

Adding new contacts

Searching, updating, deleting

Counting total contacts

User Input (CLI)

Your script uses input() to get user details like:

name

email

phone
Based on menu selections.

💾 Data Format

Contacts are stored in contacts_data.json as:

[
    {
        "id": "bcd31e2e-db47-4c89-bd28-8a4b5980e00d",
        "name": "Alice Kumar",
        "email": "alice@gmail.com",
        "phone": "9876543210"
    }
]

🧹 Future Enhancements (If you choose)

Use regex for email validation

Export contacts to CSV

Add terminal colors for better UI

Replace UUID with short numeric IDs

Add GUI (Tkinter)

If you want, I can also generate:

✅ Menu-based CLI for contact_book.py
✅ Pretty-print output tables
✅ GitHub badges + improved README
✅ Folder structure for a professional project
