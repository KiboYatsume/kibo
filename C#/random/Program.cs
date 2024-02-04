using System;
class Program
{
    static void Main(string[] args)
    {
        Random random = new Random();
        int randNumber = random.Next(1, 101);
        Console.WriteLine("Random Number : " + randNumber);
    }
}