def menu():
    passwords = []
    print("1.Show passwords\n2.Add new password\n3.Delete password\n4.Exit")
    choice = get_user_input("Enter a number: ")
    if choice == "1":
        show_passwords(read_from_file())
    elif choice == "2":
        passwords.append(crypting())
        add_to_file(passwords)
    elif choice == "3":
        delete_pass()
    elif choice == "4":
        exit()
    else:
        raise KeyError("Wrong key")
        

def get_user_input(label):
    return input(label)


def add_to_file(passwords):
    stored_passwords = open("passwords.txt","a")
    stored_passwords.write("\t".join(passwords[-1]) + "\n")



def read_from_file():
    stored_passwords = open("passwords.txt","r")
    return stored_passwords.readlines()


def show_passwords(passwords):
    for line in passwords:
        print(line)


def delete_pass(passwords):
    password = get_user_input("")
    for i in passwords:
        if password == i:
            


def crypting():
    list_of_letters = ["a", "b", "c" ,"d" ,"e" ,"f" ,"g" ,"h" ,"i" ,"j" ,"k" ,
                        "l" ,"m" ,"n" ,"o" ,"p" ,"q" ,"r" ,"s" ,"t" ,"u" ,"v" ,"w" ,"x" ,"y" ,"z",
                        "0","1","2","3","4","5","6","7","8","9"," "]
    password = get_user_input("Enter password: ")
    list_of_passwords = list(password)
    crypted_password = []
    for chars in list_of_passwords:
        crypted_password.append(list_of_letters[list_of_letters.index(chars) - 3])
    return [password,"".join(crypted_password)]


def main():
    while True:
        menu()
    

if __name__ == "__main__":
    main()