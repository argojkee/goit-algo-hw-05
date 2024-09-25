import functions
from contacts import contacts

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = functions.parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(functions.add_contact(args, contacts))
        elif command == "phone":
            print(functions.show_phone(args, contacts))
        elif command == 'change':
            print(functions.change_contact(args, contacts))
        elif command == 'all':
            functions.show_all(contacts)
        
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()