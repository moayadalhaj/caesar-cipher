import nltk
import re

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)

from nltk.corpus import words, names

word_list = words.words()
name_list = names.words()

def encrypt(str, k):
    words = str.split()
    cipher_words = []
    for word in words:
        cipher = ""
        for char in word:
            if char.isalpha():
                offset = 97 if char.islower() else 65
                char_num = ord(char)
                shifted_num = char_num + k - offset
                char = chr(shifted_num % 26 + offset)
            cipher += char
        cipher_words.append(cipher)
    return " ".join(cipher_words)

def decrypt(str, k):
    return encrypt(str, -k)


def crack(str):
    cracked_text= ""
    percentage_allow = 60
    
    for key in range (0,26):
        decrypted = decrypt(str,key)
        words = decrypted.split()
        count = 0
        for word in words:
            clean_word = re.sub(r"[^a-zA-Z]+", "", word).lower()
            if clean_word in word_list or clean_word in name_list:
                count+=1
                
        percentage = int(count / len(words) * 100)
        if percentage > percentage_allow:
            cracked_text = decrypted
            
    return cracked_text

if __name__ == '__main__':
    print(encrypt('abc',27))
    print(decrypt('bcd',1))
    print(encrypt('zzz',1))
    print(encrypt('Today we will attack.',5))
    print(decrypt('Ytifd bj bnqq fyyfhp.',5))
    print(crack('Ytifd bj bnqq fyyfhp.'))