"""
A program that returns a list of 5 randomly generated anagram phrases based on given word(s)
(Challenge Project [page 62])
"""
from collections import Counter

import load_dictionary
import random
from chapter_3.count_digrams_practice import get_digrams, remove_uncommon_digrams, remove_first_pair_rejects


def get_anagrams(name, word_list):
    """Read name & dictionary file & display all anagrams IN name."""
    name_letter_map = Counter(name)
    anagrams = []
    for word in set(word_list):
        test = ''
        word_letter_map = Counter(word.lower())
        for letter in word:
            if word_letter_map[letter] <= name_letter_map[letter]:
                test += letter
        if Counter(test) == word_letter_map:
            anagrams.append(word)

    return anagrams


def generate_random_anagram(word, word_list):
    anagram_phrase = ''
    while True:
        anagrams = get_anagrams(word, word_list)
        if len(anagrams) > 0:
            random_anagram = anagrams[random.randrange(len(anagrams))]
            anagram_phrase += f'{random_anagram} '

            left_over_list = list(word)
            for letter in random_anagram:
                left_over_list.remove(letter)
            word = ''.join(left_over_list)
            # TODO: Handle remaining letters when no anagrams exist
        else:
            break

    return anagram_phrase


def main():
    word_ini = input('Enter a word or words that you would like to find an anagram phrase for: ')
    word_list = load_dictionary.load('../2of4brif.txt')

    phrases = []

    for i in range(5):
        phrases.append(generate_random_anagram(word_ini, word_list))

    print(*phrases, sep='\n')


if __name__ == '__main__':
    main()
