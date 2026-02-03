from menu import user_login, play_game
import random
from fn_user import craet_user

def main():
    print("Welcome to the Guessing Game!")
    auth_file = "users.csv"
    
    usename = user_login(auth_file)

    if not usename:
        craet_user(auth_file)
        print("User registered. Please log in again.")
        return
    else:
    
      n = random.randint(1, 500)
      print(n)
      play_game(n, usename)

if __name__ == "__main__":
    main()