class ContactManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def add_contact(self, name, phone, email):
        with open(self.file_path, 'a') as file:
            file.write(f"{name},{phone},{email}\n")

    def search_contact(self, param):
        pass

    def update_contact(self, param, param1, param2, param3):
        pass

    def read_contacts(self):
        pass


def read_contacts(self):
    with open(self.file_path, 'r') as file:
        contacts = file.readlines()
        for contact in contacts:
            print(contact.strip())  # הסרת תווים לא נרדפים כמו '\n'


def search_contact(self, name):
    with open(self.file_path, 'r') as file:
        contacts = file.readlines()
        for contact in contacts:
            if name in contact:
                print(contact.strip())
                break
        else:
            print(f"Contact with the name '{name}' not found.")


def update_contact(self, name, new_name, new_phone, new_email):
    with open(self.file_path, 'r') as file:
        lines = file.readlines()

        with open(self.file_path, 'w') as file:
            for line in lines:
                if name in line:
                    file.write(f"{new_name},{new_phone},{new_email}\n")
                else:
                    file.write(line)


# יצירת אובייקט מנהל אנשי קשר עם קובץ "contacts.txt"
contact_manager = ContactManager("contacts.txt")

# הוספת איש קשר
contact_manager.add_contact("David", "555-9876", "david@email.com")
contact_manager.add_contact("Dav", "555-9876", "david@email.com")

# קריאת רשימת אנשי קשר
contact_manager.read_contacts()

# חיפוש איש קשר
contact_manager.search_contact("Bob")

# עדכון מידע
contact_manager.update_contact("Bob", "Bob Smith", "555-4321", "bob.smith@email.com")

# קריאה מחדש לרשימת אנשי הקשר לאחר העדכון
# contact_manager.read_contacts()
