class Program
{
    static void Main()
    {
        List<int> passcode = new List<int>();
        passcode.Add(589345);

        List<string> UserData = new List<string>();
        UserData.Add("raj");
        UserData.Add("ajay");
        UserData.Add("mehak");
        UserData.Add("kushi");


        Console.WriteLine("Enter UserName");
        string UserName = Console.ReadLine();
        string UserLower = UserName.ToLower();
        if (UserData.Contains(UserLower))
        {
            Console.WriteLine("User Exist !");
            Console.WriteLine("Enter Password");

            int password = int.Parse(Console.ReadLine());

            if (passcode.Contains(password))
            {
                Console.WriteLine("Welcome ! " + UserLower);

            }
            else
            {
                Console.WriteLine("Incorrect Password");
            }
        }
        else
        {
            Console.WriteLine("User Does Not Exist");
        }



    }
}