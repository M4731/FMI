import sys

def BF(start, list, n):
    distance = [sys.maxsize]*n
    tati = [-1]*n
    distance[start] = 0  

    for i in range(n-1):
        for x in list:
            if distance[x[0]] + x[2] < distance[x[1]]:
                distance[x[1]] = distance[x[0]] + x[2]
                tati[x[1]] = x[0]

    for x in list:
        if distance[x[0]] + x[2] < distance[x[1]]:
            return["nu merge bo$$"]
    
    result = []
    for i in range(n):
        result.append((i,distance[i]))
    return result



f = open("zgrafpond.in","r")
list = []

l = f.readline()
n = int(l.split()[0])
m = int(l.split()[1])

l = f.readline()
while l:
    list.append((int(l.split()[0])-1, int(l.split()[1])-1, int(l.split()[2])))
    l = f.readline()


print(BF(0, list, n))
f.close()   