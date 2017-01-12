from random import choice
import twitter
import os

import sys

api = twitter.Api(
    consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
    consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
    access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
    access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET']
    )

def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    open_text_file = open(file_path).read()
    # print file_green_eggs

    return open_text_file


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    words = text_string.split()

    for i in range(len(words)-2):
        key1 = words[i]
        key2 = words[i+1]
        key_words = (key1, key2)

        value_word = words[i+2]

        if key_words not in chains:
            chains[key_words] = [value_word]
        else:
            chains[key_words].append(value_word)

    return chains


# def make_more_chains(text_string):
#     """Takes input text as string; returns _dictionary_ of markov chains.

#     A chain will be a key that consists of a tuple of (word1, word2)
#     and the value would be a list of the word(s) that follow those two
#     words in the input text.

#     For example:

#         >>> make_chains("hi there mary hi there juanita")
#         {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
#     """

#     chains = {}

#     words = text_string.split()

#     for i in range(len(words)):
#         key1 = words[i]
#         print key1

#         key2 = words[i+1]
#         key_words = (key1, key2)

#         value_word = words[i+2]

#         if key_words not in chains:
#             chains[key_words] = [value_word]
#         else:
#             chains[key_words].append(value_word)

#     return chains

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    # key_word randon grabs key
    key_word = choice(chains.keys())
    text = key_word[0] + " " + key_word[1]

    while key_word in chains:
        random_word = choice(chains[key_word])
    #     print random_word
        text = text + " " + random_word
        key_word = (key_word[1], random_word)

    return text[0:140]



input_path = sys.argv[1]
# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

#chains = make_more_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text






# def open_and_read_file(file_path):
#     """Takes file path as string; returns text as string.

#     Takes a string that is a file path, opens the file, and turns
#     the file's contents as one string of text.
#     """

#     file_green_eggs = open(file_path).read()
#     # print file_green_eggs

#     return file_green_eggs

# open_and_read_file("green-eggs.txt")


# def make_chains(text_string):
#     """Takes input text as string; returns _dictionary_ of markov chains.

#     A chain will be a key that consists of a tuple of (word1, word2)
#     and the value would be a list of the word(s) that follow those two
#     words in the input text.

#     For example:

#         >>> make_chains("hi there mary hi there juanita")
#         {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
#     """

#     chains = {}

#     words = text_string.split()

#     for i in range(len(words)-2):
#         key1 = words[i]
#         key2 = words[i+1]
#         key_words = (key1, key2)

#         value_word = words[i+2]

#         if key_words not in chains:
#             chains[key_words] = [value_word]
#         else:
#             chains[key_words].append(value_word)

#     return chains


# def make_text(chains):
#     """Takes dictionary of markov chains; returns random text."""

#     # key_word randon grabs key
#     key_word = choice(chains.keys())
#     text = key_word[0] + " " + key_word[1]
    
#     while key_word in chains:
#         random_word = choice(chains[key_word])
#     #     print random_word
#         text = text + " " + random_word
#         key_word = (key_word[1], random_word)

#     return text

 # input_path = "green-eggs.txt"

 # Open the file and turn it into one long string
 # input_text = open_and_read_file(input_path)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print random_text
# def make_text(chains):
#     """Takes dictionary of markov chains; returns random text."""

#     # key_word randon grabs key
#     key_word = choice(chains.keys())
#     text = key_word[0] + " " + key_word[1]

#     while key_word in chains:
#         random_word = choice(chains[key_word])
#     #     print random_word
#         text = text + " " + random_word
#         key_word = (key_word[1], random_word)

#     return text
