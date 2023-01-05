#Web brute force

def Attack(Words, Pre = "", Post = "", PrePre = "", PostPost = ""):
    import time
    import requests
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("InTrial")
    loadBar = ("[--------------------------------------------------]")
    Count = 0
    progress = 0
    print(loadBar)
    CompareValue = ((requests.get('https://pawntakespawn.com/Omgealol')).text).find("asdwer")
    for Word in Words:
        TextUrl = "https://pawntakespawn.com/" + PrePre + Pre + (Word.replace(" ", "").replace("\n", "")) + Post + PostPost
        UrlData = (requests.get(TextUrl)).text
        print(TextUrl)
        Count += 1
        if UrlData.find("Not Found") == CompareValue:
            print("Success")
            print(TextUrl)
            f = open("SuccessfulURL.txt", "a")
            f.write(TextUrl)
            f.close()
            break
        else:
            if (Count / len(Words))*100 >= progress:
                progress += (len(Words)/50)
                loadBar = loadBar.replace("-", "#", 1)
                print(loadBar)
    print("Fail")



#import threading
#threads = []
#for file in (files):
#    t = threading.Thread(target=Trial, args=(file, Ending))
#    threads.append(t)
#    t.start()
