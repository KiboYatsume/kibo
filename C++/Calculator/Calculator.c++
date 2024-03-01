#include <iostream>
#include <cmath>
#include <string>
#include <cctype>

float add(float a, float b) {
    return a + b;
}

float subtract(float a, float b) {
    return a - b;
}

float multiplie(float a, float b) {
    return a * b;
}

float division(float a, float b) {
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

        std::cout << "\n***Calculator Menu*** \n";
        std::cout << "1.Addition\n";
        std::cout << "2.Subtraction\n";
        std::cout << "3.Multiplication\n";
        std::cout << "4.Division\n";
        std::cout << "5.Power\n";
        std::cout << "6.Factorial\n";
        std::cout << "7.Percentage\n";
        std::cout << "8.Exit\n";

        std::cout << "Select an option:";
        std::cin >> choice;

        if (choice == 1) {
            float a, b;
            std::cout << "Enter a number:";
            std::cin >> a;

            std::cout << "Enter a number to be added to:";
            std::cin >> b;

            std::cout << "The Result is :" << add(a, b);
        }

        if (choice == 2) {
            float a, b;
            std::cout << "Enter a number:";
            std::cin >> a;

            std::cout << "Enter a number to be subtracted from :";
            std::cin >> b;

            std::cout << "The Result is :" << subtract(a, b);
        }
        if (choice == 3) {
            float a, b;
            std::cout << "Enter a number:";
            std::cin >> a;

            std::cout << "Enter a number to be multiplied to:";
            std::cin >> b;

            std::cout << "The Result is :" << multiplie(a, b);
        }
        if (choice == 4) {
            float a, b;
            std::cout << "Enter a number:";
            std::cin >> a;

            std::cout << "Enter a number to be divided by :";
            std::cin >> b;

            std::cout << "The Result is :" << division(a, b);
        }
        if (choice == 5) {
            float a, b;
            std::cout << "Enter a number:";
            std::cin >> a;

            std::cout << "Enter a power :";
            std::cin >> b;

            std::cout << "The Result is :" << power(a, b);
        }
        if (choice == 6) {
            int x;
            std::cout << "Enter a number:";
            std::cin >> x;

            std::cout << "The Result is :" << factorial(x);
        }
        if (choice == 7) {
            float a, b;
            std::cout << "Enter a number (full portion):";
            std::cin >> a;

            std::cout << "Enter a number (measuring amount):";
            std::cin >> b;

            std::cout << "The Result is :" << percentage(a, b);
        }
        if (choice == 8) {
            std::string confirm;

            std::cout << "Are you sure (yes/no) :";
            std::cin >> confirm;

            // Convert confirm to lowercase
            for (char &c : confirm) {
                c = std::tolower(c);
            }

            if (confirm == "yes") {
                return 0;
            } else {
                continue;
            }
        }
    }
}
