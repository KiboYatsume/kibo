Questions = [
    ("what is the weakest fundamental force ?", "gravity"),
    ("Name the largest country", "russia"),
    ("Smallest value of the cosine function", "-1"),
    ("The sun rises from the ?", "east"),
    ("Fructose is obtained from  ?", "glucose"),
    ("What is the chemical symbol for gold?", "Au"),
    ("Who wrote 'Romeo and Juliet'?", "William Shakespeare"),
    ("What is the capital of France?", "Paris"),
    ("What is the chemical formula for water?", "H2O"),
    ("What is the largest mammal in the world?", "blue whale"),
]

def ask():
    points = 0
    for question, answer in Questions:
        user_input = input(question + "\n")
        if user_input.strip().lower() == answer.lower():
            print("BINGO!")
            points += 1
        else:
            print("aww that's not right!")
    
    name = input("Enter your name: ")
    
    if points <= 5:
        print(f"Nice try, {name}!")
    elif points <= 8:
        print(f"Congrats, {name}! Near perfect!")
    else:
        print(f"AMAZING WORK, {name}! Perfect score!")

if __name__ == '__main__':
    ask()
