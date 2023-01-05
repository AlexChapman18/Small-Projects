#You may know some letters but are not sure which ones are correct or not, but you do know the length

def Dejumble(UseWord = "", MaxItteration = "", StartPoint = 0, Itteration = 0):
    if Itteration == 0:
        tWord = input('Please input a word to solve.\n>>>').lower()
        MaxItteration = int(input("How many assumed wrong letters.\n>>>"))
        Words = []
    Alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    Dictionary = open("C:/Documents/1PawnTakesPawn/Tools/Dictionary/"+ tWord[0].upper() + ".txt",'r')
    for i in range(StartPoint, len(UseWord)):
        nextStartPoint = i + 1
        Holder = UseWord[i]
        for x in range(0, 26):
            UseWord[i] = Alphabet[x]
            for word in Dictionary:
                if "".join(UseWord) == (word.replace(" ", "").replace("\n", "")):
                    Words.append("".join(UseWord))
            if (Itteration+1) < MaxItteration:
                Dejumble(UseWord, MaxItteration, nextStartPoint, (Itteration+1))
        UseWord[i] = Holder
    return Words

