import numpy as np

# ==== Backbone ====

# The default english alphabet character list.
default_characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                     "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def find_index(input_word: str, character_list: list) -> np.array:
    """ Returns a numpy array of the index values of the input_word that map to the
    positions of the characters list.
    
    ### Parameters
    input_word : {str}
        The word whose index-mapping should be performed.
    character_list : {list}
        A list containing all relevant Vigenere characters in the table. This must
        include all of the characters in `input_word`.
    
    ### Returns
    index_list : {np.array}
        A numpy array with the size as input_word and that each element corresponds
        to the index of that character on the character_list.
    """
    return np.array([character_list.index(digit) for digit in input_word])

def find_word(input_index: list, character_list: list) -> str:
    """ Returns a list of the characters that index each value of input_index on
    the character_list
    
    ### Parameters
    input_index : {list}
        The indexes that will be converted into characters.
    character_list : {list}
        A list containing all relevant Vigenere characters in the table. This must
        include all of the characters in `input_word`.
    
    ### Returns
    char_list : {np.array}
        A numpy array with the size as input_index and that each element corresponds
        to what is indexed on the character_list.
    """
    char_list = [character_list[i % len(character_list)] for i in input_index]
    
    return "".join(char_list)

def viginere_word(message: str, key: str, character_list: list, encode: bool = True) -> str:
    """ A backbone functions that handles the default vigenere cipher algorithm for both
    encryptions and decrpytions by index-shifting of the index representations of the messsage
    and key inputs on the chararacter_list.
    
    
    ### Parameters
    message : {str}
        The message input to the cipher.
    key : {str}
        The key used by the Vigenere cipher.
    character_list : {list}, default = default_characters.
        A list containing all relevant Vigenere characters in the table. This must
        include all of the characters in `input_word`.
    encode : {bool}, default = True.
        A boolean that controls wether to encrypt or decrypt.
    
    ### Returns
    resulting_message : {str}
        The encoded/decoded product of the encryption.
    """
    encode = 1 if encode else -1
    
    # Turn words into index arrays on the character_list list.
    message_ = find_index(message, character_list)
    key_ = find_index(key, character_list)

    # Repeat and crop the key to match word.
    key_ = np.tile(key_, int(len(message_)/len(key_)) +1)[:len(message_)]
    
    # Shift the index using the key and remap to character_list.
    resulting_message_index = message_ +key_ *encode
    resulting_message = find_word(resulting_message_index, character_list)
    resulting_message = "".join(resulting_message)
    
    return resulting_message

# ==== User Interface functions ====

def encode(message: str, key: str, character_list: list = default_characters) -> str:
    """ Encodes a message using a key by performing a traditional Vigenere cipher
    using a character_list.
    
    ### Parameters
    message : {str}
        The message to be encoded.
    key : {str}
        The key used by the Vigenere cipher.
    character_list : {list}, default = default_characters.
        A list containing all relevant Vigenere characters in the table. This must
        include all of the characters in `input_word`.
    
    ### Returns
    encoded_message : {str}
        The encoded product of the encryption.
    """
    encoded_message = viginere_word(message, key, character_list, encode = True)
    
    return encoded_message

def decode(message: str, key: str, character_list: list = default_characters) -> str:
    """ Decodes a message using a key by performing a traditional Vigenere cipher
    using a character_list.
    
    ### Parameters
    message : {str}
        The message to be decoded.
    key : {str}
        The key used by the Vigenere cipher.
    character_list : {list}, default = default_characters.
        A list containing all relevant Vigenere characters in the table. This must
        include all of the characters in `input_word`.
    
    ### Returns
    decoded_message : {str}
        The decoed product of the encryption.
    """
    decoded_message = viginere_word(message, key, character_list, encode = False)
    
    return decoded_message

# ===== Command line call

import sys
import argparse

def main(argv):
    """ To be used when calling with the command line. """
    
    parser = argparse.ArgumentParser()
    parser.add_argument("inputFile", help = "Path to the input file used with the cipher.")
    parser.add_argument("outputFile", help = "Path of the output file.")
    parser.add_argument("-table", "--table", help = "Path of the character table file. Should simply contains the character one after another.")
    parser.add_argument("-key", "--key", help = "The key used for encryption.", type = str)
    parser.add_argument("-encode", "--encode", help = "Wether encoding or decoding is used. Defaults to True/Encoding.", type = str)
    args = parser.parse_args()
    
    shouldEncode =  True if args.encode == "true" else False
    
    # Load the message from input path.
    message = open(args.inputFile).read()
    key = args.key
    
    if args.table is None:
        table = default_characters
    else:
        table = list(args.table)
    
    # Find the ciphered version of the message.
    ciphered = viginere_word(message = message, key = key, character_list = table, encode = shouldEncode)
    
    # Save new message to output path.
    open(args.outputFile, "w").write(ciphered)
    
if __name__ == "__main__":
    main(sys.argv[1:])