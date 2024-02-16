using System;
using System.Net;
using Newtonsoft.Json;

class Program
{
    static void Main()
    {
        Console.WriteLine("Ask me anything!");
        string userInput = Console.ReadLine();

        string topic = ExtractTopic(userInput);
        string summary = GetSummary(topic);
        Console.WriteLine(summary);
    }

    static string ExtractTopic(string userInput)
    {
        // Remove "what/who is" from the user input to get the topic
        string[] words = userInput.Split(' ');
        string topic = string.Join(' ', words[2..]); // Get all words after the third one
        return topic;
    }

    static string GetSummary(string topic)
    {
        string apiUrl = $"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}";

        try
        {
            using (WebClient client = new WebClient())
            {
                string json = client.DownloadString(apiUrl);
                dynamic data = JsonConvert.DeserializeObject(json);
                return data.extract;
            }
        }
        catch (WebException ex)
        {
            // Handle error (e.g., topic not found)
            return "Error: Topic not found.";
        }
    }
}
