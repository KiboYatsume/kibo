import string
import random 
import os
import importlib
import subprocess
import mysql.connector
import Friday
def install_module(module_name):
    try:
        importlib.import_module(module_name)
    except ImportError:
        print(f"{module_name} is not installed. Installing...")
        try:
            subprocess.call(['pip', 'install', module_name])
            print(f"{module_name} has been successfully installed.")
        except Exception as e:
            print(f"Error installing {module_name}: {e}")
required_modules = [
    'sympy', '--upgrade setuptools', 'tk', 'numpy', 'googletrans==4.0.0-rc1', 'pymysql', 'pycryptodome',
    'mysql-connector-python', '--update futures', 'matplotlib', 'pygame', '--upgrade --force-reinstall --no-cache-dir PyDictionary',
    'gTTS', 'pyjokes', 'subprocess', 'speech_recognition', 'pyttsx3', 'wikipedia', 'webbrowser', 'smtplib']

for module in required_modules:
    install_module(module)
import sympy
import turtle
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import pickle
from collections import Counter
import math
from sympy import rad
import googletrans
from googletrans import Translator
import sympy as sp
import httpcore
import pymysql
import matplotlib.pyplot as plt
import tkinter as tf
from tkinter import messagebox,simpledialog
from tkinter import *
from PyDictionary import PyDictionary
import pygame
import time
def snake_game():
    snake_speed = 15
    window_x, window_y = 720, 480
    black, white, red, green, blue = pygame.Color(0, 0, 0), pygame.Color(255, 255, 255), pygame.Color(255, 0, 0), pygame.Color(0, 255, 0), pygame.Color(0, 0, 255)

    pygame.init()
    pygame.display.set_caption('i hate snakeu')
    game_window = pygame.display.set_mode((window_x, window_y))
    fps = pygame.time.Clock()

    snake_position = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
    fruit_position = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
    fruit_spawn = True

    direction = 'RIGHT'
    change_to = direction
    score = 0

    def show_score(choice, color, font, size):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render('Score : ' + str(score), True, color)
        score_rect = score_surface.get_rect()
        game_window.blit(score_surface, score_rect)

    def game_over():
        my_font = pygame.font.SysFont('times new roman', 50)
        game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (window_x/2, window_y/4)
        game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
        quit()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'

        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        snake_body.insert(0, list(snake_position))
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 10
            fruit_spawn = False
        else:
            snake_body.pop()

        if not fruit_spawn:
            fruit_position = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]

        fruit_spawn = True
        game_window.fill(black)

        for pos in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

        if snake_position[0] < 0 or snake_position[0] > window_x-10:
            game_over()
        if snake_position[1] < 0 or snake_position[1] > window_y-10:
            game_over()

        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over()

        show_score(1, white, 'times new roman', 20)
        pygame.display.update()
        fps.tick(snake_speed)
def dictionary():
    while True:
        def get_definition(word):
            dictionary = PyDictionary()
            definition = dictionary.meaning(word)
            if definition:
                return definition
            return f"Definition not found for '{word}'."
        def get_meaning():
            user_word = input("Enter a word (or type 'dic.close' to exit): ")
            if user_word == 'dic.close':
                return False
            result = get_definition(user_word)
            if isinstance(result, dict):
                print(f"Definitions for '{user_word}':")
                for pos, meanings in result.items():
                    print(f"{pos.capitalize()}: {', '.join(meanings)}")
            else:
                print(result)
            return True
        if not get_meaning():
            break
translator = Translator()
def Graph_SQL():
    while True:
        try:
            password = input("Please enter your MySQL password (type 'exit' to go back to the main menu): ")
            if password.lower() == 'exit':
                return
            database = input("Enter the name of the database in question:")
            field1 = input("Enter the field name:")
            field2 = input("Enter the other field name:")
            table = input("Enter the table name:")
            name = input("Enter name for graph")
            query = "SELECT " + field1 + "," + field2 + " FROM " + table + ";"
            connection = pymysql.connect(host="localhost", user="root", password=password, database=database)
            cursor = connection.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            field1_data = []
            field2_data = []
            for row in results:
                field1_data.append(row[0])
                field2_data.append(row[1])
            plt.figure(figsize=(10, 6))
            plt.bar(field1_data, field2_data, color='purple')
            plt.xlabel(field1)
            plt.ylabel(field2)
            plt.title(name)
            plt.xticks(rotation=45)
            plt.show()
            cursor.close()
            connection.close()
        except pymysql.err.OperationalError:
            print("Incorrect Password")
def sql():
    while True:
        try:
            password = input("Enter the password (type 'exit' to go back to the main menu): ")
            if password.lower() == 'exit':
                break
            mydb = mysql.connector.connect(host="localhost", user="root", password=password)
            cursor = mydb.cursor()
            result = None  
            while True:
                command = input("Input SQL command (type 'exit' to go back to the main menu): ")
                if command.lower() == 'exit':
                    break  
                cursor.execute(command)
                if command.strip().lower().startswith("select"):
                    result = cursor.fetchall()
            if result:
                for data in result:
                    print(data)
            mydb.commit()
            cursor.close()
            mydb.close()
        except mysql.connector.errors.ProgrammingError:
            print("Incorrect Password")
def SQL_MENU():
    while True:
        try:
            print("***SQL MENU*** \n1.SQL COMMAND LINE \n2.Graph \n3.EXIT")
            choice = int(input("select an option :"))
            if choice == 1:
                sql()
            if choice == 2:
                Graph_SQL()
            if choice == 3:
                confirmation = input("are you sure? (yes/no)\n")
                if confirmation.lower() == "yes":
                    break
        except ValueError:
            print('Invalid Input!!')
def definite_integration():
    var = input("Enter the variable of integration: ")
    function_str = input("Enter the function to integrate: ")
    lower_limit = float(input("Enter the lower limit of integration: "))
    upper_limit = float(input("Enter the upper limit of integration: "))
    x = sp.symbols(var)
    function = sp.sympify(function_str)
    integral = sp.integrate(function, (x, lower_limit, upper_limit))
    print(f"The definite integral of {function} from {lower_limit} to {upper_limit} with respect to {var} is: {integral}")
