


with open("input-server-6655.txt") as f:
    lines = [line.rstrip() for line in f]

T = int(lines[0])
whereSpace = lines[1].find(" ")
whereSpace2 = lines[1].rfind("")
N = int(lines[1][0:whereSpace])
P = int(lines[1][whereSpace+1:whereSpace2])


def intSepperator(Line):
    intArray = []
    firstPoint = 0
    secondPoint = lines[Line].find(" ")
    for i in range (0, (N-1)):
        intArray.append(int(lines[Line][firstPoint:secondPoint]))
        firstPoint = secondPoint + 1
        secondPoint = lines[Line].find(" ", firstPoint)
        

    secondPoint = lines[Line].rfind(" ")
    intArray.append(int(lines[Line][(secondPoint):(len(lines[Line])+1)]))
    return(intArray)


def chooser(intArray, N, P):
    t1 = 9999999


    for i in range(0, N):
        print(i)

        n1, n2, n3 = keepAdder(intArray, i, P, N)
        if n1 < t1 and n1 >= P:
            t1 = n1
            t2 = n2
            t3 = n3
        else:
            pass
    return (t2), (t3)

def keepAdder(array, l, P, N):
    total = 0
    r = l
    while l < N and (total) < P:
        total += array[l]
        l = l + 1
    return total, r, (l-1)


file2= open("answers.txt","a")
for i in range(1, (T+1)):
    print(i)
    whereSpace = lines[((i*2)-1)].find(" ")
    whereSpace2 = lines[((i*2)-1)].rfind("")
    N = int(lines[((i*2)-1)][0:whereSpace])
    P = int(lines[((i*2)-1)][whereSpace+1:whereSpace2])
    n2, n3 = chooser(intSepperator((i*2)), N, P)
    file2.writelines("Case #"+str(i)+": "+str(n2)+" "+str(n3))
    file2.write("\n")

file2.close()
