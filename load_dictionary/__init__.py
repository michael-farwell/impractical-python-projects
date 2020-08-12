"""Load a text file as a list.

Arguments:
-text file name (and dictionary path, if needed)
-word length to exclude (defaults to 1)

Exceptions:
-IOError if filename not found.

Returns:
-A list of all words in a text file in lower case.

Requires-import sys

"""
import sys


def load(file, word_length=1):
    """Open a text file & return a list of lowercase strings."""
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt if len(x) > word_length]
            return loaded_txt
    except IOError as error:
        print('{}\nError opening {}. Terminating program.'.format(
            error, file), file=sys.stderr)
        sys.exit(1)
