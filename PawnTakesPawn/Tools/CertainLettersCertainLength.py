#put in the letters you know, and the min/max length you belive it is

def CLCL():
    testWord = input('Please input the known letters.\n>>>').lower()
    minLength = input("Please input min possible length.\n>>>")
    maxLength = input("Please input max possible length.\n>>>")
    Dictionary = open("C:/Documents/Coding/1PawnTakesPawn/Tools/Dictionary/1Dictionary.txt",'r')
    possWords = []
    for word in Dictionary:
        if maxLength != "":
            word = (word.replace(" ", "").replace("\n", "-"))
            if (int(minLength)+1) > len(word) or len(word) > (int(maxLength)+1):
                continue
        tempWord = list(testWord)
        for letter in word:
            letterNum = 0
            if len(tempWord) == 0:
                word = (word.replace("-", ""))
                possWords.append(word)
                break
            for letter2 in tempWord:
                if letter == letter2:
                    del tempWord[letterNum]
                    fail = False
                    break
                letterNum += 1
    return possWords