def integrate_function():
    var = input("Enter the variable to integrate with respect to: ")
    function_str = input("Enter the desired function: ")
    x = sp.symbols(var)
    function = sp.sympify(function_str)
    integral = sp.integrate(function, x)
    print("The integral of", function, "with respect to", var, "is:", integral,"+ C")
def differentiate_function():
    var = input("Enter the variable to differentiate with respect to: ")
    function_str = input("Enter the desired function: ")
    x = sp.symbols(var)
    function = sp.sympify(function_str)
    derivative = sp.diff(function, x)  
    print("The derivative of", function, "with respect to", var, "is:", derivative)
def Degree_To_Radian():
    Degrees = int(input("Enter the degree of which you need the value of in radian :"))
    angle_degrees = Degrees
    angle_radians = rad(angle_degrees)
    print(f"{angle_degrees} degrees is equal to {angle_radians} radians.")
def Sin():
    Degrees = int(input("Enter the degree of which you need the value of :"))
    print("The value of Sin on",Degrees,"Degrees is:",math.sin(Degrees))
def Cos():
     Degrees = int(input("Enter the degree of which you need the value of :"))
     print("The value of Cos on",Degrees,"Degrees is:",math.cos(Degrees))
def Tan():
    Degrees = int(input("Enter the degree of which you need the value of :"))
    print("The value of Tan on",Degrees,"Degrees is:",math.tan(Degrees))
def Cosec():
    Degrees = int(input("Enter the degree of which you need the value of :"))
    print("The value of Cosec on",Degrees,"Degrees is:",math.cosec(Degrees))
def Sec():
    Degrees = int(input("Enter the degree of which you need the value of :"))
    print("The value of Sec on",Degrees,"Degrees is:",math.sec(Degrees))
def Cot():
    Degrees = int(input("Enter the degree of which you need the value of :"))
    print("The value of Cot on",Degrees,"Degrees is:",math.cot(Degrees))
def Function_Value():
    while True :
        print("***Trigonomteric Value Calculator Functions***\n1.Sin\n2.Cos\n3.Tan\n4.Cosec\n5.Sec\n6.Cot\n7.Exit")
        Choice = input("Select The Desired Function:")
        if Choice == "1":
            Sin()
        elif Choice == "2":
            Cos()
        elif Choice == "3":
            Tan()
        elif Choice == "4":
            Cosec()
        elif Choice == "5":
            Sec()
        elif Choice == "6":
            Cot()
        elif Choice == "7":
            confirmation = input("Are You Sure (yes/no):")
            if confirmation.lower()=="yes":
                break
def Trigonometeric_Functions():
    while True:
        print("***Trigonometry Function Menu*** \n1.Value Calculator\n2.Degree To Radian\n3.Exit")
        Choice = input("Select An Option:")
        if Choice =="1":
          Function_Value()
        if Choice == "2":
            Degree_To_Radian()
        if Choice == "3":
            confrimation = input("Are You Sure ? (yes/no) \n")
            if confrimation.lower() == "yes":
                break
def Calculate():
    def addition():
        Result = X+Y
        print (Y,"added to",X,"gives:",Result)
    def subtract():
        Result = X-Y
        print (Y,"Subtracted from",X, "is:",Result)
    def multiplie():
        Result = X*Y
        print (X,"multiplied by",Y,"is:",Result)
    def devide():
        Result = X/Y
        print (X,"devide by",Y,"is:",Result)
    def square():
        Result = X**Y
        print (X,"raised to the power",Y,"is:",Result)
    def percentage():
        Result = X/Y * 100
        print ("The Percentage is:", Result , "%")
    def Factorial():
        Result = math.factorial(X)
        print ("The Factorial of",X,"is:",Result)
    while True:
        print("***Ca1culator Menu***\n 1.Addition\n 2.Subtract\n 3.Multiplie \n 4.Devide \n 5.Square\n 6.Percentage\n 7.Factorial \n 8. Trigonometric Functions\n9.Integrate\n10.Definite Integration\n11.Differentiate\n 12.Exit")
        Choice = input("Select An Option:")
        if Choice == "1":
            X = float(input("ENTER NUMBER:"))
            Y = float(input("ENTER THE NUMBER TO BE ADDED INTO:"))
            addition()
        if Choice == "2":
            X = float(input("ENTER NUMBER TO BE SUBTRACTED FROM:"))
            Y = float(input("ENTER NUMBER TO BE SUBTRACTED:"))
            subtract()
        if Choice == "3":
            X = float(input("ENTER THE NUMBER:"))
            Y = float(input("ENTER THE NUMBER TO BE MULTIPLIED WITH:"))
            multiplie()
        if Choice == "4":
            X = float(input("ENTER DIVIDEND:"))
            Y = float(input("ENTER THE DIVISOR:"))
            devide()
        if Choice == "5":
            X = float(input("ENTER THE NUMBER:"))
            Y = float(input("ENTER IT'S POWER:"))
            square()
        if Choice == "6":
            X = float(input("ENTER PORTION AMOUNT:"))
            Y = float(input("ENTER THE TOTAL AMOUNT:"))
            percentage()
        if Choice == "7":
            X = int(input("ENTER THE NUMBER:"))
            Factorial()
        if Choice == "8":
            Trigonometeric_Functions()
        if Choice == "9":
            integrate_function()
        if Choice == "10":
            definite_integration()
        if Choice == "11":
            differentiate_function()
        if Choice == "12":
            confirmation = input("Are you sure \n")
            if confirmation.lower() == "yes" :
                break
def english_to_japanese():
    english_text = input("Enter the text:")
    janpanese_translation = translator.translate(english_text, src='en',dest='ja')
    print(english_text,"in japanese means:",janpanese_translation.text)
