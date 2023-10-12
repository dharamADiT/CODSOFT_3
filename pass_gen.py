import random
import string
# i am taking here one function "pass_gen"...
def pass_gen(length, use_lowercase=True, use_uppercase=True, use_digits=True, use_special_chars=True):
    char = ""
    if use_lowercase:
        char += string.ascii_lowercase
    if use_uppercase:
        char += string.ascii_uppercase
    if use_digits:
        char += string.digits
    if use_special_chars:
        char += string.punctuation

    if len(char) == 0:
        print("Error: Please Enable at least one character type from these !")
        return None
    
    password = ''.join(random.choice(char) for _ in range(length))
    return password

def main():
    try:
        print("------------")
        length = int(input("Enter the lenth of your password:- "))
        use_lowercase = input("Do you want to include lowercase ? (yes/no):- ").lower() == "yes"
        use_uppercase = input("Do you want to include  uppercase letters? (yes/no):- ").lower() == "yes"
        use_digits = input("Do you want to include  digits? (yes/no):- ").lower() == "yes"
        use_special_chars = input("Do you want to include special characters? (yes/no):- ").lower() == "yes"

        password = pass_gen(length, use_lowercase, use_uppercase, use_digits, use_special_chars)
        
        if password:
            print("This is your Generated Password: ", password)
        else:
            print("Password generation failed.")
    except ValueError:
        print("Invalid input. Please enter a valid integer for password length.")

if __name__ == "__main__":
    main()
