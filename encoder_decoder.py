from encodings import utf_8
from cryptography.fernet import Fernet
import os

def genwrite_key():
    key = Fernet.generate_key()
    with open("pass.key", "wb") as key_file:
        key_file.write(key)

def call_key():
    return open("pass.key","rb").read()

def create_cipher():
    key=get_key_from_jenkins_env()
    return Fernet(key)

def encode(text):
    cipher = create_cipher()  
    if (isinstance(text, (bytes, bytearray))):
      return cipher.encrypt(text)
    else:
      print("Text must be converted to Bytes")

def decode(text):
    cipher = create_cipher()
    if (isinstance(text, (bytes, bytearray))):
      return cipher.decrypt(text)
    else:
      print("Text must be converted to Bytes")

def get_key_from_jenkins_env():
    KEY = 'encpUq6k2X_K3BGZWvujQyCpAkR8S6k_CiHZxxki7kA='
    return bytes(KEY, 'utf_8')
