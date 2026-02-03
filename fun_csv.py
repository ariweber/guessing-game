import csv
from itertools import count
import os
from datetime import datetime

fieldnames = ['usernam', 'timestamp', "computer number", "guesses", "last guess", "status"]

def save_game_csv(filename, username, n, count, guess, status):
    rows = []
    user_found = False

    if os.path.exists(filename):
        with open(filename, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)

    new_data = {
            'usernam': username,    
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'computer number': n,   
            'guesses': count,
            'last guess': guess,
            'status': status
            }
    for row in rows:
        if row['usernam'] == username and row['status'] == 'In Progress':
            row.update(new_data)
            user_found = True
            break
   
    if not user_found:
        rows.append(new_data)
    
    with open(filename, mode='w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

def load_game_csv(filename, username):
    if not os.path.exists(filename):
        return None, None
    try:
        with open(filename, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['usernam'] == username and row['status'] == 'In Progress':
                    return int(row['guesses']), int(row['last guess'])
    except Exception:
        return None, None
    return None, None

def should_save_game():
    response = input("Do you want to save and exit? (y/n): ").strip().lower()
    return response in ['yes', 'y']  


           
def game_save(filename, username):
    with open(filename, mode='r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['usernam'] == username and row['status'] == 'In Progress':
                return True
    return False