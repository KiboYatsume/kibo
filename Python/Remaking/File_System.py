import sys
import pickle


#text file operations handeled here
def text_file_operation():

    #write
    def text_write():
        file = input("what is the name of the file ? \n")
        file_name = file+".txt"
        with open (file_name,'w') as file_main:     
            Content = input("Enter Your Content :")
            file_main.write(Content)
        return Content
    
    #read
    def text_read():
        file = input("what is the of the file ? \n")
        file_name = file+".txt"
        with open (file_name,'r') as file_main:
            print(file_main.read())
    
    #append
    
    def text_append():
        file = input("what is the of the file ? \n")
        file_name = file+".txt"
        with open (file_name,'a') as file_main:     
            Content = input("Enter Your Content :")
            file_main.write(Content)
        return Content
    
    #menu

    def text_menu():
        while True:
            print("***TEXT FILE MANUPILATION*** \n 1.Write(Existing Data Will Be Lost) \n 2.Read \n 3.Append New Data \n 4.Exit")
            try:
                choice = int(input("Select An Option :"))
                if choice == 1:
                    text_write()
                elif choice == 2:
                    text_read()
                elif choice == 3:
                    text_append()
                elif choice == 4:
                    break
            except Exception as e:
                print(e)
    text_menu()

#binary file operations hadeled here
def bianry_file_operations():

    #Object Class
    class MyClass:
        def __init__(self, value):
            self.value = value

    #write

    def binary_write():
        File_Name = input("Enter File Name : ")
        Extension = input("Enter The Desired Extension Of The File :")
        Content = input("Enter Content:")
        my_data = MyClass(Content)
        with open(File_Name+"."+Extension, "wb") as f:
            pickle.dump(my_data, f)
    
    #appned
    
    def binary_append():
        File_Name = input("Enter File Name : ")
        Extension = input("Enter The Desired Extension Of The File :")
        Content = input("Enter Content:")
        my_data = MyClass(Content)
        with open(File_Name+"."+Extension, "ab") as f:
            pickle.dump(my_data, f)
    
    #read
    def read_binary():
        File_Name = input("Enter File Name : ")
        Extension = input("Enter The Desired Extension Of The File :")
        with open(File_Name + "." + Extension, "rb") as f:
            while True:
                try:
                    my_data = pickle.load(f)
                    print(my_data.value)
                except EOFError as e:
                    print(e)

    
    #main
                    
    def binary_menu():
        while True:
            print("***BINARY FILE MANUPILATION*** \n 1.Write(Existing Data Will Be Lost) \n 2.Read \n 3.Append New Data \n 4.Exit")
            try:
                choice = int(input("Select An Option :"))
                if choice == 1:
                    binary_write()
                elif choice == 2:
                    read_binary()
                elif choice == 3:
                    binary_append()
                elif choice == 4:
                    break
            except Exception as e:
                print(e)

    binary_menu()

#main menu for user interaction

def main_menu_file_operations():


    #exit block
    def menu_exit():
        while True:
            print("Are You Sure ? (yes/no) \n")
            try:
                confirmation = input("")
                if confirmation == "yes":
                    sys.exit()
                elif confirmation == "no":
                    main_menu_file_operations()
                else:
                    print("Invalid Input!!!")

            except Exception as e:
                print(e)
    while True:
        print("***FILE FUNCTION MAIN MENU*** \n 1.TEXT \n 2.BINARY \n 3.EXIT")
        try:
            CHOICE = int(input("Select A Option :"))
            if CHOICE == 1:
                text_file_operation()
            elif CHOICE == 2:
                bianry_file_operations()
            elif CHOICE == 3:
                menu_exit()
        except Exception as e :
            print(e)

#call function
            
main_menu_file_operations()

