using System;
using System.Collections.Generic;

class Mookie
{
    static Dictionary<string, string> memory = new Dictionary<string, string>();

    static void Main(string[] args)
    {
        Console.WriteLine("Welcome, I am Mookie ChatBot");
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
        List<string> greetings = new List<string>
        {
            "Hi there!",
            "Hello!",
            "Hey!",
            "What's up?",
            "Yo!"
        };

        List<string> how_are_you = new List<string>
        {
            "I'm just a bot, but thanks for asking!",
            "I am doing great! Thank you!",
            "My code is running great so I am fine ^^",
            "I am a program, but sweet of you to ask still",
            "I am fine thanks for asking!"
        };
        List<string> thankyou_response = new List<string>
        {
            "np!",
            "Welcome!",
            "No Problem!",
            "Your Welcome",
            "Mention Not!"
        };
        if (userMessage.Contains("hello", StringComparison.OrdinalIgnoreCase) ||
            userMessage.Contains("hi", StringComparison.OrdinalIgnoreCase) ||
            userMessage.Contains("yoohoo", StringComparison.OrdinalIgnoreCase) ||
            userMessage.Contains("hey", StringComparison.OrdinalIgnoreCase))
        {
            Random random = new Random();
            int index = random.Next(greetings.Count);
            return greetings[index];
        }
        else if (userMessage.Contains("how are you", StringComparison.OrdinalIgnoreCase) ||
                 userMessage.Contains("how you doing", StringComparison.OrdinalIgnoreCase) ||
                 userMessage.Contains("hru", StringComparison.OrdinalIgnoreCase) ||
                 userMessage.Contains("how are you doing", StringComparison.OrdinalIgnoreCase) ||
                 userMessage.Contains("what's up", StringComparison.OrdinalIgnoreCase) ||
                 userMessage.Contains("how you doin", StringComparison.OrdinalIgnoreCase))
        {
            Random random = new Random();
            int index = random.Next(how_are_you.Count);
            return how_are_you[index];
        }
        else if (userMessage.Contains("bye", StringComparison.OrdinalIgnoreCase))
        {
            return "Goodbye! Have a great day!";
        }
        else if (userMessage.StartsWith("remember my ", StringComparison.OrdinalIgnoreCase))
        {
            // Extract the information to remember from the user's message
            string[] parts = userMessage.Split("my ", StringSplitOptions.RemoveEmptyEntries);
            if (parts.Length == 2)
            {
                string[] info = parts[1].Split(" is ");
                if (info.Length == 2)
                {
                    string key = info[0].Trim();
                    string value = info[1].Trim();
                    memory[key] = value;
                    return $"Okay, I'll remember that {key} is {value}.";
                }
            }
            return "Sorry, I couldn't understand the information to remember.";
        }
        else if (userMessage.Contains("who am i", StringComparison.OrdinalIgnoreCase))
        {
            if (memory.ContainsKey("name"))
            {
                return $"You are {memory["name"]}!";
            }
            else
            {
                return "I'm sorry, I don't remember your name.";
            }
        }

        else if (userMessage.Contains("thank you!", StringComparison.OrdinalIgnoreCase) ||
                 userMessage.Contains("ty", StringComparison.OrdinalIgnoreCase) ||
                 userMessage.Contains("tysm", StringComparison.OrdinalIgnoreCase) ||
                 userMessage.Contains("thanks", StringComparison.OrdinalIgnoreCase))
        {
            Random random = new Random();
            int index = random.Next(thankyou_response.Count);
            return thankyou_response[index];
        }
        else
        {
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
