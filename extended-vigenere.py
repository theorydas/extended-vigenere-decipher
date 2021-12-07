import numpy as np

# ==== Backbone =====

def findIndex(input_word: str, character_list: list) -> np.array:
    """ Returns a numpy array of the index values of the input_word that map to the
    positions of the characters list.
    
    ### Parameters
    input_word : {str}
        The word whose index-mapping should be performed.
    character_list : {list}
        A list containing all relevant vigenere characters in the table. This must
        include all of the characters in `input_word`.
    
    ### Returns
    index_list : {np.array}
        A numpy array with the size as input_word and that each element corresponds
        to the index of that character on the character_list.
    """
    return np.array([character_list.index(digit) for digit in input_word])

def findWord(input_index: list, character_list: list) -> str:
    """ Returns a list of the characters that index each value of input_index on
    the character_list
    
    ### Parameters
    input_index : {list}
        The indexes that will be converted into characters.
    character_list : {list}
        A list containing all relevant vigenere characters in the table. This must
        include all of the characters in `input_word`.
    
    ### Returns
    char_list : {np.array}
        A numpy array with the size as input_index and that each element corresponds
        to what is indexed on the character_list.
    """
    char_list = [character_list[i % len(character_list)] for i in input_index]
    
    return "".join(char_list)

def viginereWord(word: str, key: str, character_list: list, encode: bool = True) -> str:
    encode = 1 if encode else -1
    
    # Turn words into index arrays on the character_list list.
    word_ = findIndex(word, character_list)
    key_ = findIndex(key, character_list)

    # Repeat and crop the key to match word.
    key_ = np.tile(key_, int(len(word_)/len(key_)) +1)[:len(word_)]
    
    # Shift the index using the key and remap to character_list.
    encoded_word_index = word_ +key_ *encode
    encoded_word = findWord(encoded_word_index, character_list)
    
    return encoded_word

# ==== Utility functions.

def Encode(word: str, key: str, character_list: list):
    encoded_word = viginereWord(word, key, character_list, encode = True)
    
    return encoded_word

def Decode(word: str, key: str, character_list: list):
    decoded_word = viginereWord(word, key, character_list, encode = False)
    
    return decoded_word