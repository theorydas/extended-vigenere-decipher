 # extended-vigenere

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This simple python tool offers an easy-to-use way to handle Vigenere encryption and decryption and can also support the traditional Vigenere table as well as any other custom character table that can be created (character or number addition/subtraction, or shuffling).

## The Vigenere Puzzle

Everyone in the world of cryptography and puzzles is usually immediately introduced to the Vigenere encoding scheme which is usually
found in basic puzzles. This encoding/decoding technique can be seen as an expansion of the Caesar Cipher, where instead of a message
being shifted in the alphabet by a constant value, the amount of "shifting" is related to the position of each letter inside the message.
The behaviour of this shifting is simply controlled by the `key` which is another word that is usually repeated to overlap the message
and each of its letters induces a different shift to corresponding message's letters depending on the position of the letter's key on the
alphabet.

 ![The default Vigenere cipher table](figures/Default_table.png)

Even though the Vigenere cipher is very simple to understand and use, it is usually never extended to different alphabets or to include different
symbols and because of this there are no easy to find or use tools online that would account for that. Indeed, when I recently required such an
extended Vigenere table, I wasn't able to find a useful tool online and ended up coding these simple functions.

## Usage

### Python
When using custom character tables, one has to specify a list of the desired characters and positions.
```python
characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
              "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
              "!", "@", "#", "$", "_"]
```
Then, encoding and decoding is simply performed by calling the relevant functions.
```python
hidden_message = "this_is_a_test_message!"
encoded_message = extended_vigenere.encode(hidden_message, "secr@tkey", characters)

- glke!@#dyrxgepswilfeivw
```

```python
encoded_message = "glke!@#dyrxgepswilfeivw"
decoded_message = extended_vigenere.decode(Encoded_Message, "secr@tkey", characters)

- this_is_a_test_message!
```

### Command Line
Similarly to the python interface, these functions can be called directly from the command line for input and output file paths. If tablePath is omitted,
the default Vigenere table is used instead.
```
$ python extended_vigenere.py inputPath outputPath -table tablePath -key yourKey -encode true
```

## Requirements

The Vigenere mapping uses `numpy` arrays to perform index shifting.

### TODO
* Requires support for capitalization.
* Requires support characters not in the table.