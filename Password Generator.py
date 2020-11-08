import random
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)
uppercaseLetter1 = chr(random.randint(65,90))
uppercaseLetter2 = chr(random.randint(65,90))
lowercaseLetter1 = chr(random.randint(97,122))
lowercaseLetter2 = chr(random.randint(97,122))
number1 = chr(random.randint(48,57))
number2= chr(random.randint(48,57))
symbol1 = chr(random.randint(33,34))
symbol2 = chr(random.randint(40,42))
password = uppercaseLetter1 + uppercaseLetter2 +uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 +lowercaseLetter2+ number1 + number2 + symbol1 + symbol2
shuffle(password)

print(password)