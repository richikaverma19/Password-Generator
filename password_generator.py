import random
import string
from colorama import init, Fore

# Initialize Colorama
init(autoreset=True)

# Function to generate password
def generate_password(length, complexity):
    if complexity == '1':
        characters = string.ascii_letters
    elif complexity == '2':
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Store generated passwords
generated_passwords = []

# Main Program
def password_generator():
    print(Fore.MAGENTA + "\n========== Password Generator ==========\n")
    
    while True:
        try:
            length = int(input(Fore.CYAN + "Enter the desired password length: " + Fore.WHITE))
            if length <= 0:
                print(Fore.RED + "Password length must be a positive number!")
                return
            
            print(Fore.YELLOW + "Choose Password Complexity:")
            print(Fore.YELLOW + "1. Letters only")
            print(Fore.YELLOW + "2. Letters + Digits")
            print(Fore.YELLOW + "3. Letters + Digits + Special Characters")
            
            complexity = input(Fore.CYAN + "Enter choice (1-3): " + Fore.WHITE)
            if complexity not in ['1', '2', '3']:
                print(Fore.RED + "Invalid choice! Please select 1, 2, or 3.")
                continue

            password = generate_password(length, complexity)
            generated_passwords.append(password)
            print(Fore.GREEN + f"\nGenerated Password: {password}\n")
            
            view_previous = input(Fore.CYAN + "Do you want to view previously generated passwords? (yes/no): " + Fore.WHITE).lower()
            if view_previous == 'yes':
                print(Fore.MAGENTA + "\nPreviously Generated Passwords:")
                for i, pwd in enumerate(generated_passwords, 1):
                    print(Fore.YELLOW + f"{i}. {pwd}")
            
            continue_prompt = input(Fore.CYAN + "Do you want to generate another password? (yes/no): " + Fore.WHITE).lower()
            if continue_prompt != 'yes':
                break

        except ValueError:
            print(Fore.RED + "Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    password_generator()
