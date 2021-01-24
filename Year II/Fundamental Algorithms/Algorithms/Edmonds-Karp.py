import sys
import queue

def lista_adiacenta(n,m,list,o):
    matx = [[]for i in range(n+1)] 

    if o == "neorientat":
        for i in list:
            matx[i[0]].append((i[1],i[2]))
            matx[i[1]].append((i[0],i[2]))
    elif o == "orientat":
        for i in list:
            matx[i[0]].append((i[1],i[2]))

    return matx

visited = []

def BFS(start, list, finish, tati, rest):
    q = queue.Queue()
    q.put(start)
    global visited
    visited = [start]

    while not q.empty():
        nod = q.get()
        for j in list[nod]:
            index = j[0]
            if rest[nod][index] and index not in visited:
                visited.append(index)
                tati[index] = nod
                if(index != finish):
                    q.put(index)
    return (finish in visited)


def EK(start, finish, list, n, rest):
    tati = [0]*(n+1)
    global visited
    flow = 0
    while BFS(start, list, finish, tati, rest):
        for i in list[n]:
            index = i[0]
            if index in visited and rest[index][n]:
                x = sys.maxsize
                tati[n] = index
                j = n
                while j != start:
                    x = min(x,rest[tati[j]][j])
                    j = tati[j]
                j = n
                while j != start:
                    rest[tati[j]][j] -= x
                    rest[j][tati[j]] += x
                    j = tati[j]
                flow += x
    return flow
            

f = open("zgrafpond.in","r")
list = []

n = int(f.readline())
l = f.readline()
start = int(l.split()[0])
finish = int(l.split()[1])
m = int(f.readline())


rest = [[0]*(n+1) for i in range (n+1)]

l = f.readline()
while l:
    list.append((int(l.split()[0]), int(l.split()[1]), int(l.split()[2])))
    rest[int(l.split()[0])][int(l.split()[1])] = int(l.split()[2])
    l = f.readline()

lista = lista_adiacenta(n,m,list,"neorientat")

v = []
print(EK(1,6,lista,n,rest))
f.close()   