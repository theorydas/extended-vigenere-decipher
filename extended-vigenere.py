# I need a way to encode/decode the chain. What if the key=chain aka name of file is keychain.txt
import numpy as np

def findIndex(word: str, characters: list) -> np.array:
    return np.array([characters.index(digit) for digit in word])

def findWord(index: list, characters: list) -> list:
    return [characters[i % len(characters)] for i in index]

def viginereWord(word: str, key: str, characters: list, encode: int = 1) -> str:
    encode = 1 if encode else -1
    
    # Turn words into index arrays on the characters list.
    word_ = findIndex(word, characters)
    key_ = findIndex(key, characters)

    # Repeat and crop the key to match word.
    key_ = np.tile(key_, int(len(word_)/len(key_)) +1)[:len(word_)]
    
    # Shift the index using the key and remap to characters.
    encoded_word_index = word_ +key_ *encode
    encoded_word = findWord(encoded_word_index, characters)
    
    return encoded_word