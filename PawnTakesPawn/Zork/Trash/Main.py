#Web brute force
import requests

Dictionary = open("Words.txt", "r")
CompareValue = ((requests.get('https://pawntakespawn.com/Omgealol')).text).find("guydaiuywadbaowubdwabdaiuwd")


for Word in Dictionary:
    TextUrl = "https://pawntakespawn.com/" + (Word.replace(" ", "").replace("\n", "")) + "quest"
    print(TextUrl)
    UrlData = (requests.get(TextUrl)).text
    if UrlData.find("Not Found") == CompareValue:
        print("Success")
        f = open("CorrectUrls.txt", "a")
        f.write(TextUrl)
        f.close()
        break
    else:
        print("Fail")
