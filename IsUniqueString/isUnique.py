# This program will determine if every character
# in the string is unique. This is assuming every
# charatcer in the string can be any ASCII charatcer

def isUniqueASCII(input):
    vector = [False] * 128
    for c in input:
        value = ord(c)
        if vector[value] == True:
            return False
        vector[value] = True
    return True


