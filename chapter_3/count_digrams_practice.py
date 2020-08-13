"""
A program that finds the digrams in a given string and determines their frequencies in a dictionary file
(Practice Project [page 61])
"""
import load_dictionary


def get_digrams(word):
    """Finds and returns a set of digrams found in a given word"""
    digrams = set()
    word_len = len(word)

    for index, letter in enumerate(word):
        for i in range(word_len):
            if i != index:
                digrams.add(letter + word[i])
    print(f'# of digrams found = {len(digrams)}')
    return digrams


def set_up_occurrences_object(keys):
    """Create an object were keys are set to a zero value"""
    occurrences_object = {}
    for key in keys:
        occurrences_object[key] = 0

    return occurrences_object


def occurrences_to_percentage(occurrences_dict, n):
    for key in occurrences_dict:
        occurrences = occurrences_dict[key]
        occurrences_dict[key] = (occurrences / n) * 100

    return occurrences_dict


def remove_uncommon_digrams(digrams, word_list, threshold=0.1):
    """
    Remove and return uncommon digrams based on occurrence
    in given word list to a given threshold(defaults to .1%)
    """
    digram_frequencies = set_up_occurrences_object(digrams)
    word_list_len = len(word_list)

    for word in word_list:
        for digram in digrams:
            if digram in word:
                digram_frequencies[digram] += 1

    digram_frequencies = occurrences_to_percentage(digram_frequencies, word_list_len)

    rejects = {key for key in digram_frequencies if float(digram_frequencies[key]) <= threshold}

    filter_1 = digrams - rejects
    print(f'# of digrams after uncommon filtering = {len(filter_1)}')

    return filter_1, rejects


def remove_first_pair_rejects(filter_1, word_list, threshold=0.1):
    """
    Remove and return uncommon digrams based on occurrence
    as first pair in given word list to a given threshold(defaults to .1%)
    """
    first_pair_frequencies = set_up_occurrences_object(filter_1)
    word_list_len = len(word_list)

    for word in word_list:
        for digram in filter_1:
            if word.startswith(digram):
                first_pair_frequencies[digram] += 1

    first_pair_frequencies = occurrences_to_percentage(first_pair_frequencies, word_list_len)

    first_pair_rejects = {key for key in first_pair_frequencies if float(first_pair_frequencies[key]) <= threshold}

    filter_2 = filter_1 - first_pair_rejects
    print(f'# of digrams after first pair filtering = {len(filter_2)}')

    return filter_1 - first_pair_rejects, first_pair_rejects


def main():
    word = input('Enter a word to find digrams for: ')
    word = word.lower()

    word_list = load_dictionary.load('../2of4brif.txt')

    digrams = get_digrams(word)
    filter_1, rejects = remove_uncommon_digrams(digrams, word_list)
    filter_2, first_pair_rejects = remove_first_pair_rejects(filter_1, word_list)

    print(f'Digrams for "{word}": {sorted(filter_2)}')


if __name__ == '__main__':
    main()
