from pathlib import Path
from security import Security
def main():
    filename = input("Please enter a file name: ").strip()
    if not ".txt" in filename:
        filename += ".txt"
    path = Path(filename)
    if path.exists():
        contents = path.read_text()
    else:
        open(filename, "x")
        contents = path.read_text()
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
        if encryption == True and method == "c":
            Security.CaesarEncryptor("first", contents)
            methodinput = True
        elif encryption == False and method == "c":
            Security.CaesarDecryptor(contents)
            methodinput = True
        elif encryption == True and method == "p":
            Security.PolySubEncryptor(contents)
            methodinput = True
        elif encryption == False and method == "p":
            Security.PolySubDecryptor(contents)
            methodinput = True
        else:
            print("Please select an option and try again.")



# if __name__ == "main":
#     main()
#     pass
main()