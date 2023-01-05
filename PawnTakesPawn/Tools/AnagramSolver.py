#Solves anagrams


def Anagram():
    letters = input("Input Letters\n>>>")
    from collections import Counter
    import sys
    with open('C:/Documents/Coding/1PawnTakesPawn/Tools/Dictionary/1Dictionary.txt', 'r') as f:
        dictionary = f.read()
        dictionary = [x.lower() for x in dictionary.split('\n')]
    assert isinstance(letters, str)
    
    letters = letters.lower()
    letters_count = Counter(letters)
    anagrams = []
    for word in dictionary:
        if not set(word) - set(letters):
            check_word = set()
            for k, v in Counter(word).items():
                if v == letters_count[k]:
                    check_word.add(k)
            if check_word == set(word):
                if len(word) == len(letters):
                    anagrams.append(word)

    print(anagrams)
    return anagrams

