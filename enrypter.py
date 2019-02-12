def menu(passwords):
    print("1.Show passwords\n2.Add new password\n3.Save in file")
    choice = get_user_input("Enter a number: ")
    if choice == "1":
        show_passwords(read_from_file())
    elif choice == "2":
        passwords.append(crypting())
    elif choice == "3":
        add_to_file(passwords)

def get_user_input(label):
    return input(label)


def add_to_file(passwords):
    stored_passwords = open("passwords.txt","r+")
    for i in range(len(passwords)):
        stored_passwords.write(passwords)


def read_from_file():
    stored_passwords = open("passwords.txt","r+")
    return stored_passwords.readlines()

def show_passwords(passwords):
    for i in passwords:
        print(i)


def crypting():
    list_of_letters = ["a", "b", "c" ,"d" ,"e" ,"f" ,"g" ,"h" ,"i" ,"j" ,"k" ,
                        "l" ,"m" ,"n" ,"o" ,"p" ,"q" ,"r" ,"s" ,"t" ,"u" ,"v" ,"w" ,"x" ,"y" ,"z",
                        "0","1","2","3","4","5","6","7","8","9"]
    password = get_user_input("Enter password: ")
    list_of_passwords = list(password)
    crypted_password = []
    for chars in list_of_passwords:
        crypted_password.append(list_of_letters[list_of_letters.index(chars) - 3])
    return (password,"".join(crypted_password))

def main():
    passwords = [x for x in read_from_file()]
    menu(passwords)
    

if __name__ == "__main__":
    main()