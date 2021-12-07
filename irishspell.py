# Python program to defining a lanaguage model for unsupervised spell checking specifically for Irish language
# Importing the necessary modules to be used in the program
# MIT license: www.opensource.org/licenses/mit-license.php
import re # Regular Expressions
from collections import Counter
import string
from flask_cors import CORS

# Defining the language model and error model
def words(text):
    return re.findall(r'\w+', text.lower()) 

WORDS = Counter(words(open('bible.txt', encoding="utf-8").read()))

def P(word, N=sum(WORDS.values())):
    # Probability of word
    return WORDS[word] / N


def correction(word):
    # Most probable spelling correction for word
    return max(candidates(word), key=P)


def candidates(word):
    # Generate possible spelling corrections for word.
    return (known([word]) or known(level_one_edit(word)) or known(level_two_edit(word)) or [word])


def known(words):
    # The subset of `words` that appear in the dictionary of WORDS.
    return set(w for w in words if w in WORDS)


def level_one_edit(word):
    # All edits that are one edit away from word.
    letters    = 'áéíóúabcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    swap       = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + swap + replaces + inserts)


def level_two_edit(word):
    # All edits that are two edits away from word.
    return (e2 for e1 in level_one_edit(word) for e2 in level_one_edit(e1))  

# function to handle invalid irish words
def isValidWord(word):

    #check for valid irish words
    letters    = 'áéíóúabcdefghijklmnopqrstuvwxyz'
    isValidWord = False

    if word == "\\n":
        return False
               

    for wordletter in word:
        if wordletter in letters:
            isValidWord = True
            break
        
    if isValidWord:
        return True
    else:
        return False

def read_file(filename):

    #check for valid irish words
    letters    = 'áéíóúabcdefghijklmnopqrstuvwxyz'

    file = open(filename, encoding="utf-8")

    f = open("newOutput.txt", "a", encoding="utf-8")

    for fileLine in file:
        # Get line of file and covert it to a list
        wordRow = fileLine.split()
        isValidWord = False

        for testWord in wordRow:
            if testWord == "\\n":
               break
               

            for wordletter in testWord:
                if wordletter in letters:
                    isValidWord = True
                    break
        
        if isValidWord:
            irishWord = testWord.strip()

          #print(irishWord)
            f.write(f"{correction(irishWord)}\n")
            # print(correction(irishWord))
        else:
            f.write(f"{testWord}\n")

    file.close()

# Test Code
if __name__ == '__main__':
    read_file("input-test.txt")
