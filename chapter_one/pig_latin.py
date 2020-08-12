"""Translate a phrase into Pig Latin"""


def main():
    "Get phrase input and print translated phrase"
    vowels = ['a', 'e', 'i', 'o', 'u']
    articles = ['the']

    phrase = input(
        'Please enter the phrase you would like to translate into Pig Latin\n--->')

    phrase_list = phrase.split(' ')
    translated_phrase_list = []
    for word in phrase_list:
        if word[0] not in vowels and word not in articles:
            word = word[1:] + '{0}ay'.format(word[0])
            translated_phrase_list.append(word)
        else:
            translated_phrase_list.append(word)
    translated_phrase = ' '.join(translated_phrase_list)
    print("Your translated phrase is:\n--->")
    print(translated_phrase)


if __name__ == "__main__":
    main()
