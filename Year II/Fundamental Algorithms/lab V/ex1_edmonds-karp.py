import sys
import queue

def lista_adiacenta(n,m,list,o):
    matx = [[]for i in range(n+1)] 

    if o == "neorientat":
        for i in list:
            matx[i[0]].append((i[1],i[2],i[3]))
            matx[i[1]].append((i[0],i[2],i[3]))
    elif o == "orientat":
        for i in list:
            matx[i[0]].append((i[1],i[2],i[3]))

    return matx

f = open("grafpond.in","r")
n = int(f.readline())
visited = []
tati = [0]*(n+1)

def BFShelp(start, list):
    v = []
    q = queue.Queue()
    q.put(start)

    while not q.empty():
        nod = q.get()
        if nod not in v:
            v.append(nod)
            for i in list[nod]:
                q.put(i[0])
    
    return v


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


def verif(list, start, finish, n):
    ok = True
    v = BFShelp(start, list)
    if len(set(v)) != n:
        ok = False
    iesire = 0
    intrare = 0
    for i in list[start]:
        iesire += i[2]
    for i in list[finish]:
        intrare += i[2]
    if iesire != intrare:
        ok = False
    for i in list:
        for j in i:
            if j[2] > j[1]:
                ok = False
    return ok


def bridges(start, list, capacity, rest, n):
    v = []
    v.append(start)
    rez = []
    i = 1

    for i in range(n):
        if i<len(v):
            for j in list[v[i]]:
                if capacity[v[i]][j[0]]-rest[v[i]][j[0]] == capacity[v[i]][j[0]] and capacity[v[i]][j[0]] != 0:
                    if (v[i],j[0]) not in rez:
                        rez.append((v[i],j[0]))
                else:
                    v.append(j[0])
    return rez
        


list = []

l = f.readline()
start = int(l.split()[0])
finish = int(l.split()[1])
m = int(f.readline())


rest = [[0]*(n+1) for i in range (n+1)]
capacity = [[0]*(n+1) for i in range (n+1)]

l = f.readline()
while l:
    list.append((int(l.split()[0]), int(l.split()[1]), int(l.split()[2]), int(l.split()[3])))
    rest[int(l.split()[0])][int(l.split()[1])] = int(l.split()[2])
    rest[int(l.split()[1])][int(l.split()[0])] = -int(l.split()[3])
    capacity[int(l.split()[0])][int(l.split()[1])] = int(l.split()[2])
    l = f.readline()


lista = lista_adiacenta(n,m,list,"neorientat")
graf = lista_adiacenta(n,m,list,"orientat")

v = []
f.close()   

print(verif(lista, start, finish, n))
print(EK(1,6,lista,n,rest))

for i in range(n+1):
    for j in range(n+1):
        if capacity[i][j] != 0:
            print(str(i)+" "+str(j)+" ",end="")
            if rest[i][j] == 0:
                print(capacity[i][j],end="\n")
            else:
                print(capacity[i][j]-rest[i][j],end="\n")

print(bridges(start, graf, capacity, rest, n))
