using System;
using System.Collections.Generic;

class Mookie
{
    static Dictionary<string, string> memory = new Dictionary<string, string>();

    static void Main(string[] args)
    {
        Console.WriteLine("Welcome , I am Mookie ChatBot");
        StartChat();
    }

    static void StartChat()
    {
        string userMessage;
        do
        {
            Console.Write("You: ");
            userMessage = Console.ReadLine();
            string response = GetResponse(userMessage);
            Console.WriteLine("Mookie: " + response);
        } while (!userMessage.Equals("bye", StringComparison.OrdinalIgnoreCase));
    }

    static string GetResponse(string userMessage)
    {
        if (userMessage.Contains("hello", StringComparison.OrdinalIgnoreCase))
        {
            return "Hi there!";
        }
        else if (userMessage.Contains("how are you", StringComparison.OrdinalIgnoreCase))
        {
            return "I'm just a bot, but thanks for asking!";
        }
        else if (userMessage.Contains("bye", StringComparison.OrdinalIgnoreCase))
        {
            return "Goodbye! Have a great day!";
        }
        else if (userMessage.StartsWith("remember my name is ", StringComparison.OrdinalIgnoreCase))
        {
            // Extract the name from the user's message
            string name = userMessage.Substring("remember my name is ".Length);
            memory["name"] = name;
            return "Okay, I'll remember your name as " + name + ".";
        }
        else if (userMessage.Equals("what's my name", StringComparison.OrdinalIgnoreCase))
        {
            if (memory.ContainsKey("name"))
            {
                return "Your name is " + memory["name"] + ".";
            }
            else
            {
                return "I'm sorry, I don't remember your name.";
            }
        }
        else
        {
            // Attempt to parse and calculate the expression
            try
            {
                string[] parts = userMessage.Split('+', '-', '*', '/');
                if (parts.Length == 2)
                {
                    double num1 = Convert.ToDouble(parts[0]);
                    double num2 = Convert.ToDouble(parts[1]);
                    double result = 0;

                    if (userMessage.Contains("+"))
                    {
                        result = num1 + num2;
                    }
                    else if (userMessage.Contains("-"))
                    {
                        result = num1 - num2;
                    }
                    else if (userMessage.Contains("*"))
                    {
                        result = num1 * num2;
                    }
                    else if (userMessage.Contains("/"))
                    {
                        if (num2 != 0)
                        {
                            result = num1 / num2;
                        }
                        else
                        {
                            return "Cannot divide by zero!";
                        }
                    }
                    return "The result is " + result.ToString();
                }
                else
                {
                    return "Invalid input format!";
                }
            }
            catch (FormatException)
            {
                return "Invalid input format!";
            }
        }
    }
}
