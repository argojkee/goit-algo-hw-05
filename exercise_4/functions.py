from input_error import input_error


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
        name, phone = args
        contacts[name] = phone
        return "Contact added."


@input_error
def change_contact(args, contacts):
        name, phone = args
        contacts[name] = phone
        return 'Contact updated.'

@input_error
def show_phone(args, contacts):
        name = args[0]
        return f'{name} : {contacts[name]}'

    
def show_all(contacts):
    for k,v in contacts.items():
        print(f'{k}:{v}')

