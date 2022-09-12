from cgitb import text
from cryptography.fernet import Fernet #module that allows for encryption of text

'''
def write_key():                #function to create a key
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file: #wb is write bytes
        key_file.write(key)
'''

def load_key():
   file = open("key.key", "rb") #read bytes mode
   key = file.read()    
   file.close()
   return key

key = load_key()   #bytes is a way of storing info 
fer = Fernet(key)

#key + Password + text to encrypt = random text
#random text + key + password = txt to encrypt

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split('|')
            print("User: ", user, "| Password:", fer.decrypt(passw.encode()))

#r strip will strip off carriage return on line so "\n", you can also use strip() but rstrip() is more specific
# split will take the string and look for "|" and then split the string into a bunch of items each times that "|" is found i.e "hell|time|yes|2" = ["hello", "time", "yes", "2"] and example user, passw, x = ["hello", "time", "x"]
#pass is keyword that does nothing
#view() to call a function example

def add():
    name = input('Account Name:')
    pwd = input("Password:")

    with open('passwords.txt', 'a') as f: 
        f.write(name+"|"+fer.encrypt(pwd.encode()).decode())

#another way to write it is as: file = open("passwords.txt", 'a')
#however with the previous code it will require to be followed up with: file.close()

#command to create a file to store the password 'a' is append which will add something to an existing file or create a file if it dosent exit 'w' is write so it will create or override a new file and 'r' so it will read it only, 'with' allows us to automatically close the file once were done using it, 

while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
