using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("What is your age ?");
        int age = int.Parse(Console.ReadLine()); 

        if (age > 17) 
        {
            Console.WriteLine("You can vote!");
        }
        else
        {
            Console.WriteLine("You cannot vote!");
        }
    }
}
