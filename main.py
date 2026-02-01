from random import randint 
from file_functions import empty_file, new_record, write_to_file
import os


def compute_number():
    return randint(1, 500)



def play_game(n):
    win = False
    count = 0
    while not win:
        guess = int(input("Guess a number between 1 and 500: "))
        if guess < n:
            print("Too low!")
        elif guess > n:
            print("Too high!")
        else:
            print("you win!")
            win = True
        count += 1
    print(f"guess: {count}.")
    if new_record("record.txt", count):
        print("New record!")
    else:
        print    

        
  




n = compute_number()
print(n)
play_game(n)

