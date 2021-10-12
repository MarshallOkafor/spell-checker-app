#SpellChecker

#Function fetching comparable words from dictionary
def readdictionaryfile(dictionaryfilename):
    dictionarywords = []
    inputfile = open(dictionaryfilename, "r")
    for line in inputfile:
        word = line.strip()
        dictionarywords.append(word)
    inputfile.close()
    return dictionarywords

#Function fetching words/text for evaluation
def readtextfile(textfilename):
    words = []
    inputfile = open(textfilename, "r")
    for line in inputfile:
        wordsonline = line.strip().split()
        for word in wordsonline:
            words.append(word.strip(".,!\":;?").lower())
    inputfile.close()
    return words

#Dictionary & Text comparison function
def finderrors(dictionarywords, textwords):
    incorrectwords = []
    for word in textwords:
        if word not in dictionarywords:
            incorrectwords.append(word)
    return incorrectwords

#Printing errors - Temporary function
def printerrors(errorlist):
    print("The misspelled words are: ")
    for word in errorlist:
        print(word)


def main():
    dictionaryfile = input("Please enter the dictionary file: ")
    textfile = input("Please enter the text file: ")
    dictionarylist = readdictionaryfile(dictionaryfile)
    textlist = readtextfile(textfile)
    errorlist = finderrors(dictionarylist, textlist)
    printerrors(errorlist)


main()
