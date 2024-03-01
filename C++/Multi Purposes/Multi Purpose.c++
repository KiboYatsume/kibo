#include <iostream>
#include <cmath>
#include <string>
#include <cctype>
#include <cstdlib>
#include <ctime>

using namespace std;

// Function to generate password
string generatePassword(int length, bool useDigits, bool useSymbols) {
    const string uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const string lowercase = "abcdefghijklmnopqrstuvwxyz";
    const string digits = "0123456789";
    const string symbols = "!@#$%^&*()-_+=<>?";

    string charPool = uppercase + lowercase;
    if (useDigits) charPool += digits;
    if (useSymbols) charPool += symbols;

    string password = "";
    srand(time(0));
    for (int i = 0; i < length; ++i) {
        password += charPool[rand() % charPool.length()];
    }
    return password;
}

// Calculator functions
float add(float a, float b) {
    return a + b;
}

float subtract(float a, float b) {
    return a - b;
}

float multiply(float a, float b) {
    return a * b;
}

float divide(float a, float b) {
    return a / b;
}

float power(float a, float b) {
    return std::pow(a, b);
}

int factorial(int x) {
    if (x == 0 || x == 1) {
        return 1;
    } else {
        int result = 1;
        for (int i = 2; i <= x; ++i) {
            result *= i;
        }
        return result;
    }
}

float percentage(float a, float b) {
    return (b / a) * 100.0f;
}

int main() {
    while (true) {
        int choice;

        cout << "\n***Main Menu***\n";
        cout << "1. Password Generator\n";
        cout << "2. Calculator\n";
        cout << "3. Exit\n";

        cout << "Select an option:";
        cin >> choice;

        if (choice == 1) {
            int length;
            bool useDigits, useSymbols;

            cout << "Enter password length: ";
            cin >> length;

            cout << "Include digits? (1 for yes, 0 for no): ";
            cin >> useDigits;

            cout << "Include symbols? (1 for yes, 0 for no): ";
            cin >> useSymbols;

            string password = generatePassword(length, useDigits, useSymbols);
            cout << "Generated Password: " << password << endl;
        } else if (choice == 2) {
            // Calculator menu
            while (true) {
                int operationChoice;

                cout << "\n***Calculator Menu***\n";
                cout << "1. Addition\n";
                cout << "2. Subtraction\n";
                cout << "3. Multiplication\n";
                cout << "4. Division\n";
                cout << "5. Power\n";
                cout << "6. Factorial\n";
                cout << "7. Percentage\n";
                cout << "8. Back to Main Menu\n";

                cout << "Select an operation:";
                cin >> operationChoice;

                if (operationChoice == 8) {
                    break; // Exit calculator menu and go back to main menu
                }

                float a, b;
                cout << "Enter the first number:";
                cin >> a;

                if (operationChoice != 6) {
                    cout << "Enter the second number:";
                    cin >> b;
                }

                switch (operationChoice) {
                    case 1:
                        cout << "Result: " << add(a, b) << endl;
                        break;
                    case 2:
                        cout << "Result: " << subtract(a, b) << endl;
                        break;
                    case 3:
                        cout << "Result: " << multiply(a, b) << endl;
                        break;
                    case 4:
                        cout << "Result: " << divide(a, b) << endl;
                        break;
                    case 5:
                        cout << "Result: " << power(a, b) << endl;
                        break;
                    case 6:
                        cout << "Result: " << factorial(a) << endl;
                        break;
                    case 7:
                        cout << "Result: " << percentage(a, b) << endl;
                        break;
                    default:
                        cout << "Invalid operation choice.\n";
                }
            }
        } else if (choice == 3) {
            string confirm;

            cout << "Are you sure you want to exit (yes/no):";
            cin >> confirm;

            // Convert confirm to lowercase
            for (char &c : confirm) {
                c = std::tolower(c);
            }

            if (confirm == "yes") {
                break; // Exit the program
            }
        } else {
            cout << "Invalid choice. Please try again.\n";
        }
    }

    return 0;
}
