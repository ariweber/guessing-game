from random import randint 
from file_functions import empty_file, new_record, write_to_file
import os
from fun_csv import load_game_csv, should_save_game, save_game_csv
from fn_user import  user_input,  user_authenticated
import sys

def user_login(filename):
    username, password = user_input(filename)
    if user_authenticated(filename, username, password):
        print("Login successful.")
        return username
    else:
        print("Login failed.")
        return None




def play_game(n, username):

       
    
    
    
    win = False
    count = 0
    filename = "save_game.csv"
   
    

    keeping_enabled = should_save_game() 
    if keeping_enabled:
        save_game_csv(filename, username, n, count, 0, "In Progress")
        print("Saving system activated.")

    while not win: 
        raw_input = input("\nGuess a number between 1 and 500: ")
        if raw_input.lower() == "exit":
            status = "In Progress"
            save_game_csv(filename, username, n, count, guess, status)
            print("Exiting the game. Goodbye!")
            return
        
        try:    
            guess = int(raw_input)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue    

        count += 1
        if guess < n:
            result = "Too low!"
            status = "In Progress"
        elif 500 >= guess > n:
            result = "Too high!"
            status = "In Progress"
        elif guess < 1 or guess > 500:
            result = "Number out of range! Please guess between 1 and 500."
            status = "In Progress"
        else:   
            result = "you win!"
            status = "Completed"
            win = True
      
                 
                
        
        print(result)

        if keeping_enabled:
            print(f"Update CSV with guess {guess}?")
            if should_save_game():
                save_game_csv(filename, username, n, count, guess, status)
                print("Progress updated.")

    print(f"\nGame Over! Total guesses: {count}.")
    if empty_file("record.txt"):
        write_to_file("record.txt", count)
    else:
        if new_record("record.txt", count):    
            print("New record!")


 
def print_welcome():
    print("Welcome to the Guessing Game!")
    print("plalse enter username and password to login or register.")
    
    