def japanese_to_english():
    japanese_text = input("Enter the text:")
    english_translation = translator.translate(japanese_text, src='ja',dest='en')
    print(japanese_text,"in english means:",english_translation.text)
def english_to_korean():
    english_text = input("Enter the text:")
    korean_translation = translator.translate(english_text, src='en',dest='ko')
    print(english_text,"in korean means:",korean_translation.text)
def korean_to_english():
    korean_text = input("Enter the text:")
    english_translation = translator.translate(korean_text, src='ko',dest='en')
    print( korean_text,"in english means:",english_translation.text)
def english_to_hindi():
    english_text = input("Enter the text:")
    hindi_translation = translator.translate(english_text, src='en',dest='hi')
    print(english_text,"in hindi means:",hindi_translation.text)
def hindi_to_english():
    hindi_text = input("Enter the text:")
    english_translation = translator.translate(hindi_text, src='hi',dest='en')
    print(hindi_text,"in english means:",english_translation.text)
def Translate_Hindi():
    while True:
        print("***Hindi Translator*** \n1.Hindi To English \n2.English To Hindi \n3.Exit")
        Choice = int(input("Select An Option :"))
        if Choice == 1:
             hindi_to_english()
        if Choice == 2:
            english_to_hindi()
        if Choice == 3:
            break
def Translate_Korean():
    while True:
        print("***Korean Translator*** \n1.Korean To English \n2.English To Korean \n3.Exit")
        Choice = int(input("Select An Option :"))
        if Choice == 1:
             korean_to_english()
        if Choice == 2:
            english_to_korean()
        if Choice == 3:
            break
def Translate_Japanese():
    while True:
        print("***Japanese Translator*** \n1.Japanese To English \n2.English To Japanese \n3.Exit")
        Choice = int(input("Select An Option :"))
        if Choice == 1:
             japanese_to_english()
        if Choice == 2:
            english_to_japanese()
        if Choice == 3:
            break
def Translation_Menu():
    while True:
        print("***TRANSLATOR***\n1.Japanese\n2.Korean\n3.Hindi\n4.Exit")
        Choice = int(input("Select An Option:"))
        if Choice == 1:
            Translate_Japanese()
        if Choice == 2:
            Translate_Korean()
        if Choice == 3:
            Translate_Hindi()
        if Choice == 4:
            confirmation = input("Are You Sure ? (yes/no):")
            if confirmation.lower() == "yes":
                break
def Fact_Lab():
    Fact_lib =[
    "Fact 1 : Though less common than earthquakes, the moon actually has moonquakes, too.",
    "Fact 2 : You actually lose a large percentage of your taste buds while on an airplane. This might explain a lot about those less-than-stellar in-flight meals, or why you find yourself craving the saltiest foods while in the sky.",
    "Fact 3 : Although it may sound counterintuitive, your small intestine is actually the largest (internal) organ in your body.",
    "Fact 4 : You probably know that snails are petty slow creatures, but did you know that they also take the longest naps? One nap can last up to three years!",
    "Fact 5 : You may be jealous of a bird's ability to fly, but it may soothe your envy to learn they can't live in space because they need gravity to swallow.",
    "Fact 6 : Bees can sting other bees — usually if they feel threatened or are protecting their territory. In other words, you're not the only one who's scared of getting stung.",
    "Fact 7 : Whether you've seen a tiger in real life or in a photo, you know that they have striped fur. But they actually have striped skin, as well.",
    "Fact 8 : If you're a cat lover, then you may be surprised by this interesting fact: Cats can't taste anything that's sweet. That's probably why they can't get enough of their favorite salty snack.",
    "Fact 9 : Most people know dolphins have incredible sonar abilities. But did you know they were studied as war tools during the Cold War? They really are as smart as people say they are.",
    "Fact 10 : Not only are sea lions totally adorable, but they're also very musical. They are the only animal that can clap to a beat.",
    "Fact 11 : Like humans, koalas actually have unique individual fingerprints. If you place a koala and human finger print side by side, they're actually pretty hard to differentiate. ",
    "Fact 12 : You may know that everyone's fingerprints are different, but did you know that the same is true of everyone's tongue print?",
    "Fact 13 : Your brain uses 10 watts of energy to think, but it can't feel pain. You know what they say: Mind over matter.",
    "Fact 14 : Brendan Fraser almost died while filming The Mummy (he passed out while filming a scene). Pretty scary, right?",
    "Fact 15 : In a group of 23 people, there is a 50% chance that two will share the same birthday.",
    "Fact 16 : Will Ferrell consumed so much sugar while filming Elf that he actually became physically ill. If you've seen the famous spaghetti scene, then you can probably understand why.",
    "Fact 17 : It may feel a lot longer in the moment, but the average person spends two weeks of their life sitting at traffic lights.",
    "Fact 18 : The Hollywood sign in Los Angeles once said Hollywoodland, but was changed in 1949",
    "Fact 19 : The most expensive film ever made was Pirates of the Caribbean: On Stranger Tides, which cost 378 million dollars to create. For reference, the average budget for a big studio movie is around $65 million.",
    "Fact 20 : If E.T. is one of your favorite movies of all time, then you'll be interested to know that someone squished their hands in jelly to make the sound effect for E.T. walking around"
    ]
    print(random.choice(Fact_lib))
