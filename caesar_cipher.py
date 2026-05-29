"""
Caesar Cipher Core Cryptographic Module
---------------------------------------
This module provides the core cryptographic logic for encrypting and decrypting
text using the classic Caesar Cipher algorithm.

It is designed with cybersecurity best practices for simple algorithms:
1. Case Preservation: Ensures uppercase and lowercase letters retain their original case.
2. Character Safety: Non-alphabetic characters (numbers, punctuation, symbols, spaces)
   are skipped and left untouched.
3. Arbitrary Shifts: Modulo arithmetic gracefully handles shifts larger than 26,
   negative shifts, and zero shift.
4. Performance: O(n) time complexity and O(n) space complexity.
"""

def shift_character(char: str, shift: int) -> str:
    """
    Shifts a single alphabetic character by a specified shift value.
    Non-alphabetic characters are returned unmodified.

    :param char: A string containing a single character to shift.
    :param shift: The integer shift offset (can be positive, negative, or large).
    :return: The shifted character string of length 1.
    """
    if not char.isalpha():
        return char

    # Determine the ASCII base based on the character's casing
    ascii_base = ord('A') if char.isupper() else ord('a')
    
    # Apply Caesar Cipher formula: E_n(x) = (x + n) mod 26
    # Subtract ASCII base to shift mapping to 0-25 range, apply shift,
    # map back to ASCII range after applying modulo 26.
    shifted_code = (ord(char) - ascii_base + shift) % 26
    return chr(ascii_base + shifted_code)


def encrypt(text: str, shift: int) -> str:
    """
    Encrypts a plaintext string using the Caesar Cipher algorithm.

    :param text: The raw plaintext message to encrypt.
    :param shift: The shift key (integer offset).
    :return: The encrypted ciphertext string.
    """
    return "".join(shift_character(char, shift) for char in text)


def decrypt(text: str, shift: int) -> str:
    """
    Decrypts a ciphertext string using the Caesar Cipher algorithm.

    :param text: The encrypted ciphertext message to decrypt.
    :param shift: The shift key used for encryption (integer offset).
    :return: The decrypted plaintext string.
    """
    # Decryption is mathematically equivalent to encryption with a negative shift
    return "".join(shift_character(char, -shift) for char in text)