from base64 import b64decode

def decode(text):
  return b64decode(text).decode('utf8')