using System;

class Program
{
    static void Main(string[] args)
    {
        int choice;

        do
        {
            DisplayMenu();
            Console.WriteLine("Enter An Option:");
            if (!int.TryParse(Console.ReadLine(), out choice))
            {
                Console.WriteLine("Invaild Input! Please Enter A Number!");
                continue;
            }
            switch (choice)
            {
                case 1:
                    Console.WriteLine("User Selected Option 1");
                    break;
                case 2:
                    Console.WriteLine("User Selected Option 2");
                    break;
                case 3:
                    Console.WriteLine("User Selected Option 3");
                    break;
                case 4:
                    Console.WriteLine("User Selected Option 4 \n Exiting Program");
                    return;
                default:
                    Console.WriteLine("Invalid Input ! Please Select An Valid Option");
                    break;
            }
        } while (choice != 4);
    }
    static void DisplayMenu()
    {
        Console.WriteLine("***Menu***");
        Console.WriteLine("1. Option 1");
        Console.WriteLine("2. Option 2");
        Console.WriteLine("3. Option 3");
        Console.WriteLine("4. Exit");
    }
}