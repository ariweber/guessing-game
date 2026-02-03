from itertools import count
from menu import user_login, play_game
import random
from fn_user import craet_user
from fun_csv import save_game_csv, load_game_csv


def main():
    print("Welcome to the Guessing Game!")
    auth_file = "users.csv"
    save_file = "save_game.csv"
    
    usename = user_login(auth_file)


    if not usename:
        craet_user(auth_file)
        print("User registered. Please log in again.")
        return
    
    count, last_guess = load_game_csv(save_file, usename)

    if count is not None and last_guess is not None:
          choice = input(f"Welcome back {usename}! Found a saved game. Continue? (y/n): ").lower()
          if choice == 'y':
            print(f"Your previous: {count} last guess {last_guess}.")
            play_game(last_guess, usename)
            return
    n = random.randint(1, 500)
    play_game(n, usename)      
if __name__ == "__main__":
    main()