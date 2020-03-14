import pytest
from security import Security
from io import StringIO
s = Security()
shift = StringIO("3\n")
def test_CaesarEncrypt_Output_Type(monkeypatch):
    monkeypatch.setattr('sys.stdin', shift)
    ciphertext = s.CaesarEncryptor("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(),./[]")
    assert type(ciphertext) is str
def test_CaesarEncrypt_Output(monkeypatch):
    monkeypatch.setattr('sys.stdin', shift)
    ciphertext = s.CaesarEncryptor("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(),./[]")
    assert ciphertext != "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(),./[]"
def test_CaesarDecrypt_Output_Type(monkeypatch):
    monkeypatch.setattr('sys.stdin', shift)
    ciphertext = s.CaesarDecryptor("XYZABCDEFGHIJKLMNOPQRSTUVWxyzabcdefghijklmnopqrstuvw7890123456/[]!@#$%^&*(),.")
    assert type(ciphertext) is str
def test_CaesarDecrypt_Output(monkeypatch):
    monkeypatch.setattr('sys.stdin', shift)
    ciphertext = s.CaesarDecryptor("XYZABCDEFGHIJKLMNOPQRSTUVWxyzabcdefghijklmnopqrstuvw7890123456/[]!@#$%^&*(),.")
    assert ciphertext != "XYZABCDEFGHIJKLMNOPQRSTUVWxyzabcdefghijklmnopqrstuvw7890123456/[]!@#$%^&*(),."