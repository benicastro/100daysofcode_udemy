# PyPassword Generator

def generate_password(num_letters, num_symbols, num_numbers):
    """
    This function generates a random password for the user based on the number of input values and types.
    :param num_letters: number of letter occurrences in the password
    :param num_symbols: number of symbol occurrences in the password
    :param num_numbers: number of numbers occurrences in the password
    :return: random_password
    """
    # Import needed modules
    import characters
    import random

    random_password = ''
    for i in range(num_letters):
        random_password += random.choice(characters.letters)
    for j in range(num_symbols):
        random_password += random.choice(characters.symbols)
    for k in range(num_numbers):
        random_password += random.choice(characters.numbers)
    password_list = list(random_password)
    random.shuffle(password_list)
    random_password = ''.join(password_list)
    return random_password


# Execute program
print("Welcome to Milyastroc's PyPassword Generator!")
num_letters = int(input("Please provide number of letters: "))
num_symbols = int(input("Please provide number of symbols: "))
num_numbers = int(input("Please provide number of symbols: "))
password = generate_password(num_letters, num_symbols, num_numbers)
print(f"Your password is {password}.")

