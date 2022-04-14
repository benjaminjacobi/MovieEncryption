import string

ENGLISH_ALPHABET_LENGTH = 26


def calculate_shifted_letter(char: str, caesar_cipher_shift: int):
    if char.islower():
        shifted_char_index = (string.ascii_lowercase.index(char) + caesar_cipher_shift) % ENGLISH_ALPHABET_LENGTH
        return string.ascii_lowercase[shifted_char_index]

    elif char.isupper():
        shifted_char_index = (string.ascii_uppercase.index(char) + caesar_cipher_shift) % ENGLISH_ALPHABET_LENGTH
        return string.ascii_uppercase[shifted_char_index]

    return char


def caesar_cipher_encrypt(content: str, caesar_cipher_shift: int):
    return "".join([calculate_shifted_letter(c, caesar_cipher_shift) for c in content])
