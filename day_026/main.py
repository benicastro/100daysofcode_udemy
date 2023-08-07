"""
NATO Alphabet Project by Benedict Z. Castro | benedict.zcastro@gmail.com
"""

# Import needed modules
import pandas as pd

# Declare constants/global variables
NATO_CSV = "nato_phonetic_alphabet.csv"

# Import data frame from csv file and convert to a dictionary
nato_alphabet = pd.read_csv(NATO_CSV)
nato_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}


def main():

    # Create a variable and condition asking if the user wants to use the program again
    try_again = True
    while try_again:

        user_input = input("Please provide a word: ").upper()
        user_code = [nato_dict[letter] for letter in user_input]
        print(user_code)

        if input("Do you want to use the program again?: 'Yes' or 'No': ").lower() != "yes":
            try_again = False


# Run the project
if __name__ == "__main__":
    main()
