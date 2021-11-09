import random
import platform
import os
import sys
import time
import sqlite3

#Create database connection to SQLite
def connect_database(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    sql = """
    CREATE TABLE IF NOT EXISTS Trivia(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Question TEXT,
    Answer TEXT,
    Difficulty TEXT,
    Category TEXT
    )
    """
    cursor.execute(sql)
    conn.commit()
    conn.close()

#Clears screen to make it easier to follow.
def clear_screen():
    user_os = platform.system()
    if user_os == "Windows":
        os.system('cls')
    else:
        os.system('clear')

#Main titlepage of entire game. Where all choices are made.
def main_menu():
    msg = """
    Trivial Pursuit Assistant Edition
    =================================
    
    Please choose an option:
    
    1. Add question to trivia database
    2. Edit question in trivia database
    3. Delete question in trivia database
    4. View trivia database
    5. Choose trivia difficulty
    6. Roll the dice
    7. Exit
    """
    
    answers = ["1", "2", "3", "4"]
    print(msg)
    choice = input("Enter your number here:\n")
    if choice not in answers:
        print("Incorrect choice. Please try again.")
    elif choice == "1":
        clear_screen()
        add_trivia()
    elif choice == "2":
        clear_screen()
        edit_trivia()
    elif choice == "3":
        clear_screen()
        delete_trivia()
    elif choice == "4":
        clear_screen()
        view_trivia()
    elif choice == "5":
        clear_screen()
        difficulty()
    elif choice == "6":
        clear_screen()
        die_roll()
    elif choice == "7":
        clear_screen()
        sys.exit()
    
#User can add trivia to database
def add_trivia():
    question  = input("Please enter a new question, or say Back.\n")
    question = question.capitalize()
    if question == "Back":
        clear_screen()
        print("You just returned from the add trivia screen.\n")
        main_menu()
    else:
        answer = input("What is the answer?\n")
        answer = answer.capitalize()
        difficulty = input("What is the difficulty?\n")
        difficulty = difficulty.capitalize()
        category = input("What is the category?\n")
        category = category.capitalize()
        option = ["Yes", "No"]
        response = input("Is everything above correct? Yes or No.\n")
        response = response.capitalize()
        if response not in option:
            clear_screen()
            add_trivia()
        else:
            conn = sqlite3.connect('Trivia.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO Trivia (id, Question, Answer, Difficulty, Category) VALUES(NULL, ?, ?, ?, ?)', (question, answer, difficulty, category))
            conn.commit()
            print("question saved!")
            conn.close()
            add_trivia()

#Remove questions from database      
def delete_trivia():
    pass
    
#Edit database entries
def edit_trivia():
    pass

#View trivia database
def view_trivia():
    pass

#User see the trivia question
def question(category, difficulty):
    give_answer = input("This is where you would see a trivia question.")
    clear_screen()
    main_menu()

#User can choose question category
def category(difficulty):
    answers = ["Cat 1", "Cat 2", "Cat 3"]
    category = input("Choose a category:\nCat 1, Cat 2, or Cat 3?\n")
    category = category.capitalize()
    if category not in answers:
        clear_screen()
        print("Invalid category selection. Please try again.\n")
        category(difficulty)
    else:
        question(category, difficulty)

#User can choose question difficulty
def difficulty():
    answers = ["Easy", "Medium", "Hard", "Random", "Back"]
    choice = input("Choose your difficulty level:\nEasy, Medium, Hard, Random\nYou can say Back at any time.\n")
    choice = choice.capitalize()
    if choice not in answers:
        clear_screen()
        print("Invalid difficulty level. Please try again.")
        difficulty()
    elif choice == "Back":
        clear_screen()
        print("You just returned from the difficulty screen.\n")
        main_menu()
    else:
        clear_screen()
        category(choice)

#User can roll a single die
def die_roll():
    dice_number = random.choice([1,2,3,4,5,6])
    answers = ["Yes", "No"]
    choice = input("Would you like to roll? Yes or No.\n")
    choice = choice.capitalize()
    if choice == "No":
        clear_screen()
        print("You just returned from the die roll screen.\n")
        main_menu()
    elif choice == "Yes":
        clear_screen()
        print(f"You rolled: {dice_number}.\n")
        die_roll()
    if choice not in answers:
        clear_screen()
        print("That is not a correct selection. Please try again.\n")
        die_roll()

#Run game
connect_database(r"Trivia.db")
main_menu()

#INCOMPLETE:
#add_trivia()
#delete_trivia()
#edit_trivia()
#question()
#category()
#difficulty()

#ADD: add_trivia() - add restrictions to difficulty [easy, medium, hard]

#ADD: difficulty() - Change "answers" variable to values from database.
#ADD: difficulty() - If database is BLANK, display error message

#ADD: category() - Connect to database
#ADD: category() - change "answers" variable to value from database

#ADD: question() - Display question
#ADD: question() - Interact to display answer
#ADD: question() - Create option to get new question or change settings

#ADD: question() - Display question as "{ID}. {QUESTION}"

#ADD: delete_trivia() - create function

#ADD: edit_trivia() - create function

#ADD: view_trivia() - create function
