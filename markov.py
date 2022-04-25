"""Generate Markov text from text files."""

from itertools import chain
from random import choice

input_path = 'green-eggs.txt'
# input_path = 'gettysburg.txt'

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    with open(file_path) as f:
        text = f.read()
    #read function to return text as string

    return text



def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

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

    words = text_string.split()                 #tokenizing each word, returns big list

    for i in range(len(words) - 2):             #for loop to loop through words
        key = (words[i], words[i + 1])          #make each key word[i] and [i+1]
        value = words[i + 2]                    #value is at index i + 2

        if key not in chains:                   #if key is not in dictionary, make key an empty list
            chains[key] = []
            
        chains[key].append(value)               #add all the values to the list

    return chains



def make_text(chains):
    """Return text from chains."""
    
    words = []
    key_list = list(chains.keys())              #make key list from chains.key
  
    random_key = choice(key_list)               #using choice to pick random key
    words.extend(random_key)                    #extending to words
    random_value = choice(chains[random_key])   #using choice to pick random value associated with that key
    words.append(random_value)                  #appending the value
    item2 = random_key[1]                       #get item2 via index 1 of random_key


    while True:

        next_key = (item2, random_value)           #creating new key from item2 and random_value
        if chains.get(next_key, None) == None:      #checking if key has value either to break the loop or add to words list
            break
        # else:
        #     words.extend(next_key)

        random_value = choice(chains[next_key]) #using choice to pick random value associated with that key, also resets random_value
        words.append(random_value)              #appending the value
        item2 = next_key[1]                     #get new item2


    return ' '.join(words)
    


# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
