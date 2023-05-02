from code_challenges.hashtables.hashtable import Hashtable
import re


def first_repeated_word(str):
    temp = ''
    hashtable = Hashtable()
    letters = r'^[a-zA-Z]'
    for char in str:
        if char in [' ', '\n']:
            temp = temp.lower()
            if hashtable.has(temp):
                return temp
            elif temp != '':
                hashtable.set(temp, temp)
                temp = ''
        elif re.match(letters, char):
            temp += char
    if hashtable.has(temp):
        return temp

