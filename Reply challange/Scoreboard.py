def logwriter(score):#puts the log into list
    log=[0,0,0,0,0]
    for t in range(0,5):
        log[t]=int(score[0:score.find(" ")])
        score=score[score.find(" ")+1:]
    return log

def sort(Teams,N):#sorts the teams
    NotSwapped=True
    while NotSwapped:
        NotSwapped=False
        for i in range(N-1):
            if Teams[i][0]<Teams[i+1][0]:
                Teams[i],Teams[i+1]=Teams[i+1],Teams[i]
                NotSwapped=True
            elif Teams[i][0]==Teams[i+1][0]:
                if Teams[i][1]>Teams[i][1]:
                    Teams[i],Teams[i+1]=Teams[i+1],Teams[i]
                    NotSwapped=True
    return [str(Teams[c][2]) for c in range(N)]
                
            

file= open("input.txt","r")
tests=int(file.readline())
for i in range(tests):
    nl=file.readline()
    N=int(nl[0:nl.find(" ")])
    L=int(nl[nl.find(" ")+1:])
    Teams=[[[0,0,0,0,0],[[0,0,0,0,0] for k in range(0,5)], c+1] for c in range(0,N)]

    for u in range(0,L):#puts in the list Teams [score, penalty, teamNumber]
        log=logwriter(file.readline())
        if log[4]==1:
            TeamNo=log[1]-1
            Teams[TeamNo][0][log[2]-1]+=log[3]*100
            if Teams[TeamNo][1][log[2]-1][log[3]-1]==0:
                Teams[TeamNo][1][log[2]-1][log[3]-1]=log[0]
    for z in range(N):
        penalty=0
        Teams[z][0]=Teams[z][0][0]+Teams[z][0][1]+Teams[z][0][2]+Teams[z][0][3]+Teams[z][0][4]
        for g in range(0,5):
            for h in range(0,5):
                penalty+=Teams[z][1][g][h]
        Teams[z][1]=penalty
                                         
    standings = sort(Teams, N)
    file2= open("answers.txt","a")
    file2.writelines("Case #"+str(i+1)+": "+ " ".join(standings))
    file2.write("\n")
    file2.close()
file.close()