def Questions():
    points = 0
    Ans1 = ["Neil A.","Alden Armstrong","Neil Armstrong","Neil Alden Armstrong"]
    Ans2 = ["sun","Sun","SUN"]
    Ans3 = ["Everest","Mt.Everest","Mount Everest"]
    Ans4 = ["moon","MOON","Moon"]
    Ans5 = ["Pluto","pluto","PLUTO"]
    Ans6 =["Homosapiens","HOMOSAPIENS","Homo Sapiens","Homo sapiens","Homo-sapiens","Homo-Sapiens","Homosapien","HOMOSAPIEN","Homo Sapien","Homo sapien","Homo-sapien","Homo-Sapien"]
    Ans7 =["Gravity","gravity","GRAVITY"]
    Ans8 =["mammals","MAMMALS","mammal","MAMMAL"]
    Ans9 =["Aryabhata","Aryabhatt","ARYABHATA","ARYABHATT","aryabhatt","aryabhata"]
    Ans10=["east","East","EAST"]
    while True :
        print("Who was the first man to step on moon ? \n")
        Answer = input("")
        if Answer in Ans1:
            print("CORRECT ANSWER!!!!")
            points +=1
        if Answer not in Ans1:
            print("INCORRECT ANSWER!!!!")
            pass
        while True:
            print("Name the largest star in our so1ar system  \n")
            Answer = input("")
            if Answer in Ans2:
                print("CORRECT ANSWER!!!!")
                points +=1
            if Answer not in Ans2:
                print("INCORRECT ANSWER!!!!")
                pass
            while True:
                print("What's The Highest Mountain Cliff ? \n")
                Answer = input("")
                if Answer in Ans3:
                    points +=1
                    print("CORRECT ANWSER!!!!")
                if Answer not in Ans3:
                    print("INCORRECT ANSWER!!!!")
                    pass
                while True:
                    print("What is the name of earth's the natural satellite ? \n")
                    Answer = input("")
                    if Answer in Ans4:
                        print("CORRECT ANWSER!!!!")
                        points +=1
                    if Answer not in Ans4:
                        print("INCORRECT ANSWER!!!!")
                        pass
                    while True :
                        print("Name The Dwarf Planet In Our Solar System  \n")
                        Answer = input("")
                        if Answer in Ans5 :
                            print("CORRECT ANWSER!!!!")
                            points += 1
                        if Answer not in Ans5 :
                            print("INCORRECT ANSWER!!!!")
                            pass
                        while True :
                            print("What is the scientific name of humans ? \n")
                            Answer = input("")
                            if Answer in Ans6:
                                print("CORRECT ANWSER!!!!")
                                points +=1
                            if Answer not in Ans6:
                                print("INCORRECT ANSWER!!!!")
                                pass
                            while True:
                                print("Name the force which pulls us to the ground \n")
                                Answer = input("")
                                if Answer in Ans7:
                                    print("CORRECT ANWSER!!!!")
                                    points +=1
                                if Answer not in Ans7:
                                    print("INCORRECT ANSWER!!!!")
                                    pass
                                while True:
                                    print("Name the type of animal that milkfeed their babies \n")
                                    Answer = input("")
                                    if Answer in Ans8:
                                        print("CORRECT ANWSER!!!!")
                                        points +=1
                                    if Answer not in Ans8:
                                        print("INCORRECT ANSWER!!!!")
                                        pass
                                    while True:
                                        print("Who disocvered zero ? \n")
                                        Answer = input("")
                                        if Answer in Ans9:
                                             print("CORRECT ANWSER!!!!")
                                             points += 1
                                        if Answer not in Ans9:
                                            print("INCORRECT ANSWER!!!!")
                                            pass
                                        print("From which direction does sun rise from ? \n")
                                        Answer = input("")
                                        if Answer in Ans10:
                                            print("CORRECT ANWSER!!!!")
                                            points += 1
                                        if Answer not in Ans10:
                                            print("INCORRECT ANSWER!!!!")
                                            pass
                                        Name = input("Enter Your First Name :")
                                        while points <=5:
                                            print("Congrats",Name,"You Scored",points,"points out of 10! Nice Try")
                                            return
                                        while points <= 8:
                                            print("Congrats",Name,"You Scored",points,"points out of 10! Great Job!")
                                            return
                                        while points <= 10:
                                            print("Congrats",Name,"You Scored",points,"points out of 10! Perfect!")
                                            return
                    
def Quiz():               
    while True:
        print("***General Know1edge Quiz*** \n1.Start Quiz \n2.Exit")
        Choice = input("Se1ect An Option :")
        if Choice == "2":
            break
        if Choice == "1":
            while True :
                print("***Ru1es*** \n1.This Quiz Has 10 questions \n2.you'll be rewarded 1 point for each correct answer \n3. There's no negative Marking \n4.points system: \n 1-5 points Nice Try \n 6-8 Great Job! \n 9-10 Perfect!!")
                Choice = input("Do you wish to continue (yes/no):")
                if Choice.lower()== "no":
                    break
                if Choice.lower()== "yes":
                    Questions()
                    break
        break
def most_frequently_used_function():
    most_common_function = Counter(function_usage).most_common(1)
    return most_common_function[0][0]
function_usage = {
    "Password Function": 0,
    "Stack Function": 0,
    "Calculator": 0,
    "Encryption": 0,
    "Turtle Graphic": 0,
    "File Function": 0,
    "Quiz" : 0,
    "Fun Fact" : 0,
    "Translator" : 0,
    "SQL" : 0,
    "GUI MENU" : 0,
    "Dictionary" : 0,
    "Snake Game" : 0,
    "Friday" : 0
}
def read_txt():
    File_Name = input("Enter File Name : ")
    File = open(File_Name+".txt","r")
    print(File.read())
def append_text():
    File_Name = input("Enter File Name : ")
    Content = input("Enter Content:")
    File = open(File_Name+".txt","a")
    File.write("\n"+Content)
def write_text():
    File_Name = input("Enter File Name : ")
    Content = input("Enter Content:")
    File = open(File_Name+".txt","w")
    File.write(Content)
