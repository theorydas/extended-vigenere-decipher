# extended-vigenere

Everyone in the world of cryptography and puzzles is usually immediately introduced to the Vigenere encoding scheme which is usually
found in basic puzzles. This encoding/decoding technique can be seen as an expansion of the Caesar Cipher, where instead of a message
being shifted in the alphabet by a constant value, the amount of "shifting" is related to the position of each letter inside the message.
The behaviour of this shifting is simply controlled by the `key` which is another word that is usually repeated to overlap the message
and each of its letters induces a different shift to corresponding message's letters depending on the position of the letter's key on the
alphabet.

 ![The default Vigenere cipher table](figures/Default_table.png)


Even though the Vigenere cipher is very simple to understand and use, it is usually never extended to different alphabets or to include different
symbols and because of this there are no easy to find or use tools online that would account for that. Indeed, when I recently required such an
extended vigenere table, I wasn't able to find a useful tool online and ended up coding these simple functions. Here, extended-vigenere offers a simply python
tool that handles the Vigenere encryption and decryption that supports the traditional Vigenere table as well as any other custom character table that
can be created.

## Requirements

The vigenere mapping uses `numpy` arrays to perform index addition.