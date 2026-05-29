"""
Unit Test Suite for Caesar Cipher Core Cryptography
--------------------------------------------------
This suite contains comprehensive automated unit tests targeting the `encrypt`
and `decrypt` functions in the `caesar_cipher` module.

It verifies correctness across basic operations, edge cases, boundaries,
case preservation, non-alphabetic safety, and mathematical wrap-around behavior.
"""

import unittest
from caesar_cipher import encrypt, decrypt


class TestCaesarCipher(unittest.TestCase):
    """Test cases to validate Caesar Cipher logic."""

    def test_basic_encryption(self):
        """Verify that basic English strings are shifted forward correctly."""
        self.assertEqual(encrypt("hello", 3), "khoor")
        self.assertEqual(encrypt("world", 5), "btwqi")
        self.assertEqual(encrypt("abc", 1), "bcd")

    def test_basic_decryption(self):
        """Verify that basic English strings are shifted backward correctly."""
        self.assertEqual(decrypt("khoor", 3), "hello")
        self.assertEqual(decrypt("btwqi", 5), "world")
        self.assertEqual(decrypt("bcd", 1), "abc")

    def test_case_preservation(self):
        """Verify that upper and lowercase letters retain their original case after shifts."""
        self.assertEqual(encrypt("Hello World", 4), "Lipps Asvph")
        self.assertEqual(decrypt("Lipps Asvph", 4), "Hello World")
        self.assertEqual(encrypt("PyThOn", 10), "ZiDrYx")
        self.assertEqual(decrypt("ZiDrYx", 10), "PyThOn")

    def test_non_alphabetic_characters(self):
        """Verify that numbers, punctuation, spaces, and symbols remain unchanged."""
        plaintext = "Prodigy InfoTech Task-01: Caesar Cipher (2026)!"
        ciphertext = "Rtqfkia KphqVgej Vcum-01: Ecguct Ekrjgt (2026)!"
        
        # Test with a shift of 2
        self.assertEqual(encrypt(plaintext, 2), ciphertext)
        self.assertEqual(decrypt(ciphertext, 2), plaintext)

    def test_large_shift_values(self):
        """Verify that shifts larger than 26 wrap around correctly (modulo 26 arithmetic)."""
        # Shift 29 is equivalent to shift 3 (29 % 26 = 3)
        self.assertEqual(encrypt("xyz", 29), "abc")
        self.assertEqual(decrypt("abc", 29), "xyz")
        
        # Shift 52 is equivalent to shift 0 (52 % 26 = 0)
        self.assertEqual(encrypt("python", 52), "python")
        self.assertEqual(decrypt("python", 52), "python")
        
        # Shift 100 is equivalent to shift 22 (100 % 26 = 22)
        self.assertEqual(encrypt("hello", 100), "dahhk")
        self.assertEqual(decrypt("dahhk", 100), "hello")

    def test_negative_shift_values(self):
        """Verify encryption and decryption with negative shift values."""
        # A negative shift of -3 in encryption moves letters backwards (same as decryption with +3)
        self.assertEqual(encrypt("def", -3), "abc")
        self.assertEqual(decrypt("abc", -3), "def")
        
        # Shift of -29 is equivalent to shift -3 (or +23)
        self.assertEqual(encrypt("abc", -29), "xyz")
        self.assertEqual(decrypt("xyz", -29), "abc")

    def test_zero_shift(self):
        """Verify that a shift of 0 results in no change to the text."""
        self.assertEqual(encrypt("Secure Code 101", 0), "Secure Code 101")
        self.assertEqual(decrypt("Secure Code 101", 0), "Secure Code 101")


if __name__ == "__main__":
    unittest.main()