#Execute all other programs
#Web brute force
from WebDictionary import Attack
#Solves anagrams
from AnagramSolver import Anagram
#put in the letters you know, and the min/max length you belive it is
from CertainLettersCertainLength import CLCL
#You may know some letters but are not sure which ones are correct or not, but you do know the length
from Dejumbler import Dejumble
#You know some letters but not the exact positions or length
from Solver import Solve




def Main(SecondLevel = 0):
    while True:
        Choice = int(input("Choose One of the follow options:\n 1 :Choose words to manually brute force\n 2 :Anagram solver\n 3 :CLCL put in the letters you know, and the min/max length you belive it is\n 4 :Spelling corrector\n 5 :You know some letters but not the exact length or position\n>>>"))
        if Choice == 1:
            Words = input("Input word\n>>>")
        elif Choice == 2:
            Words = Anagram()
        elif Choice == 3:
            Words = CLCL()
        elif Choice == 4:
            Words = Dejumble()
        else:
            Words = Solve()
        if SecondLevel == 1:

            return Words
            break
        testWord = input("Would you like to test the word?\n>>>")
        if testWord == "n":
            break
        SecondLevel = input("Would you like to test it with other words aswell?\n>>>")
        Words2 = []
        if SecondLevel == "y":
            Words2 = Main(1)
            Position = input("Before or after?\n>>>").lower()
            if Position == "b":
                for WordsTwo in Words2:
                    Attack(Words, WordsTwo)
            else:
                for WordsTwo in Words2:
                    Attack(Words, "", WordsTwo)

        else:
            Attack(Words)



            
while True:
    Main()