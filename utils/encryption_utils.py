LOWERCASE_ASCII_BASE = ord("a")
UPPERCASE_ASCII_BASE = ord("A")
ENGLISH_ALPHABET_LENGTH = 26


def calculate_shifted_letter(c: str, caesar_cipher_shift: int):
    if c.islower():
        return chr(
            ((ord(c) + caesar_cipher_shift) % LOWERCASE_ASCII_BASE) % ENGLISH_ALPHABET_LENGTH + LOWERCASE_ASCII_BASE)
    elif c.isupper():
        return chr(
            ((ord(c) + caesar_cipher_shift) % UPPERCASE_ASCII_BASE) % ENGLISH_ALPHABET_LENGTH + UPPERCASE_ASCII_BASE)
    return c


def caesar_cipher_encrypt(content: str, caesar_cipher_shift: int):
    return "".join([calculate_shifted_letter(c, caesar_cipher_shift) for c in content])
