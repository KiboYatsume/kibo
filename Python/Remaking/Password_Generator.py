import secrets
import string
import sys

#generate password
def Password_Generator(pass_len,pass_type):
    password = ""
    password +="".join(secrets.choice(pass_type)for i in range (pass_len))
    return password

#Ask For PassWord Length

def ask_len():
    lenght = int(input("What Should be the lenght of your password ? \n"))
    return lenght


#Exit Block

def Exit():
    while True:
            print("Are you sure (yes/no) ? \n")
            try:
                confirmation = input("")
                if confirmation == "yes":
                    sys.exit()
                elif confirmation == 'no':
                        Password_Menu()
                else:
                    print("Invalid Input")
            except Exception as e :
                print(e) 

#User Menu

def Password_Menu():
    while True:
        print("***PassWord Menu*** \n 1.Pincode \n 2.Alphanumeric \n 3.Alphabetic \n 4.Alphabetic LowerCase \n 5.Alphabetic UpperCase \n 6.Exit")
        try:
            choice = int(input("Select An Option:"))
            if choice == 1:
                pass_len = ask_len()
                Generated_Pasword = Password_Generator(pass_len,string.digits)
                print(Generated_Pasword)
            elif choice == 2:
                pass_len = ask_len()
                Generated_Pasword = Password_Generator(pass_len,string.ascii_letters+string.digits+string.punctuation)
                print(Generated_Pasword)
            elif choice == 3:
                pass_len = ask_len()
                Generated_Pasword = Password_Generator(pass_len,string.ascii_letters)
                print(Generated_Pasword)
            elif choice == 4:
                pass_len = ask_len()
                Generated_Pasword = Password_Generator(pass_len,string.ascii_lowercase)
                print(Generated_Pasword)
            elif choice == 5:
                pass_len = ask_len()
                Generated_Pasword = Password_Generator(pass_len,string.ascii_uppercase)
                print(Generated_Pasword)
            elif choice == 6:
                Exit()

        except Exception as e:
            print(e)

#call function
Password_Menu()