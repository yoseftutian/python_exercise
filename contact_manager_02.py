import os


class ContactManager:

    def __init__(self, contact_list_path):
        self.contact_list_path = contact_list_path
        with open(self.contact_list_path, "w") as file:  # w for overwrite and create new list, a for append to existing
            file.write("Contacts List\n")

    @staticmethod
    def AddContact():
        name = input("Please enter the name: \n")
        phone = input("Please enter the phone: \n")
        email = input("Please enter the email: \n")
        with open("contact_list.txt", "a") as file:
            file.write(name + " " + phone + " " + email + "\n")

    def ReadContacts(self):
        with open(self.contact_list_path, "r") as file:
            file_read = file.read()
            all_contacts = []
            contact = ""
            for i in file_read:
                if i != " ":
                    contact += i
                else:
                    contact += " "
                if i == "\n":
                    all_contacts.append(contact[:-1])
                    contact = ""

            return all_contacts  # TODO: put all contacts in  dictionary to search for better search and update

    def SearchContact(self):
        name_to_search = input("Please enter the name for search: \n")
        all_contacts = ContactManager.ReadContacts(self)
        for i in all_contacts:
            if name_to_search in i:
                print("The contact was found at line: ", all_contacts.index(i), "\n", i, "\n")
                return i
            elif all_contacts.index(i) == len(all_contacts) - 1:
                print("The contact was not found at the whole list \n")
            else:
                print("The contact was not found at the line: ", all_contacts.index(i))
                continue

    def UpdateInformation(self):
        name_to_change = input("Please enter the contact name to update: \n")
        place = ""
        all_contacts = ContactManager.ReadContacts(self)
        for i in all_contacts:
            if name_to_change in i:
                place = all_contacts.index(i)
        if place == "":
            print("Opps, the name was not found!")
        if place != "":
            name = input("Please enter the name: \n")
            phone = input("Please enter the phone: \n")
            email = input("Please enter the email: \n")

            all_contacts[place] = name + " " + phone + " " + email + "\n"
            with open("contact_list.txt", "w") as file:
                updated_list = ""  # changing back to string to append to text file new information
                for i in all_contacts:
                    if "\n" in i:
                        updated_list += i[:-1] + "\n"

                    else:
                        updated_list += i + "\n"

                file.write(updated_list)
                print("The contact found and updated!\n")


if __name__ == '__main__':
    execution_of_program = True
    while execution_of_program:
        option = input(
            "1. Create list\n2. Add contact\n3. View all contacts\n4. Search "
            "contact\n5. Update contact\n0. To exit the program and delete the file created\nPlease choose your "
            "action: ")
        match option:
            case "1":
                customer1 = ContactManager("contact_list.txt")
            case "2":
                try:
                    customer1.AddContact()
                except:
                    print("The list does not exist, please create the list first!")
            case "3":
                count = 0
                for i in customer1.ReadContacts():
                    print(count, " ", i)
                    count += 1
                print()
            case "4":
                customer1.SearchContact()
            case "5":
                customer1.UpdateInformation()
            case "0":
                print("The program is ended and the file was deleted!")
                os.remove("contact_list.txt")  # remove file
                execution_of_program = False  # change the variable to False to stop the
                # execution of program (while loop)
            case _:
                print("Please choose an option from available operations: ")
