import time

#create file and fill in text
def create_file():
    f = open("task16.txt", "x")
    f.write("Congrats! Here a new file!")
    print("File created and text entered!")
    f.close()

def read_file():
    f = open("task16.txt", "r")
    if f.read(9) == "Congrats!":
        print("File created succesfully and entered data is correct")
    else:
        print("Something go wrong!")
    f.close()

create_file()
time.sleep(30)
read_file()