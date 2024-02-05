

contucts_book = {}

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args  

def add_contact(command, *args):
    contucts_book[args[0]] = {"Phone": args[1]} 
    return ("added")

def change_contact(command, *args):
    if args[0] in contucts_book:
         contucts_book[args[0]] = {"Phone": args[1]}
         return ("Contact updated.")
    else:
         return f"Name {args[0]} not found in contucts"
    

def show_phone(command, *args):
    if contucts_book[args[0]]:
        return contucts_book[args[0]]["Phone"]
    else:
        return f"Phone number of {args[0]} not found in contucts"

    

def show_all(command, *args):
    return contucts_book


def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, *args = parse_input(user_input) 
        try:
            if command in ["close", "exit"]:
                print("Good bye!")
                break
            
            elif command in ["hello"]:
                print("Hello how can I help you?")
            
            elif command in ["add"]:
                if len(args) == 2:
                    result = add_contact(command, *args)
                    print(result)
                else:
                    print("incorrect number of arguments in comand")
        
            elif command in ["change"]:
                if len(args) == 2:
                    result = change_contact(command, *args)
                    print(result)
                else:
                    print("incorrect number of arguments in comand")
            
            elif command in ["phone"]:
                result = show_phone(command, *args)
                print(result)
            
            elif command in ["all"]:
                result = show_all(command, *args)
                print(result)              
            else:
                print("Invalid comand")     
        except:
            print("fallback error capture try to correct wrong number of arguments")
if __name__ == "__main__":
    main()