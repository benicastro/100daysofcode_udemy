"""Caesar Cipher Project, by Benedict Castro benedict.castro11@gmail.com
An encryption/decryption tool.
Tags: short, code, logic"""

# Import needed modules
import proj_art
from alphabet import alphabet


def main():
    print(proj_art.logo)
    print('''Caesar Cipher, an encryption/decryption tool.
    By Benedict Castro benedict.zcastro@gmail.com''')

    def ask_user():
        """This function asks the user if he/she wants to either encrypt or decrypt some text."""
        invalid_inputs = True
        while invalid_inputs:
            user_choice = input('Type "encode" to encode, or type "decode" to decode: ')
            user_message = input("Please type your message: ").lower()
            shift_number = int(input("Please provide the shift number (int): "))
            if shift_number > 26:
                shift_number %= 26
            if user_choice.lower() not in ["encode", "decode"]:
                print("Please provide a valid input.")
            else:
                invalid_inputs = False
                return user_choice, user_message, shift_number

    def enc_dec(user_choice, user_message, shift_number):
        """This function encrypts/decrypts the given message based on the user's choice."""
        new_message = ''
        if user_choice == "decode":
            shift_number *= -1
        for letter in user_message:  # Find the letters in the user's message and shift them
            if letter.isalpha():
                letter_index = alphabet.index(letter)
                new_index = letter_index + shift_number
                new_message += alphabet[new_index]
            else:
                new_message += letter
        return new_message

    run_program = True
    while run_program:  # Main program loop
        user_choice, user_message, shift_number = ask_user()
        output = enc_dec(user_choice, user_message, shift_number)
        print(f"The {user_choice}d message is: {output}.")

        # Ask user if they want to try again.
        use_again = input('Do you want to use the tool again? Please type "yes" or "no": ')
        if use_again.lower() != "yes":
            break

    print("Thanks for using this tool! May you decipher all your worries away.")


# If the program is run (instead of imported), run the game:
if __name__ == "__main__":
    main()
