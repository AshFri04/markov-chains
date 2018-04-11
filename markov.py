"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path) as my_file:
        file_data = my_file.read()
    return file_data


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    words = text_string.split()

    # for i in range(len(words)-2):
    for i, word in enumerate(words):
        try:
            chains[(words[i], words[i+1])] = chains.get((words[i], words[i+1]),\
                []) + [words[i+2]]
        except IndexError:
            None
    for key in chains:
        print key, chains[key]

    return chains


def make_text(chains):

    """Return text from chains."""

    word_list = []

    random_key = choice(chains.keys())

    for word in random_key:
        word_list.append(word)

    new_key = (random_key[1], choice(chains[random_key]))
    word_list.append(new_key[1])

    while True:

        #check to see if new_key in chains
        if not chains.get(new_key):
            break
        else:
            new_random_word = choice(chains[new_key])
            word_list.append(new_random_word)
            new_key = (new_key[1], new_random_word)

    return ' '.join(word_list)


#            w1   w2            w3
# "could you + [       with        ]"
        
#                                   w4
#         (w2,          w3) ---> random_value
#         you          with         a
#         with          a           

import sys
input_path = sys.argv[1]

input_path = "taylorswiftlyrics.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
