import random
import string

def generate_password(length, include_letters=True, include_numbers=True, include_symbols=True):
    
    letters = string.ascii_letters if include_letters else ''
    numbers = string.digits if include_numbers else ''
    symbols = string.punctuation if include_symbols else ''

  
    all_characters = letters + numbers + symbols

    if not all_characters:
        raise ValueError("At least one character set must be selected")

 
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():

    print("Welcome to the Password Generator!")

    try:
       
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Password length must be a positive integer.")
            return

        include_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
        include_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        include_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

        if not (include_letters or include_numbers or include_symbols):
            print("You must include at least one type of character.")
            return

        # Generate the password
        password = generate_password(length, include_letters, include_numbers, include_symbols)
        
        print(f"Generated password: {password}")

    except ValueError:
        print("Invalid input. Please enter numeric values for length.")

if __name__ == "__main__":
    main()
