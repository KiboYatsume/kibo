using System;

class Program
{
    static void Main(string[] args)
    {
        PasswordMenu();
    }

    static void PasswordMenu()
    {
        while (true)
        {
            Console.WriteLine("***Password Menu***");
            Console.WriteLine("1. Pincode");
            Console.WriteLine("2. Alphanumeric");
            Console.WriteLine("3. Alphabetic");
            Console.WriteLine("4. Alphabetic LowerCase");
            Console.WriteLine("5. Alphabetic UpperCase");
            Console.WriteLine("6. Exit");

            Console.Write("Enter Your Choice: ");

            int choice;
            if (!int.TryParse(Console.ReadLine(), out choice))
            {
                Console.WriteLine("Invalid Input! Enter A Number!");
                continue;
            }

            switch (choice)
            {
                case 1:
                    Console.Write("Enter Password Length: ");
                    int length1;
                    if (!int.TryParse(Console.ReadLine(), out length1))
                    {
                        Console.WriteLine("Invalid Input! Enter A Number!");
                        continue;
                    }
                    string generatedPassword1 = PasswordGenerator(length1, "0123456789");
                    Console.WriteLine("The Generated Password is: " + generatedPassword1);
                    break;
                case 2:
                    Console.Write("Enter Password Length: ");
                    int length2;
                    if (!int.TryParse(Console.ReadLine(), out length2))
                    {
                        Console.WriteLine("Invalid Input! Enter A Number!");
                        continue;
                    }
                    string generatedPassword2 = PasswordGenerator(length2, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()");
                    Console.WriteLine("The Generated Password is: " + generatedPassword2);
                    break;
                case 3:
                    Console.Write("Enter Password Length: ");
                    int length3;
                    if (!int.TryParse(Console.ReadLine(), out length3))
                    {
                        Console.WriteLine("Invalid Input! Enter A Number!");
                        continue;
                    }
                    string generatedPassword3 = PasswordGenerator(length3, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ");
                    Console.WriteLine("The Generated Password is: " + generatedPassword3);
                    break;
                case 4:
                    Console.Write("Enter Password Length: ");
                    int length4;
                    if (!int.TryParse(Console.ReadLine(), out length4))
                    {
                        Console.WriteLine("Invalid Input! Enter A Number!");
                        continue;
                    }
                    string generatedPassword4 = PasswordGenerator(length4, "abcdefghijklmnopqrstuvwxyz");
                    Console.WriteLine("The Generated Password is: " + generatedPassword4);
                    break;
                case 5:
                    Console.Write("Enter Password Length: ");
                    int length5;
                    if (!int.TryParse(Console.ReadLine(), out length5))
                    {
                        Console.WriteLine("Invalid Input! Enter A Number!");
                        continue;
                    }
                    string generatedPassword5 = PasswordGenerator(length5, "ABCDEFGHIJKLMNOPQRSTUVWXYZ");
                    Console.WriteLine("The Generated Password is: " + generatedPassword5);
                    break;
                case 6:
                    Console.WriteLine("Are you sure ?(yes/no)");
                    string confirmation = Console.ReadLine();
                    switch (confirmation)
                    {
                        case "yes":
                            Environment.Exit(0);
                            break;
                        case "no":
                            continue;
                        default:
                            Console.WriteLine("Invalid input. Please enter 'yes' or 'no'.");
                            break;
                    }
                    break;
                default:
                    Console.WriteLine("Invalid option. Please try again.");
                    break;
            }
        }
    }

    static string PasswordGenerator(int length, string characters)
    {
        Random random = new Random();
        char[] password = new char[length];
        for (int i = 0; i < length; i++)
        {
            password[i] = characters[random.Next(characters.Length)];
        }
        return new string(password);
    }
}