def File_Handle_Menu():
    while True:
        print("***File Menu*** \n 1.TEXT FILE \n 2.BINARY FILE \n 3.EXIT")
        Choice = int(input("Select An Option:"))
        if Choice == 1:
            while True:
                print("***TEXT FULE MENU*** \n1.Write(Previous Data Will Be Lost)\n2.Append \n3.Read\n4.Exit")
                Choice = int(input("Select An Option:"))
                if Choice == 1:
                    write_text()
                if Choice == 2:
                    append_text()
                if Choice == 3:
                  read_txt()
                if Choice == 4:
                  confrimation = input("Are You Sure \n")
                  if confrimation == "yes":
                          break
        if Choice == 2:
            while True:
                print("***BINARY FULE MENU*** \n1.Write(Previous Data Will Be Lost)\n2.Append \n3.Read\n4.Exit")
                Choice = int(input("Select An Option:"))
                if Choice == 1:
                    write_binary()
                if Choice == 2:
                    append_binary()
                if Choice == 3:
                  read_binary()
                if Choice == 4:
                  confrimation = input("Are You Sure \n")
                  if confrimation == "yes":
                          break
        if Choice == 3:
            confrimation = input("Are You Sure \n")
            if confrimation == "yes":
                break
class MyClass:
    def __init__(self, value):
        self.value = value
def write_binary():
    File_Name = input("Enter File Name : ")
    Extension = input("Enter The Desired Extension Of The File :")
    Content = input("Enter Content:")
    my_data = MyClass(Content)
    with open(File_Name+"."+Extension, "wb") as f:
        pickle.dump(my_data, f)
def read_binary():
    File_Name = input("Enter File Name : ")
    Extension = input("Enter The Desired Extension Of The File :")
    with open(File_Name + "." + Extension, "rb") as f:
        while True:
            try:
                my_data = pickle.load(f)
                print(my_data.value)
            except EOFError:
                break
def append_binary():
    File_Name = input("Enter File Name : ")
    Extension = input("Enter The Desired Extension Of The File :")
    Content = input("Enter Content:")
    my_data = MyClass(Content)
    with open(File_Name+"."+Extension, "ab") as f:
        pickle.dump(my_data, f)
def Rainbow_spiral():
    l=['red','blue','black','green','black','yellow']
    turtle.speed(1000)
    for i in range(1,400):
        turtle.circle(i/5)
        turtle.right(13)
        if i %10==1:
            turtle.color(random.choice(l))
    for i in range(200):
      for j in range(500):
          pass
      turtle.bye()
def race_simulation():
    g = turtle.Turtle()
    g.speed(10)
    screen = g.screen
    screen.setup(height=1.0, width=1.0)
    screen.bgcolor("green")

    def Track():
        text = "---" * 53
        g.penup()
        g.goto(-315, 200)
        g.pendown()
        g.fd(635)
        g.penup()
        g.goto(-315, 110)
        g.pendown()
        g.fd(635)
        g.penup()
        g.goto(-315, 150)
        g.pendown()
        g.write(text)
        g.hideturtle()

    Track()
    A = turtle.Turtle()
    B = turtle.Turtle()
    A.shape("circle")
    B.shape("square")

    def Positions():
        A.speed(10)
        B.speed(10)
        A.penup()
        A.goto(-315, 180)
        A.pendown()
        B.penup()
        B.goto(-315, 130)
        B.pendown()

    Positions()

    def race():
        while True:
            A_steps = random.randint(1, 10)
            B_steps = random.randint(1, 10)
            A.forward(A_steps)
            A.clear()
            B.forward(B_steps)
            B.clear()
            if A.xcor() >= 300:
                messagebox.showinfo("RESULTS", "Player A Wins !!!")
                break
            if B.xcor() >= 300:
                messagebox.showinfo("RESULTS", "Player B Wins !!!")
                break
    race()
def Turtle_Menu():
    def Square():
        for i in range(4):
            turtle.forward(100)
            turtle.right(90)
        turtle.done()
    def Circle():
        turtle.circle(100,370)
        turtle.done()
    def ChessBoard():
        sc = turtle.Screen()
        pen = turtle.Turtle()

        def draw():
            for i in range(4):
                pen.forward(30)
                pen.left(90)
            pen.forward(30)

        sc.setup(600, 600)
        pen.speed(100)
        for i in range(8):
            pen.up()
            pen.setpos(0, 30 * i)
            pen.down()
            for j in range(8):
                if (i + j) % 2 == 0:
                    col = 'black'
                else:
                    col = 'white'
                pen.fillcolor(col)
                pen.begin_fill()
                draw()
                pen.end_fill()
        pen.hideturtle()
        turtle.done()
    while True:
        print("***Turtle Menu*** \n1.ChessBoard \n2.Circle \n3.Square \n4.RainBow Spiral\n5.Race\n6.Exit")
        Choice = input("Select An Option:")
        if Choice == "1":
            ChessBoard()
        if Choice == "2":
            Circle()
        if Choice == "3":
            Square()
        if Choice == "4":
            Rainbow_spiral()
        if Choice == "5":
            race_simulation()
        if Choice == "6":
            confermation = input("Are You Sure ? \n")
            if confermation.lower() == "yes":
                break
def DECRYPTION():
    encrypted_data = input("Enter the encrypted data: ")
    key = input("Enter the key: ")
    cipher = AES.new(key, AES.MODE_CBC)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    return decrypted_data
def ENCRYPTION():
    message = input("Enter the message to encrypt: ")
    key = input("Enter the key: ")
    encrypted_message = ""
    key_index = 0
    for char in message:
        encrypted_message += chr(ord(char) + ord(key[key_index]))
        key_index = (key_index + 1) % len(key)
    return encrypted_message
def DECRYPT():
    encrypted_message = input("Enter the encrypted message: ")
    key = input("Enter the key: ")
    decrypted_message = ""
    key_index = 0
    for char in encrypted_message:
        decrypted_message += chr(ord(char) - ord(key[key_index]))
        key_index = (key_index + 1) % len(key)
    return decrypted_message
def ENCRYPT():
    try:
        user_input = input("Enter the text to encrypt: ")
        key = os.urandom(32)
        encrypted_data = aes_encrypt(user_input, key)
        print("Key:", key)
        print("Encrypted data:", encrypted_data)
        return encrypted_data, key
    except ValueError:
        print("Invalid input. Please make sure the key is 16, 24, or 32 bytes long.")
