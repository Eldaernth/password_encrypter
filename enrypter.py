def menu(passwords):
    print("1.Show passwords\n2.Add new password\n3.Delete password\n4.Exit")
    choice = get_user_input("Enter a number: ")
    if choice == "1":
        show_passwords(passwords)
    elif choice == "2":
        passwords.append(crypting())
        add_to_file(passwords)
    elif choice == "3":
        delete_pass(passwords)
    elif choice == "4":
        exit()
    else:
        raise KeyError("Wrong key")
        

def get_user_input(label):
    return input(label)


def add_to_file(passwords):
    with open("passwords.txt","w") as stored_passwords:
        for i in passwords:
            stored_passwords.write(i)



def read_from_file():
    with open("passwords.txt","r") as stored_passwords:
        return stored_passwords.readlines()


def show_passwords(passwords):
    for line in passwords:
        print(line)


def delete_pass(passwords):
    password = get_user_input("Enter password: ")
    for i in passwords:
        if password == i.split("\t")[0]:
            passwords.remove(i)
    add_to_file(passwords)


def crypting():
    list_of_letters = ["a", "b", "c" ,"d" ,"e" ,"f" ,"g" ,"h" ,"i" ,"j" ,"k" ,
                        "l" ,"m" ,"n" ,"o" ,"p" ,"q" ,"r" ,"s" ,"t" ,"u" ,"v" ,"w" ,"x" ,"y" ,"z",
                        "0","1","2","3","4","5","6","7","8","9"," ",",",".","_"]
    password = list(get_user_input("Enter password: "))
    crypted_password = []
    for chars in password:
        crypted_password.append(list_of_letters[list_of_letters.index(chars) - 3])
    string_password = "{}\t{}\n".format("".join(password),"".join(crypted_password))
    return string_password


def main():
    while True:
        passwords = [x for x in read_from_file()]
        menu(passwords)
    

if __name__ == "__main__":
    main()