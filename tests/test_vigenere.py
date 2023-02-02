import extended_vigenere

def test_cycle():
    message = "helloworld"
    encrypted = extended_vigenere.encode(message, "key")
    decrypted = extended_vigenere.decode(encrypted, "key")
    
    assert message == decrypted

def test_identity_encoder():
    message = "helloworld"
    encrypted = extended_vigenere.encode(message, "a")
    
    assert message == encrypted

def test_identity_decoder():
    encryption = "helloworld"
    decrypted = extended_vigenere.decode(encryption, "a")
    
    assert encryption == decrypted

def test_key_repetition():
    message = "helloworld"
    encrypted_1 = extended_vigenere.encode(message, "pof")
    encrypted_2 = extended_vigenere.encode(message, "pofpof")
    
    assert encrypted_1 == encrypted_2