def aes_encrypt(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data.encode(), AES.block_size))
    iv = cipher.iv
    return (iv + ct_bytes)

def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encrypted_text += shifted_char.upper() if is_upper else shifted_char
        else:
            encrypted_text += char
    return encrypted_text
def Encryptor():
    while True:
        print("***ENCRYPTION MENU*** \n 1.AES Encryptor Function \n 2.Simple Encryptor \n 3.AES Decryptor \n 4.Simple Decryptor \n 5.Exit")
        Choice  = input("Select An Option:")
        if Choice == "1":
            print(ENCRYPT())
        if Choice == "2":
            print(ENCRYPTION())
        if Choice == "3":
            print(DECRYPTION())
        if Choice == "4":
            print(DECRYPT())
        if Choice == "5":
            Confrimation = input("Are You Sure ? \n")
            if Confrimation.lower() == "yes":
                break
def Stack():
    stack = []
    def push(item):
        stack.append(item)
        print("Element", item, "is inserted successfully into the stack")
    def pop(item):
        if not is_empty():
            popped_item = stack.pop()
            return popped_item
        else:
            return None
    def Display():
        if not is_empty():
            print("stack content is:")
            for item in reversed(stack):
                print(item)
    def is_empty():
        return len(stack) == 0
    while True:
        print("***STACK MENU***")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Exit")
        Choice = input("Enter Your Choice:")
        if Choice == "1":
            element = input("Enter element to PUSH :")
            push(element)
            print(stack)
        if Choice == "2":
            confirmation = input("Are you sure ? \n")
            pop(confirmation)
            print(stack)
        if Choice == "3":
            confirmation = input("do you wanna display the stack ? \n")
            if confirmation == "yes":
                print(stack)
        if Choice == "4":
            confirmation = input("Are you sure ? \n")
            if confirmation.lower() == "yes":
                break
def generate_password(pass_len, chars):
    password = ""
    for i in range(pass_len):
        password += random.choice(chars)
    return password
def main():
    while True:
        print("\n **PASSWORD_MENU** \n 1.Pincode \n 2.Alphanumeric \n 3.Alphabetically \n 4.Lowecase \n 5.Uppercase \n 6.EXIT")
        choice = input("Select an option:")
        if choice == "1":
            pass_len = int(input("Enter the length of your password:"))
            password = generate_password(pass_len, string.digits)
            print("The Generated Password Is:",password)
        elif choice == "2":
            pass_len = int(input("Enter the length of your password:"))
            password = generate_password(pass_len, string.ascii_letters + string.digits)
            print("The Generated Password Is:",password)
        elif choice == "3":
            pass_len = int(input("Enter the length of your password:"))
            password = generate_password(pass_len, string.ascii_letters)
            print("The Generated Password Is:",password)
        elif choice == "4":
            pass_len = int(input("Enter the length of your password:"))
            password = generate_password(pass_len, string.ascii_lowercase)
            print("The Generated Password Is:",password)
        elif choice == "5":
            pass_len = int(input("Enter the length of your password:"))
            password = generate_password(pass_len, string.ascii_uppercase)
            print("The Generated Password Is:",password)
        elif choice == "6":
            confirmation = input("Are you sure?\n")
            if confirmation.lower() == "yes":
                break
