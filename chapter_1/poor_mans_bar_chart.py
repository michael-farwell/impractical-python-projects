from collections import defaultdict
from pprint import pprint

"""Show a defaultdict based on common letters in a phrase"""


def main():
    """Get phrase input and show default dict of letters that appear with their frequencies"""

    phrase = input(
        'Please enter the phrase you would like to analyze\n--->')

    phrase = phrase.replace(' ', '')
    letter_dictionary = defaultdict(list)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        letter_dictionary[letter] = []

    for letter in phrase:
        letter_dictionary[letter.lower()].append(letter.lower())

    pprint(letter_dictionary)


if __name__ == "__main__":
    main()
