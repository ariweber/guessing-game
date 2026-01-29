from random import randint

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

n = compute_number()
# print(n)
play_game(n)


