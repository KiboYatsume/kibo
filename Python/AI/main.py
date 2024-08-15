import random
import json
import sys
import ollama
import hashlib


def load_json(file_path):
    """Load JSON data from a file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: Credential file not found.")
        sys.exit()
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON.")
        sys.exit()

def find_user(users, name, password):
    """Find a user by name and password in the list of users."""
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    for user in users:
        if user["Name"].lower() == name.lower() and user["password"] == password_hash:
            return user
    return None

def admin_and_creator_verification(users, name):
    """Verify if the user is an admin or creator."""
    user = find_user(users, name, input("Please enter your password: "))
    if user and (user.get("is_admin") or user.get("is_creator")):
        print("Please enter the security pin:")
        entered_pin = input("")
        stored_hash = "6b760d71ea03f1e71b8e3b56a8ba9548dc10a2f2997ff9773f58569e2f39ba8f"
        is_valid = stored_hash == hashlib.sha256(entered_pin.encode('utf-8')).hexdigest()
        if is_valid:
            print("User verified!")
            return user
        else:
            print("Authentication failed!")
    return None

def save_json(file_path, users):
    with open(file_path, 'w') as file:
        json.dump(users, file, indent=4)

def add_user(file_path):
    users = load_json(file_path)  # Load existing users
    new_name = input("Enter your name: ")
    
    # Check if the user already exists
    if find_user(users, new_name, ""):
        print("User already exists!")
        return
    
    # Prompt for additional user details
    new_gender = input("Enter you gender: ")
    new_age = input("Enter your age: ")
    is_student = input("Are you a student? (true/false): ").lower() == 'true'
    is_creator = input("Are you a creator? (true/false): ").lower() == 'true'
    is_admin =   input("Are you a admin? (true/false): ").lower() == 'true'
    new_password = input("Enter your password: ")
    password_hash = hashlib.sha256(new_password.encode('utf-8')).hexdigest()
    new_course = input("Enter your course: ")
    
    new_user = {
        "Name": new_name,
        "Gender" : new_gender,
        "Age": new_age,
        "is_student": is_student,
        "is_creator": is_creator,
        "is_admin" : is_admin,
        "password": password_hash,
        "course": new_course
    }
    
    users.append(new_user)  # Add the new user to the list
    save_json(file_path, users)  # Save the updated list
    print(f"User {new_name} added successfully!")


def get_response(message):
    stream = ollama.chat(
        model='llama3.1',
        messages=[{'role': 'user', 'content': message}],
        stream=True,
    )
    
    response = ""
    for chunk in stream:
        response += chunk['message']['content']  # Accessing the dictionary correctly
    
    return response


def chatbot():
    while True:
        user_message = input("You: ")
        message = user_message.lower()
        response = get_response(message)
        print("Mookie: " + response)
        if message == "bye":
            break

def login_as_existing():
    file_path = "credential.json"
    users = load_json(file_path)
    print("Mookie: Hello, I am Mookie. Please enter your name and password...")
    user_name = input("You: ")
    user_password = input("You: ")
    user = find_user(users, user_name, user_password)
    if user:
        print(f"Welcome {user['Name']}, I am Mookie. How may I assist you?")
        chatbot()
    else:
        print("Mookie: Sorry, I couldn't find your profile.")

def new_user():
    file_path = "credential.json"
    users = load_json(file_path)
    print("Verification required! Enter UserName...")
    user_name = input("You: ")
    verified_user = admin_and_creator_verification(users, user_name)
    if verified_user:
        print(f"Access granted for {user_name}. You can now add a new user.")
        add_user(file_path)
    else:
        print("Access denied or user not found.")

def confirm_exit():
    print("Are you sure (yes/no)?")
    confirmation = input("")
    if confirmation.lower() == "yes": 
        print("Exiting the portal. Goodbye!")
        sys.exit()
    else : 
            pass


def user_login_portal():
    """Main login portal for users."""
    file_path = "credential.json"
    users = load_json(file_path)

    while True:
        print("*** User Login Portal ***")
        print("1. Enter as existing user")
        print("2. Add a new user")
        print("3. Exit")
        try:
            user_input_handler = int(input("Enter your choice: "))
            if user_input_handler == 1:
                login_as_existing()
            elif user_input_handler == 2:
                new_user()
            elif user_input_handler == 3:
                while True:
                    confirm_exit()
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    user_login_portal()