def GUI_MENU():
    def Quiz():
        root = tf.Tk()
        root.title("***GUI QUIZ***")
        root.geometry('280x280')
        entry = Entry(root)
        entry.pack()
        LP = tf.Listbox(root)
        LP.insert(1, " 1. Quiz")
        LP.insert(2, "2. Exit")
        LP.place(x='0', y='10')
        entry.place(x='1', y='176')
        def Rules():
                start = tf.simpledialog.askstring("Rules","*THIS IS GENERAL KNOWLEDGE QUIZ \n *THIS QUIZ HAS 10 QUESTIONS \n *EACH CORRECT ANSWER ONE POINT IS REWARDED \n DO YOU WISH TO CONTINUE (yes/no)")
                if start.lower() == 'yes':
                        Questions()
                if start.lower()  == 'no':
                        return
        def Questions():
            points = 0
            Ans1 = ["neil a.","alden armstrong","neil armstrong","neil alden armstrong","armstrong"]
            Ans2 = ["sun"]
            Ans3 = ["everest","mt.everest","mount everest"]
            Ans4 = ["moon"]
            Ans5 = ["pluto"]
            Ans6 =["homosapiens","homosapien"]
            Ans7 =["gravity"]
            Ans8 =["mammals","mammal"]
            Ans9 =["aryabhatt","aryabhata"]
            Ans10=["east"]
            Answer1 = tf.simpledialog.askstring("Question.1", "Who was the first man to step on moon ? ")
            if Answer1.lower() in Ans1:
                messagebox.showinfo("Correct Answer!!!", "hoorah ! that's the correct answer!")
                points += 1
            if Answer1.lower() not in Ans1:
                messagebox.showinfo("Wrong Answer!!!", "Awwh ! that's not the correct answer!")
                pass
            Answer2 = tf.simpledialog.askstring("Question.2", "Name the largest star in our so1ar system ")
            if Answer2.lower() in Ans2:
                messagebox.showinfo("Correct Answer!!!", "hoorah ! that's the correct answer!")
                points += 1
            if Answer2.lower() not in Ans2:
                messagebox.showinfo("Wrong Answer!!!", "Awwh ! that's not the correct answer!")
                pass
            Answer3 = tf.simpledialog.askstring("Question.3", "What's The Highest Mountain Cliff ?")
            if Answer3.lower() in Ans3:
                messagebox.showinfo("Correct Answer!!!", "hoorah ! that's the correct answer!")
                points += 1
            if Answer3.lower() not in Ans3:
                messagebox.showinfo("Wrong Answer!!!", "Awwh ! that's not the correct answer!")
                pass
            Answer4 = tf.simpledialog.askstring("Question.4", "What is the name of earth's the natural satellite ?")
            if Answer4.lower() in Ans4:
                messagebox.showinfo("Correct Answer!!!", "hoorah ! that's the correct answer!")
                points += 1
            if Answer4.lower() not in Ans4:
                messagebox.showinfo("Wrong Answer!!!", "Awwh ! that's not the correct answer!")
                pass
            Answer5 = tf.simpledialog.askstring("Question.5", "Name The Dwarf Planet In Our Solar System")
            if Answer5.lower() in Ans5:
                messagebox.showinfo("Correct Answer!!!", "hoorah ! that's the correct answer!")
                points += 1
            if Answer5.lower() not in Ans5:
                messagebox.showinfo("Wrong Answer!!!", "Awwh ! that's not the correct answer!")
                pass
            Answer6 = tf.simpledialog.askstring("Question.6", "What is the scientific name of humans ?")
            if Answer6.lower() in Ans6:
                messagebox.showinfo("Correct Answer!!!", "hoorah ! that's the correct answer!")
                points += 1
            if Answer6.lower() not in Ans6:
                messagebox.showinfo("Wrong Answer!!!", "Awwh ! that's not the correct answer!")
                pass
            Answer7 = tf.simpledialog.askstring("Question.7", "Name the force which pulls us to the ground ")
            if Answer7.lower() in Ans7:
                messagebox.showinfo("Correct Answer!!!", "hoorah ! that's the correct answer!")
                points += 1
            if Answer7.lower() not in Ans7:
                messagebox.showinfo("Wrong Answer!!!", "Awwh ! that's not the correct answer!")
                pass
            Answer8 = tf.simpledialog.askstring("Question.8", "Name the type of animal that milkfeed their babies")
            if Answer8.lower() in Ans8:
                messagebox.showinfo("Correct Answer!!!", "hoorah ! that's the correct answer!")
                points += 1
            if Answer8.lower() not in Ans8:
                messagebox.showinfo("Wrong Answer!!!", "Awwh ! that's not the correct answer!")
                pass
            Answer9 = tf.simpledialog.askstring("Question.9", "Who disocvered zero ? ")
            if Answer9.lower() in Ans9:
                messagebox.showinfo("Correct Answer!!!", "hoorah ! that's the correct answer!")
                points += 1
            if Answer9.lower() not in Ans9:
                messagebox.showinfo("Wrong Answer!!!", "Awwh ! that's not the correct answer!")
                pass
            Answer10 = tf.simpledialog.askstring("Question.10", "From which direction does sun rise from ? ")
            if Answer10.lower() in Ans10:
                messagebox.showinfo("Correct Answer!!!", "hoorah ! that's the correct answer!")
                points += 1
            if Answer10.lower() not in Ans10:
                messagebox.showinfo("Wrong Answer!!!", "Awwh ! that's not the correct answer!")
                pass
            Name = simpledialog.askstring("Name","Enter Your First Name")
            while points <=5:
                messagebox.showinfo("Congrats","Horrah! "+Name+" You Scored "+str(points)+" points out of 10! Nice Try!")
                return
            while points <= 8:
                messagebox.showinfo("Congrats","Horrah! "+Name+" You Scored "+str(points)+" points out of 10! Great!")
                return
            while points <= 10:
                messagebox.showinfo("Congrats","Horrah! "+Name+" You Scored "+str(points)+" points out of 10! Perfect!")
                return
        def user_input_handler():
            user_entry = entry.get()
            if user_entry == '1':
                Rules()
            elif user_entry == '2':
                root.destroy()
        execute_button = Button(root, text="Execute", command=user_input_handler)
        execute_button.place(x=120, y=176)
    def DECRYPTION():
        def Ask_Data():
            root = tf.Tk()
            root.withdraw()
            message = simpledialog.askstring("Enter the message to decrypt", "Enter the message to decrypt: ")
            root.destroy()
            return message

        def Ask_Key():
            root = tf.Tk()
            root.withdraw()
            key = simpledialog.askinteger("Enter the key", "Enter the key: ")
            root.destroy()
            return key

        encrypted_message = Ask_Data()
        if encrypted_message is None:
            return "No message entered."

        key = Ask_Key()
        if key is None:
            return "No key entered."

        decrypted_message = ""
        key_index = 0
        for char in encrypted_message:
            decrypted_message += chr(ord(char) - key)  
            key_index = (key_index + 1) % len(str(key))
        return decrypted_message

    def ENCRYPTION():
        def Ask_Data():
            root = tf.Tk()
            root.withdraw()
            message = simpledialog.askstring("Enter the message to encrypt", "Enter the message to encrypt: ")
            root.destroy()
            return message

        def Ask_Key():
            root = tf.Tk()
            root.withdraw()
            key = simpledialog.askinteger("Enter the key", "Enter the key: ")
            root.destroy()
            return key

        message = Ask_Data()
        if message is None:
            return "No message entered."

        key = Ask_Key()
        if key is None:
            return "No key entered."

        encrypted_message = ""
        key_index = 0

        for char in message:
            encrypted_message += chr(ord(char) + key)  
            key_index = (key_index + 1) % len(str(key))

        return encrypted_message

    def cryotograohy_menu():
        menu_popup = Toplevel(root)
        menu_popup.title("CrytoGraphy Menu")
        cryptography_options = "**CrytoGraphy Menu** \n1.Encryption \n2.Decryption\n3.Exit"
        menu_label = Label(menu_popup, text=cryptography_options, justify='left')
        menu_label.pack()
        user_input = Entry(menu_popup)
        user_input.pack()
        
        def cryptography_manger():
            choice = user_input.get()
            if choice == '1':
                result = ENCRYPTION()
                messagebox.showinfo("Encrypted data", result)
            if choice == '2':
                result = DECRYPTION()
                messagebox.showinfo("Decrypted data", result)
            if choice == '3':
                root.destroy()

        execute_button = Button(menu_popup, text="Execute", command=cryptography_manger)
        execute_button.pack()

    def password_generator_Aplhabetical_Upper():
        root = tf.Tk()
        root.withdraw()
        choice = tf.simpledialog.askinteger("Password Length", "Enter the length of the PIN code:")

        if choice is not None:
            characters = string.ascii_uppercase
            result = ''.join(random.choice(characters) for _ in range(choice))
            return result
        else:
            return None

    def password_generator_Aplhabetical_Lower():
        root = tf.Tk()
        root.withdraw()
        choice = tf.simpledialog.askinteger("Password Length", "Enter the length of the PIN code:")

        if choice is not None:
            characters = string.ascii_lowercase
            result = ''.join(random.choice(characters) for _ in range(choice))
            return result
        else:
            return None

    def password_generator_Aplhabetical():
        root = tf.Tk()
        root.withdraw()
        choice = tf.simpledialog.askinteger("Password Length", "Enter the length of the PIN code:")

        if choice is not None:
            characters = string.ascii_letters
            result = ''.join(random.choice(characters) for _ in range(choice))
            return result
        else:
            return None

    def password_generator_Aplhanumeric():
        root = tf.Tk()
        root.withdraw()
        choice = tf.simpledialog.askinteger("Password Length", "Enter the length of the PIN code:")

        if choice is not None:
            characters = string.digits + string.ascii_letters
            result = ''.join(random.choice(characters) for _ in range(choice))
            return result
        else:
            return None

    def password_generator_pincode():
        root = tf.Tk()
        root.withdraw()
        choice = tf.simpledialog.askinteger("Password Length", "Enter the length of the PIN code:")

        if choice is not None:
            characters = string.digits
            result = ''.join(random.choice(characters) for _ in range(choice))
            return result
        else:
            return None

    def password_menu():
        menu_popup = Toplevel(root)
        menu_popup.title("Password Menu")
        password_options = "**PASSWORD_MENU**\n1. Pincode\n2. Alphanumeric\n3. Alphabetically\n4. Lowercase\n5. Uppercase\n6. EXIT"
        menu_label = Label(menu_popup, text=password_options, justify='left')
        menu_label.pack()

        user_input = Entry(menu_popup)
        user_input.pack()

        def handle_password_choice():
            choice = user_input.get()
            if choice == '1':
                generated_password = password_generator_pincode()
                messagebox.showinfo("Generated Password", generated_password)
            if choice == '2':
                generated_password = password_generator_Aplhanumeric()
                messagebox.showinfo("Generated Password", generated_password)
            if choice == '3':
                generated_password = password_generator_Aplhabetical()
                messagebox.showinfo("Generated Password", generated_password)
            if choice == '4':
                generated_password = password_generator_Aplhabetical_Lower()
                messagebox.showinfo("Generated Password", generated_password)
            if choice == '5':
                generated_password = password_generator_Aplhabetical_Upper()
                messagebox.showinfo("Generated Password", generated_password)
            elif choice == '6':
                menu_popup.destroy()

        execute_button = Button(menu_popup, text="Execute", command=handle_password_choice)
        execute_button.pack()

    root = tf.Tk()
    root.title("***GUI MENU***")
    root.geometry('280x280')
    entry = Entry(root)
    entry.pack()
    LP = tf.Listbox(root)
    LP.insert(1, " 1. Password Generator")
    LP.insert(2, "2. Cryptography")
    LP.insert(3,"3.Quiz")
    LP.insert(4, "4. Exit")
    LP.place(x='0', y='10')
    entry.place(x='1', y='176')

    def user_input_handler():
        user_input = entry.get()
        if user_input == '1':
            password_menu()
        if user_input == '2':
            cryotograohy_menu()
        if user_input == '3':
            Quiz()
        if user_input == '4':
            root.destroy()

    execute_button = Button(root, text="Execute", command=user_input_handler)
    execute_button.place(x=120, y=176)

    root.mainloop()
