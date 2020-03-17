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
        cipherucalphabet = collections.deque("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        cipherlcalphabet = collections.deque("abcdefghijklmnopqrstuvwxyz")
        ciphernumbers = collections.deque("0123456789")
        ciphersymbols = collections.deque("!@#$%^&*(),./[]")
        cipherucalphabet.rotate(shift)
        cipherlcalphabet.rotate(shift)
        ciphernumbers.rotate(shift)
        ciphersymbols.rotate(shift)
        cipherucalphabet = "".join(list(cipherucalphabet))
        cipherlcalphabet = "".join(list(cipherlcalphabet))
        ciphernumbers = "".join(list(ciphernumbers))
        ciphersymbols = "".join(list(ciphersymbols))
        i=0
        for i in range(len(ucalphabet)):
            if ucalphabet[i] in plaintext:
                ciphertext = ciphertext + cipherucalphabet[i]
            i+1
        for i in range(len(lcalphabet)):
            if lcalphabet[i] in plaintext:
                ciphertext = ciphertext + cipherlcalphabet[i]
            i+1
        for i in range(len(numbers)):
            if numbers[i] in plaintext:
                ciphertext = ciphertext + ciphernumbers[i]
            i+1
        for i in range(len(symbols)):
            if symbols[i] in plaintext and len(symbols)<=16:
                ciphertext = ciphertext + ciphersymbols[i]
            i+1
        filename = input("Please enter a file name: ").strip()
        if not ".txt" in filename:
            filename += ".txt"
        path = Path(filename)
        if path.exists():
            path.write_text(ciphertext)
        else:
            open(filename, "x")
            path.write_text(ciphertext)

    def CaesarDecryptor(self, plaintext):
        shift = int(input("Please enter a number to shift text by: "))
        ciphertext = ""
        ucalphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lcalphabet = "abcdefghijklmnopqrstuvwxyz"
        numbers = "0123456789"
        symbols = "!@#$%^&*(),./[]"
        cipherucalphabet = collections.deque("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        cipherlcalphabet = collections.deque("abcdefghijklmnopqrstuvwxyz")
        ciphernumbers = collections.deque("0123456789")
        ciphersymbols = collections.deque("!@#$%^&*(),./[]")
        cipherucalphabet.rotate(shift)
        cipherucalphabet.rotate(shift)
        ciphernumbers.rotate(shift)
        ciphersymbols.rotate(shift)
        shift = int("-" + str(shift))
        cipherucalphabet.rotate(shift)
        cipherucalphabet.rotate(shift)
        ciphernumbers.rotate(shift)
        ciphersymbols.rotate(shift)
        cipherucalphabet = "".join(list(cipherucalphabet))
        cipherlcalphabet = "".join(list(cipherlcalphabet))
        ciphernumbers = "".join(list(ciphernumbers))
        ciphersymbols = "".join(list(ciphersymbols))
        i=0
        for i in range(len(ucalphabet)):
            if ucalphabet[i] in plaintext:
                ciphertext = ciphertext + cipherucalphabet[i]
            i+1
        for i in range(len(lcalphabet)):
            if lcalphabet[i] in plaintext:
                ciphertext = ciphertext + cipherlcalphabet[i]
            i+1
        for i in range(len(numbers)):
            if numbers[i] in plaintext:
                ciphertext = ciphertext + ciphernumbers[i]
            i+1
        for i in range(len(symbols)):
            if symbols[i] in plaintext and len(symbols)<=16:
                ciphertext = ciphertext + ciphersymbols[i]
            i+1
        filename = input("Please enter a file name: ").strip()
        if not ".txt" in filename:
            filename += ".txt"
        path = Path(filename)
        if path.exists():
            path.write_text(ciphertext)
        else:
            open(filename, "x")
            path.write_text(ciphertext)

    def PolySubEncryptor(self, plaintext):
        pass

    def PolySubDecryptor(self, plaintext):
        plaintext = ""
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789\n ~`!@#$%^&*()_-+=<>,.?/\|[]{};:"
        letter_to_index = dict(zip(alphabet, range(len(alphabet))))
        index_to_letter = dict(zip(range(len(alphabet)), alphabet))
        if type(self.key) == int:
            self.key = str(self.key)
        split_ciphertext = [ciphertext[i:i + len(self.key)] for i in range(0, len(ciphertext), len(self.key))]
        for each_split in split_ciphertext:
            i = 0
            for letter in each_split:
                number = (letter_to_index[letter] - letter_to_index[self.key[i]]) % len(alphabet)
                plaintext += index_to_letter[number]
                i += 1
        return(plaintext)
