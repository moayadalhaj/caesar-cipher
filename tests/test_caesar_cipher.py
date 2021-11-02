from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import encrypt,decrypt,crack

def test_version():
    assert __version__ == '0.1.0'

def test_encrypt_shifted_string():
    expected = 'bcd'
    actual = encrypt('abc',1)
    assert actual == expected

def test_encrypt_shifted_string2():
    expected = 'aaa'
    actual = encrypt('zzz',27)
    assert actual == expected

def test_encrypt():
    expected = 'Ytifd bj bnqq fyyfhp'
    actual = encrypt('Today we will attack',5)
    assert actual == expected

def test_decrypt():
    expected = 'Today we will attack'
    actual = decrypt('Ytifd bj bnqq fyyfhp',5)
    assert actual == expected

def test_crack():
    expected = 'Today we will attack'
    actual = crack('Ytifd bj bnqq fyyfhp')
    assert actual == expected

def test_decrypted_enycrypted_string():
    expected = 'It was the best of times, it was the worst of times.'
    cipher_text = encrypt('It was the best of times, it was the worst of times.',7)
    actual = crack(cipher_text)
    assert actual == expected
