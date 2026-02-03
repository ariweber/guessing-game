import bcrypt

def hash_password(password):
    try:
        password = str(password)    
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed
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

user_registration("users.csv")



