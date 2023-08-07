"""
PhoneticCode Class - can be used to create a list of the phonetic code words from the NATO alphabet for a given word as input.
"""


class PhoneticCode:

    def __init__(self):
        self.nato_alphabet = {'A': 'Alfa',
                              'B': 'Bravo',
                              'C': 'Charlie',
                              'D': 'Delta',
                              'E': 'Echo',
                              'F': 'Foxtrot',
                              'G': 'Golf',
                              'H': 'Hotel',
                              'I': 'India',
                              'J': 'Juliet',
                              'K': 'Kilo',
                              'L': 'Lima',
                              'M': 'Mike',
                              'N': 'November',
                              'O': 'Oscar',
                              'P': 'Papa',
                              'Q': 'Quebec',
                              'R': 'Romeo',
                              'S': 'Sierra',
                              'T': 'Tango',
                              'U': 'Uniform',
                              'V': 'Victor',
                              'W': 'Whiskey',
                              'X': 'X-ray',
                              'Y': 'Yankee',
                              'Z': 'Zulu'}

    def nato_code(self, word):
        """Returns a list with the phonetic code words for the input word."""
        return [self.nato_alphabet[letter] for letter in word.upper() if letter in self.nato_alphabet.keys()]
