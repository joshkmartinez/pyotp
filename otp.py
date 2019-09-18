import sys
import itertools
import binascii
s = "hello world"  # message or ciphertext
password = "12345 12345"
switch = 0  # 0 to encrypt - 1 to decrypt
p = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C',
     'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']  # no numbers for you boi


def xor(msg, key):
    # This should work with a key shorter than the msg?
    return ''.join([chr(ord(x) ^ ord(y)) for x, y in zip(msg, itertools.cycle(key))])


def encrypt(msg, key):
    out = xor(msg, key)
    return (binascii.hexlify(out.encode())).decode()


def decrypt(cipher, key):
    out = (binascii.unhexlify(cipher.encode())).decode()
    return xor(out, key)


if (len(s) != len(password) and switch == 0):
    print("The password must be the same length as the message.")
    sys.exit()

split = list(s)
if switch == 0:
    for x in split:
        if x in p:
            pass
        else:
            print("The only supported characters are uppercase and lowercase letters. Dont complain, I even included support for spaces, just for you!")
            sys.exit()

if(switch == 1):
    print("Here is the plaintext: \n" + decrypt(s, password))
else:
    print("Here is the ciphertext: \n" + encrypt(s, password))
