"""Write a code that will remove vowels from a string and run it for the sentence:

'Computer Science Makes the World go round but it doesn't make the world round itself!'

Print the save the result as the variable = NoVowels
"""

def RemoveVowels(NormText):
    CipherText = ''
    for ch in NormText:
        if ch == 'a':
            CipherText += ''
        elif ch == 'e':
            CipherText += ''
        elif ch == 'i':
            CipherText += ''
        elif ch == 'o':
            CipherText += ''
        elif ch == 'u':
            CipherText += ''
        elif ch == 'A':
            CipherText += ''
        elif ch == 'E':
            CipherText += ''
        elif ch == 'I':
            CipherText += ''
        elif ch == 'O':
            CipherText += ''
        elif ch == 'U':
            CipherText += ''
        else:
            CipherText += ch
    return CipherText

NoVowels = RemoveVowels('Computer Science Makes the World go round but it doesn\'t make the world round itself!')

"""Write an encryption code that you make up and run it for the variable NoVowels"""

def removeChar(string, idx):
    return string[:idx] + string[idx+1:]
def keyGen():
    import random
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    key = ""
    for i in range(len(alphabet)):
        ch = random.randint(0,26-i)
        key += alphabet[ch]
        alphabet = removeChar(alphabet,ch)
    return key

CipherAlphabet = keyGen()
alphabet = "abcdefghijklmnopqrstuvwxyz "

def SubEncryption(string):
    CipherText = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    string = string.lower()
    for ch in string:
        idx = alphabet.find(ch)
        CipherText += CipherAlphabet[idx]
    return CipherText
print(SubEncryption(NoVowels))
