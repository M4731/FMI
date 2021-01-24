import sys

def FW(w, n):
    distance = w
    tati = [[-1]*n for i in range(n)] 

    for i in range(n):
        for j in range(n):
            distance[i][j] = w[i][j]
            if w[i][j] == 0 or w[i][j] == sys.maxsize:
                tati[i][j] = -1
            else:
                tati[i][j] = i
                
    for k in range(n):
        for i in range(n): 
            for j in range(n):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    tati[i][j] = tati[k][j] 
    return distance



f = open("zgrafpond.in","r")
list = []

l = f.readline()
n = int(l.split()[0])
m = int(l.split()[1])
w = [[sys.maxsize]*n for i in range(n)] 
for i in range(n):
    w[i][i] = 0

l = f.readline()
while l:
    w[int(l.split()[0])-1][int(l.split()[1])-1] = int(l.split()[2])
    l = f.readline()

print(*FW(w, n),sep="\n")
f.close()  