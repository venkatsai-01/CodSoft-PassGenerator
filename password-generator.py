import random
import string

def generate_password(length):
    used_characters = string.ascii_lowercase + string.ascii_uppercase \
    + string.digits + string.punctuation
    
    password = ""
    for i in range(length):
        password = password + random.choice(used_characters)
    
    return password

def main():
    while(True):
        len = int(input("Enter the desired length of password: "))
        if(len<8):
            print("Enter a minimum of 8 characters. Try again.")
            continue
        password = generate_password(len)
        print(f'Generated Password: "{password}"')
        break

if __name__ == "__main__":
    main()