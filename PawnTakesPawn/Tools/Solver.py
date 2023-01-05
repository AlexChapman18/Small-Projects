#You know some letters but not the exact positions or length

def Solve():
    Words = []
    testWord = input('Please input a word to solve.\nUse Spaces to signify unkown letters: ').lower()
    Spaces = input("How many more spaces till the end of the word do you believe?")
    for i in range(0, (int(Spaces)-1)):
        nonBlanks = len(testWord)-testWord.count(' ')
        Dictionary = open("C:/Documents/Coding/1PawnTakesPawn/Tools/Dictionary/1Dictionary.txt",'r')
        for word in Dictionary:
            word = (word.replace(" ", "").replace("\n", ""))
            incLetter = 0
            incMatch = 0
            if len(word) == len(testWord):
                for letter in testWord:
                    if letter == word[incLetter]:
                        incMatch += 1
                    incLetter += 1
                if incMatch == nonBlanks:
                    Words.append(word)
        testWord += (" ")
    return Words

