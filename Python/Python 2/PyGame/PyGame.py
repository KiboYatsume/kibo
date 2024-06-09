import secrets as r
import sys as s

Starts = [
    "If you look closely {} is {}",
    "The universe is {} who is {}",
    "A white van full of {} is {}",
    "The man who is {} should be {}",
    "An orphan with {} can be {}"
]

Mid = [
    "a big fat dog",
    "a fucking crackhead",
    "a Shark"
]

End = [
    "Morbidly obese",
    "snorting shit",
    "going to germany",
    "overdosing on brownies"
]

def GameLogic():
    while True:
        print("***Welcome To 'THE GAME'***")
        try:
            userdraw = int(input("Draw a number between 1 to 5 (enter '000' to exit): "))
            if userdraw in [1, 2, 3, 4, 5]:
                print(r.choice(Starts).format(r.choice(Mid), r.choice(End)))
            elif userdraw == 000:
                s.exit(0)
            else:
                print("Out of Draw")
        except ValueError as e:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print("An error occurred:", e)

GameLogic()
