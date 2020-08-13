"""Find palindromes (letter palingrams) in a dictionary file using recursion. (Challenge Project [page 34])"""
import load_dictionary

word_list = load_dictionary.load('../2of4brif.txt')


def is_palindrome(word):
    if len(word) <= 1:
        return True
    else:
        if word[0] == word[-1]:
            return is_palindrome(word[1:-1])
        else:
            return False


pali_list = [x for x in word_list if is_palindrome(x)]

print('\nNumber of palindromes found = {}'.format(len(pali_list)))
print(*pali_list, sep='\n')
