import collections
from pathlib import Path
class Security(object):

    def __init__(self, plaintext):
        #super().__init__()
        pass

    def CaesarEncryptor(self, plaintext):
        shift = int(input("Please enter a number to shift text by: "))
        ciphertext = ""
        ucalphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lcalphabet = "abcdefghijklmnopqrstuvwxyz"
        numbers = "0123456789"
        symbols = "!@#$%^&*(),./[]"
        cipherucalhabet = collections.deque[ucalphabet]
        cipherlcalhabet = collections.deque[lcalphabet]
        ciphernumbers = collections.deque[numbers]
        ciphersymbols = collections.deque[symbols]
        cipherucalhabet = cipherucalhabet.rotate(shift)
        cipherlcalhabet = cipherucalhabet.rotate(shift)
        ciphernumbers = ciphernumbers.rotate(shift)
        ciphersymbols = ciphersymbols.rotate(shift)
        for i in len(plaintext):
            if ucalphabet in plaintext:
                ciphertext = ciphertext + cipherucalhabet[i]
            if lcalphabet in plaintext:
                ciphertext = ciphertext + cipherlcalhabet[i]
            if numbers in plaintext:
                ciphertext = ciphertext + ciphernumbers[i]
            if symbols in plaintext:
                pass
        filename = input("Please enter a file name: ").strip()
        if not ".txt" in filename:
            filename += ".txt"
        path = Path(filename)
        if path.exists():
            path.write_text()
        else:
            open(filename, "x")
            path.write_text()

    def CaesarDecryptor(self, plaintext):
        pass

    def PolySubEncryptor(self, plaintext):
        pass

    def PolySubDecryptor(self, plaintext):
        pass
