import re

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    if len(args)!=2:
        mess="Invalid data"
    else:
        name, phone = args
        contacts[name] = phone
        mess="Contact added."
    return mess

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name]=phone
        mess="Contact updated."
    else:
        mess="Contact not found"
            

    return mess

def show_phone(args, contacts):
    if len(args)>1:
        mess="Invalid data"
    else:
        kay=re.sub('\W','',str(args))
        if kay in contacts:
            mess=f"Contacts number:[{contacts[kay]}]"
        else:
            print(kay)
            mess="Contact not found"
    return mess

def show_all(contacts):
    if any(contacts):
        for key, value in contacts.items():
            print(key,"-",value)
    else:
        print("We don't have contacts.")
    

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
            print("I have comands: [add]/[change] /[phone]/[show all] contacts )))")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args,contacts))
        elif command == "show":
            show_all(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()


    