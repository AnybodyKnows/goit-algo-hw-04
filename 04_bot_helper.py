

contucts_book = []

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args  

def add_contact(command, *args):
    contucts_book.append({"Name": args[0],"Phone": args[1]}) 
    return ("added")

def change_contact(command, *args):
    return ("updated")

def show_phone(command, *args):
    return ("!!!tel number should be here")

def show_all(command, *args):
    return ("!!!All telephones should be here")


def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, *args = parse_input(user_input) 

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command in ["hello"]:
            print("Hello how can I help you?")
        elif command in ["add"]:
              result = add_contact(command, *args)
              print(result)
        elif command in ["change"]:
              result = change_contact(command, *args)
              print(result)
        elif command in ["phone"]:
              result = show_phone(command, *args)
              print(result)
        elif command in ["all"]:
              result = show_all(command, *args)
              print(result)              
        else:
            print("Invalid comand")     

if __name__ == "__main__":
    main()