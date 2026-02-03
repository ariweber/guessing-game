from fileinput import filename
import bcrypt

def hash_password(password):
    try:
        password = str(password)    
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')
    except Exception as e:
        print(f"Error hashing password: {e}")
        return None

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)


def user_registration(filename):
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    hashed_password = hash_password(password)

    with open(filename, "a") as f:
        f.write(f"{username},{hashed_password}\n")

def user_login(filename):
    try:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        return username, password
    except Exception as e:
        print(f"Error during login: {e}")
        return None, None



def user_authenticated(filename, username, password):
    with open(filename, "r") as f:
        for line in f:
            stored_username, stored_hashed_password = line.strip().split(",")
            if stored_username == username:
                if check_password(password, stored_hashed_password.encode('utf-8')):
                    return True
                else:
                    return False



