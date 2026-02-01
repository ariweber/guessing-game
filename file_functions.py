def empty_file(filename):
        with open(filename, "r") as f:
            content = f.read().strip() 
            if content == "":
                return True 
            else:
                return False 
            
def write_to_file(filename, data):
    with open(filename, "w") as f:
        f.write(str(data))

def new_record(filename, count):
    with open(filename, "r") as f:
        record = f.read().strip()
        if record == "" or count < int(record):
            write_to_file(filename, count)
            return True
        else: 
            return False
