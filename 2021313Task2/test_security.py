import pytest
from security import Security
key = 15
s = Security(key)
plaintext = """Top 10 Programming Languages 2017 (hackernoon.com)
1- Python - Python Software Foundation
2- C - Dennis Ritchie & Bell Labs
3- Java - Oracle Corporation
4- C++ - Bell Labs
5- C# - Microsoft
6- R - R Core Team
7- JavaScript - Netscape
8- PHP - Zend Technologies
9- Go - Google
10- Swift - Apple"""
def test_CaesarEncrypt_Output_Type():
    ciphertext = s.CaesarEncryptor(plaintext)
    assert type(ciphertext) is str
def test_CaesarEncrypt_Output():
    ciphertext = s.CaesarEncryptor(plaintext)
    assert ciphertext != plaintext
def test_CaesarDecrypt_Output_Type():
    ciphertext = s.CaesarDecryptor(plaintext)
    assert type(ciphertext) is str
def test_CaesarDecrypt_Output():
    ciphertext = s.CaesarDecryptor(plaintext)
    assert ciphertext != plaintext