#Credit - Raghav Agrawal
'''
A quick and easy encryption/decryption module - Credit - Raghav Agrawal

A quick guide to using the enigma module - Credit to Raghav Agrawal

1) First, import enigma:
import enigma

2)Create an enigma instance:
mystery = enigma.enigma()

3)Encrypt a message
mystery.encrypt("Have fun today!")

4) Decrypt a message
mystery.decrypt("<Your Encryption>")

5) Use repr() to see everything you've encrypted
repr(mystery)

Have fun!
'''
import urllib
class enigma:
    #Class instances and properties defined below#
    _ = "abcdefghijklmnopqrstuvwxyz"
    key = {}
    for idx, item in enumerate(_):
        key[item] = idx + 1
    del idx
    del item
    del _
    def __init__(self):
        self.data = []
    def encrypt(self, data = "ENIGMA"):
        self.data.append(data)
        data = str(data)
        asciis = [ord(x) for x in data]
        alphas = []
        for item in data:
            if item.upper() != item.lower():
                alphas.append(str(self.key[item.lower()]))
            else:
                alphas.append(0)
        str_ = ""
        for idx, item in enumerate(data):
            str_+=str(chr(asciis[idx]+int(alphas[idx])+idx))
            str_+="plus"+str(alphas[idx])
            str_+= "raghav"
        str_ = str_[0:len(str_)-6]
        str__ = ":".join([str(ord(item)) for item in str_])
        _str = [chr(int(item) + idx) for idx, item in enumerate(str__.split(":"))]
        return urllib.parse.quote("".join(_str))
    def decrypt(self, data):
        data = urllib.parse.unquote(data)
        zero = []
        for idx, item in enumerate(data):
            zero.append(str(ord(item)-idx))
        zero = ":".join(zero)
        first = "".join([chr(int(x)) for x in zero.split(":")])
        second = first.split("raghav")
        third = ""
        for idx, item in enumerate(second):
            temp = item.split("plus")
            third += chr(ord(temp[0]) - (int(temp[1]) + idx))
        return third
    def __str__(self):
        return "An enigma object"
    def __repr__(self):
        return str(tuple(self.data))
mystery = enigma()
