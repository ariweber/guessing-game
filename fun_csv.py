import csv
import os
from datetime import datetime

fieldnames = ['timestamp', "computer number", "guesses", "last guess", "status"]

def save_game_csv(filename, n, count, guess, status):
    with open(filename, mode='a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writerow({
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'computer number': n,     
            'guesses': count,          
            'last guess': guess,   
            'status': status            
        })

def load_game_csv(filename):


    with open(filename, mode='r+', newline='') as csvfile:
        reader = list(csv.DictReader(csvfile))
        if not reader:
            return None, 0
            
        # לוקחים את השורה האחרונה (המשחק האחרון שנשמר)
        last_save = reader[-1]
        
        # מחזירים את המספר של המחשב ואת כמות הניחושים
        return int(last_save['computer number']), int(last_save['guesses'])

def should_save_game():
    response = input("Do you want to save and exit? (y/n): ").strip().lower()
    return response in ['yes', 'y']  

def init_game_csv(filename, computer_number):
    with open(filename, mode='w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        writer.writerow({
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'computer number': computer_number,
            'guesses': 0,
            'last guess': 0,
            'status': "In Progress"
        })
           