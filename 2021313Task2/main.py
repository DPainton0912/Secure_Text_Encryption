from pathlib import Path
from security import Security
def __main__():
    fileinput = input("Please enter a file name: ").strip()
    if not ".txt" in fileinput:
        fileinput += ".txt"
    pathinput = Path(fileinput)
    if pathinput.exists():
        plaintext = pathinput.read_text()
    else:
        open(fileinput, "x")
        plaintext = pathinput.read_text()
    cryptinput = False
    while cryptinput == False:
        crypt = input("Encryption (e) or Decryption (d)? ").strip().lower()
        if crypt == "e":
            cryptinput = True
            encryption = True
        elif crypt == "d":
            cryptinput = True
            encryption = False
        else:
            print("Please select an option and try again.")
    methodinput = False
    while methodinput == False:
        method = input("Caesar cipher (c) or Polyalphabetic cipher (p)? ").strip().lower()
        keyinput = False
        while keyinput == False:
            key = input("Please enter a number to shift text by for Caesar cipher or a word/random collection of letters for Polyalphabetic cipher: ").strip()
            if method == "c":
                try:
                    key = int(key)
                    keyinput = True
                except:
                    print("Something went wrong.")
            else:
                keyinput = True
        s = Security(key)
        if encryption == True and method == "c" and type(key) is int:
            ciphertext = s.CaesarEncryptor(plaintext)
            methodinput = True
        elif encryption == False and method == "c" and type(key) is int:
            ciphertext = s.CaesarDecryptor(plaintext)
            methodinput = True
        elif encryption == True and method == "p":
            ciphertext = s.PolySubEncryptor(plaintext)
            methodinput = True
        elif encryption == False and method == "p":
            ciphertext = s.PolySubDecryptor(plaintext)
            methodinput = True
        else:
            print("Please select an option and try again.")

    def WriteToFile(ciphertext):
        fileoutput = input("Please enter a file name: ").strip()
        if not ".txt" in fileoutput:
            fileoutput += ".txt"
        pathoutput = Path(fileoutput)
        if pathoutput.exists():
            pathoutput.write_text(ciphertext)
        else:
            open(fileoutput, "x")
            pathoutput.write_text(ciphertext)
        print("Please refer to new file to see encrypted or decrypted text.")

    WriteToFile(ciphertext)

if __name__ == "__main__":
    __main__()