def main_menu():
    try:
        while True:
            print("***FUNCTION MENU***\n1. Password Function\n2. Stack Function\n3. Calculator\n4. Encryption\n5. Turtle Graphic\n6. File Function\n7. Quiz\n8. Fun Fact \n9. History  \n10.Translator \n11.SQL \n12.GUI MENU \n13.Dictionary\n14.Snake Game \n15.Friday \n16.Exit")
            Choice = int(input("Select a Function:"))
            if Choice == 1:
                main()
                function_usage["Password Function"] += 1
            elif Choice == 2:
                Stack()
                function_usage["Stack Function"] += 1
            elif Choice == 3:
                Calculate()
                function_usage["Calculator"] += 1
            elif Choice == 4:
                Encryptor()
                function_usage["Encryption"] += 1
            elif Choice == 5:
                Turtle_Menu()
                function_usage["Turtle Graphic"] += 1
            elif Choice == 6:
                File_Handle_Menu()
                function_usage["File Function"] += 1
            elif Choice == 7:
                Quiz()
                function_usage["Quiz"] += 1
            elif Choice == 8:
                Fact_Lab()
                function_usage["Fun Fact"] += 1
            elif Choice == 9:
                print("Most frequently used function:", most_frequently_used_function())
            elif Choice == 10:
                Translation_Menu()
                function_usage["Translator"] += 1
            elif Choice == 11:
                SQL_MENU()
                function_usage["SQL"] += 1
            elif Choice == 12:
                GUI_MENU()
                function_usage["GUI MENU"] += 1
            elif Choice == 13:
                dictionary()
                function_usage["Dictionary"] +=1
            elif Choice == 14:
                snake_game()
                function_usage["Snake Game"] +=1
            elif Choice == 15:
                function_usage["Friday"] +=1
                Friday.wish_Me()
                Friday.voice_trigger()
            elif Choice == 16:
                try:
                    confirmation = input("Are You Sure?\n")
                    if confirmation.lower() == "yes":
                        break
                    elif confirmation.lower()=='no':
                        pass
                    else :
                        print('None of the options was selected!')
                except ValueError :
                    print('Invalid Input')
    except ValueError:
        print('Invalid Input!')
main_menu()
